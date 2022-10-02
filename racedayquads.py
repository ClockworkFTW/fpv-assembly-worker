import requests
from bs4 import BeautifulSoup


def getPrice(product_url):
    
    response = requests.get(product_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    price = soup.find("div", class_="price--main").findChild().text.strip().replace("$","")

    return price