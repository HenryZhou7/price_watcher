#The user enters an URL from the product page from nike
#and then the program prints out the price for the specific product

import urllib2
from lxml import html
import requests

        
def get_price_nike(user_input):
    
    """
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    response = opener.open(user_input)
    html = response.read()
    """
    
    

    page = requests.get(user_input)
    html = page.text
    
    
    
    temp_text = open("nike_url_not_on_sale.txt", "w")
    temp_text.write(html)
    temp_text.close()
    
    
    return 0

"""
    temp_text = open("nike_url_not_on_sale.txt", "w")
    temp_text.write(page)
    temp_text.close()
 """   
    
    #Search each line for existence of the keyword
    #"exp-pdp-local-price nsg-text--nike-orange"
"""
    keyword = "exp-pdp-local-price"

    #read the files line-by-line
    with open("nike_url_not_on_sale.txt") as f:
        content = f.readlines();
    total_resources = len(content)

    price = 0
    
    for x in range(0, total_resources):
    
        if content[x].find(keyword) != -1: #Found the keyword, the price is in here
            print "The item is on sale!"
            start = content[x].find("$")
            end = content[x].find("/")
            temp = content[x][start + 1:end - 1]
            price = float(temp)
    return price
    
"""
temp_input = raw_input("Please enter a product page on Nike: ")

while temp_input != "quit":
    price = get_price_nike(temp_input)
    print "The item is on sale for: %f" % (price)
    temp_input = raw_input("Please enter a product page on Nike: ")

print "Thank you for using!" 
