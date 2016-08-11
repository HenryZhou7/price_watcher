# File for a class Commodity
# Each Commodity has three data members
# url_address: a string containing the weblink url address
# original_price: a float of the original price of the item
# current_price: a float of the real-time price of the item

class Commodity:
    
    #constructor
    def __init__(self, url, first_price, curr_price):
        self.url_address = url
        self.original_price = first_price
        self.current_price = curr_price
    
    
        
    # Update the real-time price, the price may go up, go down or stay the same
    def update(self, updated_price):
        self.current_price = updated_price
        
    # Check if the price have gone down
    # If the price have gone down, then give indication to the user
    # Otherwise, do nothing
    def check(self):
        if self.current_price < self.original_price:
            # Found an item that is on sale
            print "Item whose URL is: %s" % (self.url_address)
            print "The price drops from %f to %f" % (self.original_price, self.current_price)
            return True
        else:
            return False
    
    