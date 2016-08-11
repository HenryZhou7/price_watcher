# This file contains functions accessing the price of items on Nike

import urllib2

#This product returns the original price of the url_address given
def get_price_nike(url_address):
    price = 0;
    
    response = urllib2.urlopen(url_address)
    url_content = response.read()
    
    
    temp_text_file = open("temp_url_data.txt", "w")
    temp_text_file.write(url_content)
    temp_text_file.close()
    
    # It turns out that this keyword is the indication of the appearance 
    # of the actual price of the item
    target = "exp-pdp-local-price"
    
    # Read the files line by line in search of the keyword
    with open("temp_url_data.txt") as f:
        content = f.readlines();
        
    total_lines = len(content)
    
    for x in range(0, total_lines):
        if content[x].find(target) != -1:
            start = content[x].find("$")
            end = content[x].find("/")
            temp = content[x][start + 1: end - 1]
            price = float(temp)
            return price
    
    return price
    