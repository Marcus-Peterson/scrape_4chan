import os
import re
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
class PostScraper:
    def __init__(self, csv_path, json_dir='datasets', json_file='post_replies_dataset.json'):
        self.csv_path = csv_path
        self.json_dir = json_dir
        self.json_path = os.path.join(json_dir, json_file)
        os.makedirs(self.json_dir, exist_ok=True)  # Ensure the directory exists
        if not os.path.isfile(self.json_path):
            with open(self.json_path, 'w') as f:  # Initialize an empty JSON if not exists
                json.dump({'question': [], 'none_question': []}, f)

    def load_links(self):
        df = pd.read_csv(self.csv_path)
        return df['Link'].tolist()

    def scrape_posts(self):
        links = self.load_links()
        print(f"Starting to scrape {len(links)} posts...")
        for index, link in enumerate(links, start=1):
            print(f"Scraping post {index} of {len(links)}: {link}")
            try:
                page_content = requests.get(link).text
                soup = BeautifulSoup(page_content, 'html.parser')
                main_post = self.scrape_post_content(soup)
                replies = self.scrape_replies(soup)

                category = 'question' if self.is_question(main_post) else 'none_question'
                # Load existing data safely
                try:
                    with open(self.json_path, 'r', encoding='utf-8') as f:
                        self.dataset = json.load(f)
                except json.JSONDecodeError as e:
                    print(f"JSON decode error: {e}")
                    print("Creating a new dataset...")
                    self.dataset = {'question': [], 'none_question': []}

                # Append new data
                self.dataset[category].append({'post': main_post, 'replies': replies})
                # Save back to JSON
                self.save_to_json()
                print(f"Saved data for post {index}.")
            except requests.RequestException as e:
                print(f"An error occurred while fetching the page: {e}")
                continue
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
                continue


    def scrape_post_content(self, soup):
        post_content = soup.find('blockquote', class_="postMessage").get_text(strip=True)
        return post_content

    def scrape_replies(self, soup):
        replies = []
        for reply in soup.find_all('div', class_="post reply"):
            reply_content = reply.find('blockquote', class_="postMessage")
            if reply_content:
                replies.append(reply_content.get_text(strip=True))
        return replies

    def is_question(self, text):
        return bool(re.search(r'\?\s*$', text))

    def save_to_json(self):
        with open(self.json_path, 'w') as f:
            json.dump(self.dataset, f, indent=4)
            print(f"Data saved to {self.json_path}")
        # Print out the JSON object that was just saved
        print(json.dumps(self.dataset, indent=4))

# Usage
#scraper = PostScraper(csv_path='datasets/my_threads_4chan.csv',json_file="my_threads_on_4chan.json")

#scraper.scrape_posts()
#time.sleep(10)

