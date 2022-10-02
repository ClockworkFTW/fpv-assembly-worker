import requests
from bs4 import BeautifulSoup


def getPrice(product_url):
    
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    price = soup.find("span", id="ProductPrice-product-template").text.strip().replace("$","")

    return price