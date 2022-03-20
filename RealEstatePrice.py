from bs4 import BeautifulSoup
import requests
from csv import writer

url = 'https://www.pararius.com/apartments/amsterdam?ac=1%22'
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")
soup1 = BeautifulSoup(soup.prettify(), "html.parser")

## Scrap the Data from the Web

raw_data = soup.find_all("section", class_ = "listing-search-item")

## Create a CSV File for the data

with open('housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Title', 'Location', 'Area', 'Features', 'Price']
    thewriter.writerow(header)

    for data in raw_data:
        title = data.find('a', class_ = "listing-search-item__link--title").text.replace("\n","")
        location = data.find("div", class_ = "listing-search-item__location").text.replace("\n","")
        price = data.find("div", class_ = "listing-search-item__price").text.replace("\n","")
        features = data.find("div", class_ = "listing-search-item__features").text.replace("\n","")
        area = data.find("a", class_ = "listing-search-item__link").text.replace("\n","")
        info = [title, location,area,features,price]
        #print(info)
        thewriter.writerow(info)

