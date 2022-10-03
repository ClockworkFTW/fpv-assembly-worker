def getPrice(soup):
    
    try:
        
        price = soup.find("span", id="ProductPrice-product-template").text.strip().replace("$","")
        return price
    
    except:

        return None