# 5.Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart, use a loop to sum the prices.
# If an item price is 0 (out of stock), skip it. Stop adding items if the running total crosses ₹2000 using break, and print the final
# total.<br><br><em><strong>Constraint:</strong> Use both break and continue in your solution.</em>


# prices = [500 , 0 , 700 , 250 , 300 , 500 , 750]

# total = 0

# for price in prices:

    # if price == 0:
    #     print("Please! add item into cart")
#         continue

#     total = total + price

#     if total > 2000:
#         print("Stop Adding Item into Cart value is cross 2000")
#         break

# print("Total price of Shopping cart : ",total )


prices = [500 , 0 , 700 , 250 , 300 , 500 , 750]

i = 0
total = 0

while i < len(prices):
    price = prices[i]

    if price == 0:
        print("please add item into cart")
        continue

    total = total + price

    if total > 2000:
        print("Stop Add Item into Cart value is cross 2000")
        break

print("Total Value Of Cart : ",total)