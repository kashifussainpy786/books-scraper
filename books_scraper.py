import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://books.toscrape.com"
wb = Workbook()
ws = wb.active
ws.append(['title'])
for i in range(1,51):
	url = f"https://books.toscrape.com/catalogue/page-{i}.html"
	request = requests.get(url)
	soap = BeautifulSoup(request.text, "html.parser")
	s = soap.find_all('h3')
	# print(s)

	for h3 in s:
		a = h3.find('a')
		ws.append([a["title"]])

wb.save("C:/Users/aaaa/Downloads/MY PYTHON LEARNING/scraping.xlsx")
wb.save("scraping.xlsx")
print("Done")
try:
    wb.save("scraping.xlsx")
    print("Saved")
except Exception as e:
    print(e)