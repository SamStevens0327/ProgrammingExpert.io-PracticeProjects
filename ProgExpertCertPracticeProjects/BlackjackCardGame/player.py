import deck
class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.wallet = 100000
        self.stash = 0
        self.bet = 0
        self.status = None
