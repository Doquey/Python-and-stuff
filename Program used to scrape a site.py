#Setting the base to the looper
from bs4 import BeautifulSoup
from urllib.request import urlopen as Ureq
import requests
my_url = "https://www.newegg.com/p/pl?d=grafics+cards"
Ureq(my_url)
import pandas as pd
Uclient=Ureq(my_url)
pagehtml = Uclient.read()
Uclient.close()
soup = BeautifulSoup(pagehtml,"html.parser")
item_container = soup.findAll('div',class_='item-container')
contain = item_container[0]


#Creating the loop itself
product_name1 = []
item_shipping1 = []
product_price1 = []
brand1 = []
Data = pd.DataFrame()

for contain in item_container:
    Brand = contain.div.div.a.img['title']
    item_title = contain.findAll('a',class_='item-title')
    product_name = item_title[0].text.replace(",", " ")
    item_shipping = contain.findAll('li',class_='price-ship')[0].text.strip().replace(",", " ")
    product_price = contain.findAll('li',class_='price-current')[0].strong.text.replace(",", " ")
    product_name1.append(product_name)
    item_shipping1.append(item_shipping)
    product_price1.append(product_price)
    brand1.append(Brand)
Data['product-name'] = product_name1
Data['item-shipping'] = item_shipping1
Data['product-price'] = product_price1
Data['Brand'] = brand1
print(Data)
# saving the dataframe 
Data.to_csv('Product_data.csv')