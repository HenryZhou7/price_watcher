# This is the main program of the command line app, Price Watcher
# The app will store the product url from the website
# and once there is a deal going on, the program will alert you
# There is no limitation on how many items can be on the list
# But obviously, the more you add, the more time-consuming it will be
# The website can support nike.com


import os
from commodity import Commodity     # The item class for holding the information
from procedural_functions import *  # Necessary functions written in another file


# Here starts the main program
os.system("clear")
print "Welcome to using this command line program, Price Watcher"


# A list of items to store all the data 
# Initialize it with the previously saved data
wishlist = load_data_from_file()
print_instruction()

while True:
    instruction = raw_input("Please enter what you want to do: ")
    os.system("clear")
    if instruction == "quit":
        break
    elif instruction == "all":
        print_wishlist(wishlist)
    elif instruction == "clear":
        clear_wishlist(wishlist)
    elif instruction == "add":
        add_commodity(wishlist)
    elif instruction == "delete":
        delete_commodity(wishlist)
    elif instruction == "update":
        update_commodity_price(wishlist)
    elif instruction == "check":
        check_on_sale(wishlist)
    elif instruction == "help":
        print_instruction()
    else:
        print "Invalid command. Please enter again."

# Store the data into a file for next time use
store_data(wishlist)

os.system("clear")

print "Thank you for using the program."
print "We will store your wishlist to keep track of the price"
print "Hope to see you again"
print "Goodbye!"