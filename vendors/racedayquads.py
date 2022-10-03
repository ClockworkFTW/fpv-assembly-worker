def getPrice(soup):
    
    try:
        
        price = soup.find("div", class_="price--main").findChild().text.strip().replace("$","")
        return price
    
    except:

        return None