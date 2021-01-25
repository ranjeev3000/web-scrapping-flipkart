# -*- coding: utf-8 -*-
'''
Spyder Editor

This is a temporary script file.


from bs4 import BeautifulSoup as soup
from urlib.request import urlopen as uReq

my_url= 'https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'

uClient = uReq(my_url)

page_html = page.read(uClient)
uClient.close()


'''
from bs4 import BeautifulSoup as soup
import urllib.request
with urllib.request.urlopen('https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off') as response:
    page_html = response.read()
    
page_soup = soup(page_html,"html.parser")
containers= page_soup.findAll("div", {"class": "_4ddWXP"})
print(len(containers))

#print(soup.prettify(containers[0]))

container = containers[0]

print(container.div.img["alt"])
price= container.findAll("div", {"class": "_30jeq3"})
#print(price[0].text)

ratings= container.findAll("div", {"class": "_3LWZlK"})
#print(ratings[0].text)


filename = "product_info.csv"

f = open(filename,"w")
headers = "product name, price, ratings\n"
f.write(headers)

for container in containers:
    product_name = container.div.img["alt"]
    price_container = container.findAll("div", {"class": "_30jeq3"})
    price = price_container[0].text.strip()
    rating_container = container.findAll("div", {"class": "_3LWZlK"})
    rating = rating_container[0].text
    
    print("product name: " + product_name)
    print("price: " + price)
    print("ratings "+ rating)
    
    
    #sorting parsing
    trim_price = ''.join(price.split(','))
    rm_rupee = trim_price.split("₹")
    add_rs_price = "Rs." +rm_rupee[1]
    split_price = add_rs_price.split('E')
    final_price = split_price[0]
    
    split_rating = rating.split(" ")
    final_rating = split_rating[0]
    
    
    print(product_name.replace(",","|") + ","+ final_rating + "\n")
    
f.close()
