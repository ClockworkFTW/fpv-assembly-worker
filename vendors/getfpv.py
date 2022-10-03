def getPrice(soup):
    
    try:
        
        price = soup.find("meta", {"itemprop" : "price"})['content'].strip().replace("$","")
        return price
    
    except:

        return None