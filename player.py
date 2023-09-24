class Player:
    def __init__(self, name, symbol=""):
        self.name = name
        self.symbol = symbol
        self.win_count = 0

    def add_win_count(self):
        self.win_count += 1


