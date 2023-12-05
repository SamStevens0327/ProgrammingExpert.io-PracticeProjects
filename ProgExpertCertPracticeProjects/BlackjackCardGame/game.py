import random
import player
import sys

def start_game():
    while True:
        request = input("Type 'yes' to start or 'no' to exit; then hit Enter: ").lower()

        if request == "yes":
            print("Welcome to BlackJack!")
            start = True
            break
        elif request == "no":
            start = False
            break
        else:
            print("Enter either 'yes' or 'no'...")

    return start


def quit_program():
    print("Exiting the program.")
    sys.exit()


def invite_players():
    print(
        "Enter the names of all the players. "
        "Once all players are entered, type done to save the names."
        )
    
    players = []
    count = 1

    while True:
        player_name = input(f"Enter name of player {count}: ")

        if len(player_name) > 12:
            print("Name can be max 12 characters long")
        elif player_name.isspace() == True:
            print("Enter a name...")
        elif len(player_name) < 1:
            print("Please enter at least a character as a name.")
        elif player_name.lower() == "done":
            break
        else:
            new_player = player.Player(player_name)
            players.append(new_player)
            count += 1

    return players


def buy_sell_chips(players: list[player.Player]):
    for i in range(len(players)):
        players[i].status = True
        while True:
            x = input(f"{players[i].name}: How much chips would you like to buy?")

            try:
                x = float(x)
            except ValueError:
                print("Use a number!")
                continue
            if x == 0:
                print(f"You have ${players[i].stash} of chips to play with.")
                break
            elif x > 100000:
                print("Max buy is $100,000")
            elif x > 100 and x < 100000:
                players[i].stash += x
                players[i].wallet -= x
                print(f"You have ${players[i].stash} available to play with.")
                break
            elif x > 0 and x < 100:
                print("Minimum buy-in is $100.")
            elif x < 0 and abs(x) < players[i].stash:
                players[i].stash -= abs(x)
                players[i].wallet += abs(x)
                print(f"You now have ${players[i].stash} of chips to play with.")
                break
            elif x < 0 and abs(x) > players[i].stash:
                print("You don't have that many chips to sell.")

    return players


def add_deck(deck: dict()):
    deck += deck
    return deck


def buy_in(x: int, players: list[player.Player]):
    print(f"The minimum buy in for this round is ${x}")

    remaining_players = []
    broke_players = []
    for i in range(len(players)):
        if players[i].stash < x:
            print(f"{players[i].name} could not afford the buy in.")
            broke_players.append(players[i])
        elif players[i] not in broke_players:
            players[i].stash -= x
            players[i].bet += x
            remaining_players.append(players[i])

    return remaining_players


def deal(players: list[player.Player], deck: dict()):

    print("Dealing...")

    for _ in range(2):
        for i in range(len(players)):
            card = random.choice(list(deck.keys()))
            players[i].hand.append(card)
            deck.pop(card)
    
    return [players, deck]


def bet_round(players: list[player.Player], deck: dict()):
    
    print("Betting round...")

    for i in range(len(players)):
        if players[i].status == True:
            print(f"{players[i].name}, your hand is {players[i].hand}")

            while True:
                bet = input("What is your bet? ")
                if bet.lower() == "fold":
                    print(f"{players[i].name} folded.")
                    players[i].status = False
                else:
                    try:
                        bet = float(bet)
                    except ValueError:
                        print("Use a number!")
                        continue
                    if bet < 0:
                        print("Positive number please!")
                        continue
                    elif bet >= 0 and bet < players[i].stash:
                        players[i].stash -= bet
                        players[i].bet += bet
                        break
                    elif bet > players[i].stash:
                        print("You don't have that many chips to bet.")
                        continue
        else:
            print(f"{players[i].name} is not in this round.")
            continue


    return [players, deck]


def play_round(players: list[player.Player], deck: dict()):

    print("Dealing round...")

    for i in range(len(players)):
        if players[i].status == True:
            while True:
                play = input(f"{players[i].name}:\n"
                            f"Your hand is: {players[i].hand}\n"
                            "Would you like to hit or stick?")
                if play.lower() == 'hit':
                    card = random.choice(list(deck.keys()))
                    players[i].hand.append(card)
                    deck.pop(card)

                    for j in players[i].hand:
                        hand_val = 0
                        hand_val += deck[players[i].hand[j]]
                    

                    
                elif play.lower() == 'stick':
                    break
                elif play.lower() == 'fold':
                    players[i].status == False
                    print(f"{players[i].name} folded.")
                else:
                    print("Say either 'Hit' or 'Stick'!")
        else:
            print(f"{players[i].name} is not in this round.")
            continue

    return [players, deck]