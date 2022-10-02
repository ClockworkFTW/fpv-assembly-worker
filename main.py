from datetime import date
import getfpv
import pyrodrone
import racedayquads

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
    today = date.today()

    if part['vendor'] == "getfpv":
        price = getfpv.getPrice(part['product_url'])
    
    if part['vendor'] == "pyrodrone":
        price = pyrodrone.getPrice(part['product_url'])

    if part['vendor'] == "racedayquads":
        price = racedayquads.getPrice(part['product_url'])

    vendor = part['vendor']
    
    print(today, price, vendor)