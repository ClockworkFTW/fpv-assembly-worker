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
            soup.find("div", class_="price--main")
            .findChild()
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

            parts = soup.find_all("div", class_="productitem")

            for part in parts:

                name = (
                    part.find("h2", class_="productitem--title").find("a").text.strip()
                )
                link = (
                    "https://racedayquads.com"
                    + part.find("h2", class_="productitem--title").find("a")["href"]
                )
                image = "https:" + part.find("img")["src"]

                data.append({"name": name, "link": link, "image": image})

        with open("parts-racedayquads.csv", "w", newline="") as file:

            writer = csv.writer(file)
            writer.writerow(["name", "link", "image"])

            for row in data:

                writer.writerow([row["name"], row["link"], row["image"]])

    except Exception as e:

        print(e)
