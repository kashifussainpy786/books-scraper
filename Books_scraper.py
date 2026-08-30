import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://books.toscrape.com"
wb = Workbook()
ws = wb.active
ws.append(["title","price","rating"])
for i in range(1,51):
    url = f"https://books.toscrape.com/catalogue/page-{i}.html"
    request = requests.get(url)
    soap = BeautifulSoup(request.text, "html.parser")
    s = soap.find_all('h3')
    # print(s)

    for h3 in s:
        a = h3.find('a')
        article = h3.parent
        price = article.find('p', class_='price_color').text
        rating = article.find('p', class_='star-rating')["class"][1]
        ws.append([a["title"],price,rating])

wb.save("C:/Users/aaaa/Downloads/MY PYTHON LEARNING/scraping.xlsx")
#wb.save("/storage/emulated/0/My python learning/scraping.xlsx")
