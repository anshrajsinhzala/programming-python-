# 4.You have a list of song durations (in seconds) from your Spotify playlist. Use a for loop with enumerate to print each song's 
# position (starting from 1) and its duration in the format: 'Song 1: 210 seconds'.

song_duration = [100 , 200 , 250 , 280 , 320]

for index , duration in enumerate(song_duration,start=1):
    print(f'song {index}: {duration} seconds')