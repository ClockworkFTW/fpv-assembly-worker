import csv
import requests
from datetime import date
from bs4 import BeautifulSoup


def getPrice(url):
    """"""

    try:

        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        price = (
            soup.find("span", id="ProductPrice-product-template")
            .text.strip()
            .replace("$", "")
        )

        return price

    except:

        return None


def scrapeParts(url, pages):
    """"""

    try:

        data = []

        for page in range(1, pages):

            response = requests.get(url + str(page))
            soup = BeautifulSoup(response.content, "html.parser")

            parts = soup.find_all("div", class_="grid-view-item")

            for part in parts:

                name = part.find("a", class_="grid-view-item__title").text.strip()
                link = (
                    "https://pyrodrone.com"
                    + part.find("a", class_="grid-view-item__title")["href"]
                )
                image = "https:" + part.find("img")["src"]

                data.append({"name": name, "link": link, "image": image})

        with open("parts-pyrodrone.csv", "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["name", "link", "image"])

            for row in data:

                writer.writerow([row["name"], row["link"], row["image"]])

    except:

        print("error")
