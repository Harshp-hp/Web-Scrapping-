from bs4 import BeautifulSoup
import requests

url = 'https://economictimes.indiatimes.com/markets/stocks/news'

req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
soup1 = BeautifulSoup(soup.prettify(), 'html.parser')

#print(soup1)

raw_data = soup1.find_all("div", class_ = "eachStory")
stock_news = ""
for data in raw_data:
    news = data.h3.a['href']
    stock_news += '\u2022' + news + "\n"

print(stock_news)