#3.Simulate removing the last played song from your playlist_ids list using pop(), and display the removed ID along with the remaining playlist.

playlist_ids = [101, 220, 335, 445, 555, 765, 842]
removed_id = playlist_ids.pop()
print(f"deleted item: {removed_id}")
print(f'updated list: {playlist_ids}')