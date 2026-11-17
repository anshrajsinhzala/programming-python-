# 3.Write a Python function that takes a list of IPL team names and prints only those teams whose names are longer than 6 characters,
# skipping the rest using the continue statement

def ipl_team(team):

    for team in ipl_teams:
        if len(team) <= 6:
            continue
        print(team)

ipl_teams = [
    "CSK",
    "Mumbai",
    "RCB",
    "Gujarat",
    "LSG",
    "Rajsthan"
]

ipl_team(ipl_teams)