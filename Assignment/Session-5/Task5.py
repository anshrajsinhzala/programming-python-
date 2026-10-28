# 5.Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) and prints
# which one should use a list and which should use a tuple, explaining your choice in a comment

orders = ["pizza" , "burger" , "ice-cream"]
print(f'Zomato Order (list): {orders}')

ipl_team_names = ("MI" , "CSK" , "RCB" , "RR")
print(f'IPL Team (tuple): {ipl_team_names}')

# list: mutable - you can add,update or remove Zomato Order.
# tuple: immutable - you can not change indivisual team name after creation 