# 3.Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, write code to display all
# items that cost more than ₹200.

food_prices = {                                      #key = item     value = prices
    "Pizza" : 280 ,
    "Burger" : 80 ,
    "Hot Choco" : 250 ,
    "COld Coffee" : 210 ,
    "Chienese" : 100 ,
}

print("Food item cost more than 200: ")

for item,price in food_prices.items():
    if price > 200:
        print(f'{item} : ₹ {price} ')