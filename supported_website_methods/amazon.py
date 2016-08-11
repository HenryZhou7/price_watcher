# This file contains functions that are used to extract the price from amazon

import urllib2
import requests


# Given a url_address to the product. 
# Return the value of the product
def get_price_amazon(url_address):
    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(url_address)
    html = response.read()
    
    #page = requests.get(url_address)
    #html = page.text                # html is a string
    
    # Find two of the important keywords
    keyword1 = "id=\"priceblock_dealprice\""
    keyword2 = "id=\"priceblock_ourprice\""
    
    price = 0
    price_found = False
    
    if html.find(keyword1) != -1:   # Match pattern 1
        
        price_found = True
        indicator = html.find(keyword1)
        temp_substring = html[indicator:]
        start = temp_substring.find("$")
        end = temp_substring.find("/")
        price_str = temp_substring[start + 1: end - 1]
        price = float(price_str)
        
    elif html.find(keyword2) != -1:     # Match pattern 2
        price_found = True
        indicator = html.find(keyword2)
        temp_substring = html[indicator:]
        start = temp_substring.find("$")
        end = temp_substring.find("/")
        price_str = temp_substring[start + 1: end - 1]
        price = float(price_str)
        
    else:
        # Do nothing
        return price
    
    return price