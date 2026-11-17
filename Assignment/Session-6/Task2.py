# 2.Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. 
# Then, delete one influencer from the dictionary and print the updated dictionary.

insta_followers = {                                   #key = username   value = Follower
    "Kohli" : 10000 , 
    "Rohit" : 15000, 
    "Mrbeast" : 20000 , 
    "Therock"  : 25000 , 
    "Cristiano" : 30000
    }  

# Add new influencer
insta_followers ["Leomessi"] = 40000

# Update the follower count
insta_followers ["Kohli"] = 50000

# delete one influencer
del insta_followers["Cristiano"]

print("Update Dictionary: ")
print(insta_followers)