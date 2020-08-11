from bs4 import BeautifulSoup
import requests
import re
import webbrowser
import time
import datetime
from win10toast import ToastNotifier
import webbrowser

# Change Based on your preferences
accepted_price = 3500
products = ['https://www.amazon.in/Microsoft-Xbox-%E0%A4%B5%E0%A4%BE%E0%A4%AF%E0%A4%B0%E0%A4%B2%E0%A5%87%E0%A4%B8-%E0%A4%95%E0%A4%82%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%B2%E0%A4%B0-%E0%A4%AC%E0%A5%8D%E0%A4%B2%E0%A5%82%E0%A4%9F%E0%A5%82%E0%A4%A5/dp/B01MR1Z7JJ/ref=sr_1_1?crid=I30Z6HMGI7AQ&dchild=1&keywords=xbox+one+controller&qid=1597147443&sprefix=xb%2Caps%2C297&sr=8-1',
            'https://www.amazon.in/Microsoft-Xbox-%E0%A4%B5%E0%A4%BE%E0%A4%AF%E0%A4%B0%E0%A4%B2%E0%A5%87%E0%A4%B8-%E0%A4%95%E0%A4%82%E0%A4%9F%E0%A5%8D%E0%A4%B0%E0%A5%8B%E0%A4%B2%E0%A4%B0-%E0%A4%AC%E0%A5%8D%E0%A4%B2%E0%A5%82%E0%A4%9F%E0%A5%82%E0%A4%A5/dp/B06X92RN9D/ref=sr_1_3?crid=I30Z6HMGI7AQ&dchild=1&keywords=xbox+one+controller&qid=1597147443&sprefix=xb%2Caps%2C297&sr=8-3']
to_refresh = 600 

# code
def openlink(link):
    webbrowser.open(link)

date_time_obj=datetime.datetime.now()
minim_price = 999999
minim_link = ''

toaster = ToastNotifier()


while(1):
    for i in products:
        page = requests.get(i,headers={"User-Agent":"Defined"})
        soup = BeautifulSoup(page.content, "html.parser")
        try:
            price = soup.find(id="priceblock_dealprice").get_text()
        except:
            price = soup.find(id="priceblock_ourprice").get_text()
        price = price.replace(',','')
        price = price.replace('.','')
        price = int(price[3:-2])
        
        if minim_price != min(price,minim_price):
            minim_link = i  
            minim_price = min(price,minim_price)
    print(minim_price)
    print(minim_link) 
    if(accepted_price >= minim_price):
        toaster.show_toast("PRICE DROP", "Get the product on Amazon", duration = 120 ,callback_on_click=lambda: openlink(minim_link)) 
        break

    time.sleep(to_refresh)   





