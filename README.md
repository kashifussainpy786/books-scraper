# Books Scraper

A Python web scraper that extracts title, price, and rating of all 1000 books from [books.toscrape.com](https://books.toscrape.com) across 50 pages and exports them to an Excel file.

## Tools Used
- Python
- BeautifulSoup (bs4)
- requests
- openpyxl

## What It Does
- Scrapes 50 pages automatically
- Extracts book title, price, and rating for each book
- Saves output to `scraping.xlsx`

## How to Run
1. Install dependencies:
   pip install requests bs4 openpyxl
2. Run the script:
   python books_scraper.py
3. Output file `scraping.xlsx` will be created in the same folder

## Output
Excel file with 1000 books — three columns: Title, Price, Rating.
