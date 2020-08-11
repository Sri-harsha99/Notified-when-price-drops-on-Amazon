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
products = ['https://www.flipkart.com/microsoft-xbox-one-wireless-controller-bluetooth-with-3-5-mm-jack-white-motion/p/itmf4pzhyrjhxsms?pid=ACCF4P9WCSHAYSHS&lid=LSTACCF4P9WCSHAYSHSNKLJYU&marketplace=FLIPKART&fm=gamificationAndPersonalisation%2FrecentlyViewed&iid=GAP_RECENTLY_VIEWED_DESKTOP_HORIZONTAL_cfb29d1a-3609-42f1-a1e1-662067796672.ACCF4P9WCSHAYSHS&ppt=pp&ppn=pp&ssid=2hxpqmuyz40000001597121724554&otracker=pp_recently_viewed_Recently%2BViewed_4_36.productCard.RECENTLY_VIEWED_Recently%2BViewed_ACCF4P9WCSHAYSHS_gamificationAndPersonalisation%2FrecentlyViewed_3&otracker1=pp_recently_viewed_PINNED_gamificationAndPersonalisation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_4_NA_view-all&cid=ACCF4P9WCSHAYSHS',
            'https://www.flipkart.com/microsoft-wireless-controller-bt-wht-gamepad/p/itmemsyduqwggyg3?pid=ACCEMSYDJDGC2WUV&lid=LSTACCEMSYDJDGC2WUVPXFLTI&marketplace=FLIPKART&fm=gamificationAndPersonalisation%2FrecentlyViewed&iid=GAP_RECENTLY_VIEWED_DESKTOP_HORIZONTAL_ba47a6fb-6827-48a2-94ac-9e65ed17d10e.ACCEMSYDJDGC2WUV&ppt=pp&ppn=pp&ssid=2hxpqmuyz40000001597121724554&otracker=pp_recently_viewed_Recently%2BViewed_1_36.productCard.RECENTLY_VIEWED_Recently%2BViewed_ACCEMSYDJDGC2WUV_gamificationAndPersonalisation%2FrecentlyViewed_0&otracker1=pp_recently_viewed_PINNED_gamificationAndPersonalisation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_1_NA_view-all&cid=ACCEMSYDJDGC2WUV',
            'https://www.flipkart.com/microsoft-xbox-one-wireless-controller-bluetooth-gamepad/p/itmff8u3mz3yysf4?pid=ACCE7AV9TZHHAESC&lid=LSTACCE7AV9TZHHAESCSTRHQS&marketplace=FLIPKART&fm=gamificationAndPersonalisation%2FrecentlyViewed&iid=GAP_RECENTLY_VIEWED_DESKTOP_HORIZONTAL_cfb29d1a-3609-42f1-a1e1-662067796672.ACCE7AV9TZHHAESC&ppt=pp&ppn=pp&ssid=2hxpqmuyz40000001597121724554&otracker=pp_recently_viewed_Recently%2BViewed_3_36.productCard.RECENTLY_VIEWED_Recently%2BViewed_ACCE7AV9TZHHAESC_gamificationAndPersonalisation%2FrecentlyViewed_2&otracker1=pp_recently_viewed_PINNED_gamificationAndPersonalisation%2FrecentlyViewed_Recently%2BViewed_DESKTOP_HORIZONTAL_productCard_cc_3_NA_view-all&cid=ACCE7AV9TZHHAESC']
to_refresh = 600 


def openlink(link):
    webbrowser.open(link)


date_time_obj=datetime.datetime.now()
minim_price = 999999
minim_link = ''
sold = 'Sold Out'

toaster = ToastNotifier()

while(1):
    price_array = []
    for i in products:
        source = requests.get(i).text
        soup = BeautifulSoup(source,features='lxml')
        price = soup.find('div',class_='_1vC4OE _3qQ9m1').text
        price = price.replace(',','')
        price = int(price[1:])
        try:
            out = soup.find('div',class_='_9-sL7L').text
        except:
            price_array.append(price)
            if minim_price != min(price,minim_price):
                minim_link = i  
                minim_price = min(price,minim_price)
    print(minim_price)
    print(minim_link) 
    if(accepted_price >= minim_price):
        toaster.show_toast("PRICE DROP", "Get the product on Amazon", duration = 120 ,callback_on_click=lambda: openlink(minim_link)) 
        break

    time.sleep(to_refresh)   
