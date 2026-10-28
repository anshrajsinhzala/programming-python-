# Add two more song IDs to your playlist_ids list using both append() and extend(), then print the updated list.<br><br><em><strong>
# Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>

# append() Method

playlist_ids = [101 , 220 , 335 , 445 , 555 ,]
playlist_ids.append("666")
print(playlist_ids)


# extend() Method

playlist_ids = [101 , 220 , 335 , 445 , 555 ,]
playlist_id = [765 , 842 ]
playlist_ids.extend(playlist_id)
print(playlist_ids)