#a little trick to clear the string before executing everything

import os
os.system('clear')



#This file intends to scrap from a certain number from a string

original_string = "http://store.nike.com/ca/en_gb/pd/flyknit-lunar-3-running-shoe/pid-10191260/pgid-11101348"

target1 = "nike"
target2 = "amazon"

if original_string.find(target1) != -1:
    print "Yes it is from Nike"

if original_string.find(target2) == -1:
    print "Nope! This one is not"
    
#Here is a real-world example

#if a product on nike.com is on sale, it will contain the folling line
target = "exp-pdp-local-price nsg-text--nike-orange"

#open a list of extractions from html file
with open("html_test.txt") as f:
    content = f.readlines();
    
total_sources = len(content)

#See if it is on sale
for x in range(0, total_sources):
    if content[x].find(target) != -1:
        print "Yes! The item you stored is on sale!"
        start = content[x].find("$")
        end = content[x].find("/")
        temp = content[x][start + 1:end - 2]
        price = float(temp)
        print "The price on sale is: %f" % (price)