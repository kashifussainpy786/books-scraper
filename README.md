# Books Scraper

A Python web scraper that extracts all 1000 book titles from [books.toscrape.com](https://books.toscrape.com) across 50 pages and exports them to an Excel file.

## Tools Used
- Python
- BeautifulSoup (bs4)
- requests
- openpyxl

## What It Does
- Scrapes 50 pages automatically
- Extracts full book titles using HTML attribute parsing
- Saves output to `scraping.xlsx`

## How to Run
1. Install dependencies:
   pip install requests bs4 openpyxl
2. Run the script:
   python scraper.py
3. Output file `scraping.xlsx` will be created in the same folder

## Output
Excel file with 1000 book titles, one per row.
