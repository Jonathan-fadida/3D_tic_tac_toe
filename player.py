print("Welcome To Tic Tac Toe Game in 3D ! The best game on the planet!")

import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class TicTacToe3D:
    def __init__(self):
        self.players = []
        self.current_player = None

    def get_player_names(self):
        self.players.append(Player(input("Enter Player 1's name: "), ""))
        self.players.append(Player(input("Enter Player 2's name: "), ""))
        # Randomly choose the starting player
        self.current_player = random.choice(self.players)  
        # The starting player gets "X"
        self.current_player.symbol = "X"  
        

    def start_game(self):
        print(f"{self.current_player.name} you have been chosen to start the game as {self.current_player.symbol} ! Please make a move: ")

if __name__ == "__main__":
    game = TicTacToe3D()
    game.get_player_names()
    game.start_game()
