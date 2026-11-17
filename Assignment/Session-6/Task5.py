# 5.Write a function get_unique_artists(spotify_playlist1, spotify_playlist2) that takes two sets of artist names and returns a set
# of all unique artists across both playlists (set union).<br><br><em><strong>Hint:</strong> Use the union() method or the | operator
# for sets.</em>

def get_unique_artists(spotify_playlist1, spotify_playlist2):
    unique_artists = spotify_playlist1.union(spotify_playlist2)
    return unique_artists

spotify_playlist1 = {"Arjit Singh" , "Sonu Nigam" , "Darshan Raval"}
spotify_playlist2 = {"Gaman Santhal" , "RAjbha Gadhvi" , "Arjit Singh"}

print("Unique Artist: ",get_unique_artists(spotify_playlist1, spotify_playlist2))