import requests
from datetime import date
from bs4 import BeautifulSoup

from vendors import getfpv, pyrodrone, racedayquads

# TODO: Connect to database and get parts

parts = [
    {
        "vendor": "getfpv",
        "product_url": "https://www.getfpv.com/iflight-xing2-2506-1350kv-1650kv-1850kv-motor.html"
    },
    {
        "vendor": "getfpv",
        "product_url": "https://www.getfpv.com/rushfpv-rush-blade-60a-3-6s-blheli-32-4-in-1-esc-extreme-edition-30x30.html"
    },
    {
        "vendor": "getfpv",
        "product_url": "https://www.getfpv.com/armattan-odonata-1-6-nano-quadcopter-frame-kit.html"
    },
    {
        "vendor": "pyrodrone",
        "product_url": "https://pyrodrone.com/products/iflight-xing2-2506-1350kv-motor"
    }, 
    {
        "vendor": "racedayquads",
        "product_url": "https://www.racedayquads.com/products/emax-eco-ii-2306-2400kv-motor"
    },
]

for part in parts:

    response = requests.get(part['product_url'])
    soup = BeautifulSoup(response.content, 'html.parser')

    if part['vendor'] == "getfpv":
        price = getfpv.getPrice(soup)
    
    if part['vendor'] == "pyrodrone":
        price = pyrodrone.getPrice(soup)

    if part['vendor'] == "racedayquads":
        price = racedayquads.getPrice(soup)

    vendor = part['vendor']
    today = date.today()
    
    # TODO: Save prices to database

    print(today, price, vendor)