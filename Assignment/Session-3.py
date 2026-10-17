"""Task-1:- Declare four variables in Python: your age as an int, your height in centimeters as a float, your name as a str, and
whether you have a Spotify account as a bool. Print each variable and use the type() function to display its data type."""

age=20                      #integar
height_cm=154.55            #Float
name="Zala Anshrajsinh"     #String
has_spotify_acc=True        #boolean

print("Age : ", age , type(age))
print("Height : ", height_cm , type(height_cm))
print("Name : ", name , type(name))
print("Spotify Account : ", has_spotify_acc , type(has_spotify_acc))




"""Task-2:- Write a function total_cart_amount(prices) that takes a list of product prices as strings
(like ['199.99', '49', '350.75']) and returns the total as a float. Print the result for a sample Flipkart-style cart.
<br><br><em><strong>Hint:</strong> Use float() to convert each string before summing.</em>"""

def total_cart_amount(prices):
    total = 0.0

    for price in prices:
        total += float(price)

    return total


# Sample Flipkart cart
cart_prices = ['199.99', '49', '350.75']

result = total_cart_amount(cart_prices)
print("Total Cart Amount: ₹", result)




"""Task-3:- Create a script that asks the user to input their cricket score as a string, converts it to an int, and prints
'Half-century!' if the score is 50 or more, otherwise prints 'Keep going!'.<br><br><em><strong>Constraint:</strong> Use input(),
int(), and if-else.</em>"""

score=input("Enter your Cricket Score : ")

score=int(score)

if score >=50:
    print("Half-Century!")
else:
    print("Keep Going")




"""Task-4:- Given the variable is_premium = 'True' (as a string), write code to correctly convert it to a boolean value and
print its type.<br><br><strong>Hint:</strong> The bool() function alone won’t work as expected. Think about string comparison."""

is_premium = 'True'

#Convert String to Boolean
is_premium = (is_premium == 'True')

print("Premium Status : ", is_premium)
print("Data Type: ",type(is_premium))