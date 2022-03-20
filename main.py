from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests


URL = "https://www.businesstoday.in/coronavirus"
req = requests.get(URL)
soup = BeautifulSoup(req.content, "html.parser")
soup1 = BeautifulSoup(soup.prettify(), "html.parser")

data = soup1.find_all("div", class_="widget-listing")
finaldata = ""
for d in data:
    news = d.div.div.a['title']
    finaldata += '\u2022' + news + "\n"
print(finaldata)



