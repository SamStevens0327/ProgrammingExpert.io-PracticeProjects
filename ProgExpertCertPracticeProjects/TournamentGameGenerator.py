def get_num_teams():
    while True:
        num_teams = int(input("Enter the number of teams: "))

        if num_teams >=2:
            break

        print("The minimum number of teams is 2: ")

    return int(num_teams)

def get_team_names(x):
    team_names = []

    for i in range(x):
        while True:
            team_name = input(f"Enter the name of team #{i + 1}: ")
            num_words = len(team_name.split(" "))

            if num_words > 2:
                print("Team name can be no longer than 2 words.")
            elif len(team_name) < 2:
                print("Team name must be at least 2 characters long.")
            elif team_name in team_names:
                print("Name has already been taken.")
            else:
                break
            
        team_names.append(team_name)

    return team_names

def get_num_games(num_teams):
    while True:
        num_games = int(input("Enter number of games played by each team."))

        if num_games >= (num_teams - 1):
            break

        print("each team must play the other at least once.")
    
    return num_games

def get_num_wins(team_names, num_games):
    team_wins = []

    for team_name in team_names:
        while True:
            num_wins = int(input(f"Enter the number of wins for {team_name}: "))

            if num_wins > num_games:
                print(f"{team_name} only played {num_games} in total")
            elif num_wins < 0:
                print("Minimum number of wins is 0")
            else:
                break
            
        team_wins.append(num_wins)

    return team_wins

def generate_games(teams, team_wins, games):
    print("Generating games to be played in the first round of the tournament...")

    team_wins.sort()
    game = 1
    while game < games:
        team_1 = teams[-game]
        team_2 = teams[game - 1]

        print(f"Game {game}: {team_1} VS {team_2}")

        game += 1


num_teams = get_num_teams()
teams = get_team_names(num_teams)
games = get_num_games(num_teams)
wins = get_num_wins(teams, games)
generate_games(teams, wins, games)
