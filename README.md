
# 4chan Scraping Toolkit 🕵️‍♂️📊

## Overview 📚
This toolkit is designed for scraping **text data** from 4chan, ideal for research in fields like hate speech detection and online discourse analysis. It includes tools for scraping archived posts and processing individual threads.

## Components 🛠️
- **Archive Scraper (`chan_archive_scraper.py`)**: This script scrapes archived threads from a specified 4chan board. It saves the data in a CSV format, listing post numbers and links.
- **Post Scraper (`chan_post_scraper.py`)**: This tool processes individual 4chan threads, classifying posts as questions or statements, and saves the data in JSON format.

## Installation and Setup 💻
1. Clone or download this repository.
2. Ensure Python is installed on your system.
3. Install required Python libraries: `requests`, `pandas`, `regex`,  `bs4` (BeautifulSoup), and `json`.

## Usage 🚀
- **Archive Scraper**:
  ```python
  python chan_archive_scraper.py
  ```
  The script will scrape the archive and output a CSV file with post numbers and links.

- **Post Scraper**:
  ```python
  python chan_post_scraper.py
  ```

    ```python
  python chan_archive_scraper.py
  ```
  The script will scrape the archive and output a CSV file with post numbers and links.

- **Example usages**:
  ```
  See the directory: "datasets" for sample data

  scraper = ChanArchiveScraper('directory=datasets', 'file_name=sample_4chan_data.csv')
  csv_file = scraper.scrape_archive()

  scraper_posts = PostScraper(csv_path='datasets/sample_4chan_data.csv',json_file="sample_4chan_data.json")
  scraper_posts.scrape_posts()
  ```
  Customize the script with specific thread IDs or CSV paths as needed. The script will process the threads and output a JSON file with structured data.

## Contributing 🤝
Contributions to improve or extend the toolkit's functionality are always welcome. Feel free to fork, modify, and create pull requests.

## License 📃
This project is open-sourced under the MIT License.

## Disclaimer ⚠️
This toolkit is open-source, so use it as you wish. Be advised though, the collected data is guaranteed to contain offensive, hateful, racist and downright vile information. The main purpose of this toolkit is provide developers with a easy to use scraping toolkit that can provide ML or DL models with data to better train for example hatespeech detection systems. But you know, I am not your dad so I am not going to tell you what to do. Any psychological harm that has been caused by using this toolkit is your responsibility. 
Just as a knife can either be used to cut onions and chicken for a nice stew, that same knife can be used to stab someone. 
I as the author of the toolkit is not responsible for your reckless usage of this toolkit. 
