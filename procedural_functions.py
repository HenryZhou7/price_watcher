# To make the code more readable, I put some of the functions in this file
# These functions can totally go into the start of the main_program.py
# which will make the main_program.py exceptionally long.

import os
from commodity import Commodity     #include the class
# Different methods for accessing the price tage from various websites
from supported_website_methods.nike import *
from supported_website_methods.amazon import *


# The functions to give the user instructions on how to use the program
def print_instruction():
    print "This program can monitor the price of the items you found on the internet"
    print "And it will give you an alert once the item you stored previously\n"
    print "Here are what you can do: "
    print "To display your entire wishlist: enter \"all\""
    print "To clear your entire wishlist: enter \"clear\""
    print "Add an item to your wishlist: enter \"add\""
    print "Delete an item from your wishlist: enter \"delete\""
    print "Update the current price of all the items in your wishlist: enter \"update\""
    print "Check if anything on your wishlist is on sale: enter \"check\""
    print "Please update before check\n"
    print "Enter \"help\" to show the instruction again"
    print "Enter \"quit\" to quit the program"



# Display all the items in the wishlist
def print_wishlist(wishlist):
    os.system("clear")      # Some of the displaying format to optimize user experience
    print "Displaying all the items in the wishlist:\n" 
    
    total_items = len(wishlist)
    index = 1
    for x in range(0, total_items):
        print "Item No.%d" % index
        print "The URL is: %s" % wishlist[x].url_address
        print "The price when added is: $%f" % wishlist[x].original_price
        print "Its current price is: $%f\n" % wishlist[x].current_price
        index = index + 1
    print "End of the wishlist"
    return



# Clear all the items in the wishlist
def clear_wishlist(wishlist):
    user_response = raw_input("Are you sure you want to do this? This cannot be undone. Enter \"yes\" to continue: ")
    
    if user_response == "yes":
        del wishlist[:]
        print "Clearing process done."
    else:
        print "Nothing is done. Your wishlist stays the same."
        
    return
  
            

# In the beginning of the program, need to load the stored data back to the program        
# Scrapping from the file. Traverse all the lines and extract the data
# Construct an object of the class and append it to the list
def load_data_from_file():
    
    print "Loading data..."
    
    wishlist = []
    
    #Read from a file
    with open("stored_data.txt") as f:
        content = f.readlines()
    total_item_num = len(content)
    
    for x in range(0, total_item_num):
        each_entry = content[x].split()     # Break things up and store each entry
        temp_item = Commodity(each_entry[0], float(each_entry[1]), float(each_entry[2]))
        wishlist.append(temp_item)

    return wishlist
    


# When the user wants to add an item to the wishlist
# The program asks for the URL
# See if the url is one of the websites that the program supports
# Check to see if it is the same item by checking the price with the user
# Getting the price, construct an object and append it to the end of the list
def add_commodity(wishlist):
    url_input = raw_input("Please enter the URL link of the item: ")
    
    current_price = 0
    #Check to see if it is supported by the program
    if url_input.find("amazon") != -1:    
        current_price = get_price_amazon(url_input)
    elif url_input.find("nike") != -1:
        current_price = get_price_nike(url_input)
        
    # Re-ensure that it is the item by matching the price with the user
    user_response = raw_input("So it is $%f ? If correct, enter \"yes\" " % (current_price))
    
    if user_response != "yes":       # Fails to add. Doesn't match
        print "Adding process fails"
        print "Try it again"
        return
    else:
        temp_item = Commodity(url_input, current_price, current_price)
        wishlist.append(temp_item)
        print "The item with the url: %s is added" % (url_input)
      
    return



# When the user wants to delete an item from the wishlist
# Traverse throughout the whole wishlist
# If found, delete and return
# Otherwise, display error message
def delete_commodity(wishlist):
    url_input = raw_input("Please enter the URL of the item you want to delete: ")
    
    total_item = len(wishlist)
    
    exist = False
    
    for x in range(0, total_item):
        if wishlist[x].url_address == url_input:
            exist = True;
            temp_item = wishlist[x]
            wishlist.remove(temp_item)
            print "The item has been found and deleted from your wishlist"
            return
            
    if exist == false:
        print "The item you entered does not exist in your wishlist"
        print "Please try something elase"
    
    return



# When the user wants to update all the current prices of all the items in the list
# Traverse through the wishlist and check each of its current price
def update_commodity_price(wishlist):
    os.system("clear")
    print "Updating the information..."
    print "This could take a few minutes..."
    
    total_items = len(wishlist)
    
    for x in range(0, total_items):
        url_address = wishlist[x].url_address
        
        #Decide which method to use
        if url_address.find("amazon") != -1:
            curr_price = get_price_amazon(url_address)
            wishlist[x].update(curr_price)
        elif url_address.find("nike") != -1:
            curr_price = get_price_nike(url_address)
            wishlist[x].update(curr_price)
        
    os.system("clear")
    print "Thank you for waiting. All the prices are up-to-date."
    
    return



# Checking if anything in the list is on sale
# The case where the item's current price is lower than its original price
# Traverse through the wishlist
# Print out all the items that are on sale
# Give a total sum of all the on-sale items
def check_on_sale(wishlist):
    
    os.system("clear")
    
    total_on_sale = 0
    total_items = len(wishlist)
    for x in range(0, total_items):
        if wishlist[x].check() == True:
            total_on_sale = total_on_sale + 1
        else:
            continue
    
    # Give a summary, total number of on-sale items
    print "There are a total of " + str(total_on_sale) + " item(s) on sale."
    
    return



# Store the data into the file "stored_data.txt"
# Can substitute this with a database operation
def store_data(wishlist):
    total_items = len(wishlist)
    
    text_file = open("stored_data.txt", "w")
    
    for x in range(0, total_items):
        temp_string = "%s %f %f\n" % (wishlist[x].url_address, wishlist[x].original_price, wishlist[x].current_price)
        text_file.write(temp_string)
    
    text_file.close()
    
    return
    
    

