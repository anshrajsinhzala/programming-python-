"""Task-1 :- Create three variables in Python named item_price, delivery_fee, and coupon_discount, and assign them values 
representing a Swiggy order (e.g., 250, 30, 20). Print each variable."""

item_price = 250
delivery_fee = 30
coupon_discount = 20

print("Item Price:", item_price)
print("Delivery Fee:", delivery_fee)
print("Coupon Discount:", coupon_discount)




"""Task-2 :- Write a Python script that uses indentation correctly to check if a Flipkart product's price is above 1000; 
if yes, print 'Eligible for free delivery', else print 'Delivery charges apply'.<br><br><em><strong>Hint:</strong> Use an
if-else block and make sure your indentation is consistent.</em>"""

product_price =int(input("Enter Product Price : "))

if product_price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")




"""Task-3 :- Add both single-line and multi-line comments in your script explaining what each section does, using # for single-
line and triple quotes for multi-line comments."""

"""
This program checks whether a Flipkart product
is eligible for free delivery based on its price.
"""

# Store the product price
product_price = 1500

# Check if the price is above 1000
if product_price > 1000:
    print("Eligible for free delivery")
else:
    print("Delivery charges apply")




"""Task-4 :- Create variables for an IPL match: team_name, runs_scored, and overs_played. Assign appropriate values and print
them using the correct naming conventions for Python variables.<br><br><em><strong>Constraint:</strong> Use snake_case for all 
variable names.</em>"""

# Create variables using snake_case
team_name = "Chennai Super Kings"
runs_scored = 185
overs_played = 20

# Print the match details
print("Team Name:", team_name)
print("Runs Scored:", runs_scored)
print("Overs Played:", overs_played)