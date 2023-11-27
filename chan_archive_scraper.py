import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class ChanArchiveScraper:
    def __init__(self, directory='datasets', file_name='4chan_archive_extracted_links.csv'):    #Default to datasets and 4chan_archive_extracted_links.csv if directory or file_name is not defined
        self.base_url = 'https://boards.4chan.org'
        self.archive_url = urljoin(self.base_url, '/pol/archive')
        self.csv_file_path = os.path.join(directory, file_name)

    def scrape_archive(self):
        # Make the request
        data = requests.get(self.archive_url).text
        soup = BeautifulSoup(data, 'html.parser')

        # Find the table by ID
        table = soup.find('table', {'id': 'arc-list'})

        # Initialize an empty list to store the data
        rows_list = []

        # Iterate over each row in the found table
        for row in table.find_all('tr'):
            # Find the post number cell, continue if not found
            number_cell = row.find('td')
            if not number_cell:
                continue
            post_number = number_cell.get_text(strip=True)
            
            # Find the link cell with class 'quotelink' and create an absolute URL
            link_cell = row.find('a', {'class': 'quotelink'})
            if not link_cell:
                continue
            link = urljoin(self.base_url, link_cell['href'])
            
            # Append the post number and link to the list
            rows_list.append({'No': post_number, 'Link': link})

        # Convert the list of dictionaries into a DataFrame with the specified column names
        df_links = pd.DataFrame(rows_list, columns=['No', 'Link'])

        # Ensure the directory exists
        os.makedirs(os.path.dirname(self.csv_file_path), exist_ok=True)

        # Save the DataFrame to a CSV file without an index
        df_links.to_csv(self.csv_file_path, index=False)

        # Output the path to the CSV file
        return self.csv_file_path

# Usage:
#scraper = ChanArchiveScraper('my_directory', 'my_file_name.csv')
#csv_file = scraper.scrape_archive()
#print(f"Data saved to {csv_file}")
