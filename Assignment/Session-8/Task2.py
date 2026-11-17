# 2.Given a list of daily step counts for a week, use a while loop to find and print the first day when you crossed 10,000 steps.
# <br><br><em><strong>Hint:</strong> Loop through the list and stop as soon as you find a value greater than 10,000.</em>

steps = [5000 , 7500 , 9000 , 12000 , 8000 , 11000 , 9500]

days = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday" , "Saturday" , "Sunday"]

i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("First Day Crossed 10,000 steps: ",days[i])
        print("steps: ",steps[i])
        break
    i += 1
else:
    print("You did not cross 10000 steps this week" )