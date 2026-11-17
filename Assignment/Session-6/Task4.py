# 4.Create two sets: flipkart_users and myntra_users, each containing 5 unique usernames. Find and print the set of users who have
# accounts on both platforms using set intersection

flipkart_users = {"Jay" , "Ved" , "Meet" , "Tirth" , "Raj"}
myntra_users = {"Mihir" , "Rushi" , "Jay" , "Ved" , "Rudra"} 

common_users = flipkart_users.intersection(myntra_users)

print("Common user in both sets: ")
print(common_users)