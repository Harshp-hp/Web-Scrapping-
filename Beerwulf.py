from requests_html import HTMLSession
import pandas as pd

url = 'https://www.beerwulf.com/en-gb/c/beer-kegs/sub-kegs'
s = HTMLSession()
drinklist = []

def requests(url):
    r = s.get(url)
    r.html.render(sleep=1)
    return r.html.xpath('//*[@id="product-items-container"]', first=True)


def parse(products):
    for item in products.absolute_links:
        r = s.get(item)
        name = r.html.find('div.product-detail-info-title', first=True).text
        subtext = r.html.find('div.product-subtext', first=True).text
        price = r.html.find('div.product-detail-info-price', first=True).text
        desc = r.html.find('div.product-description', first=True).text

        if r.html.find('div.add-to-cart-container', first=True):
            stock = 'In-Stock'
        else:
            stock = 'Out-Of-Stock'

        drink = {
            'name': name,
            'subtext':subtext,
            'price':price,
            'desc': desc,
            'stock':stock
        }
        drinklist.append(drink)
def output():
    df = pd.DataFrame(drinklist)
    df.to_csv('drinklist.csv', index=False)




products = requests('https://www.beerwulf.com/en-gb/c/beer-kegs/sub-kegs')
parse(products)
output()
print(drinklist)