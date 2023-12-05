import game
import deck

request = game.start_game()
if request == False:
    game.quit_program()
else:
    players = game.invite_players()     # players sit at table

    players = game.buy_sell_chips(players)      # players buy a stash

    print("Let's play!")

    buy_in = 50
    players = game.buy_in(buy_in, players)      # players put money on the table

    # table is a list of [players, current deck]
    table = [players, deck.cards]

    table = game.deal(table[0], table[1])      # players get first hand

    table = game.bet_round(table[0], table[1])      # players bet on first hand

    table = game.play_round(table[0], table[1])     # hit or stick

    table = game.bet_round(table[0], table[1])






