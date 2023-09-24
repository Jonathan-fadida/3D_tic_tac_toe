print("Welcome To Tic Tac Toe Game in 3D ! The best game on the planet!")

import random


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

def my_num(mm):
    return mm*2

class TicTacToe3D:
    def __init__(self):
        self.game_players = []

    def get_game_players(self):
        players = []
        player1_name = input("Enter Player 1's name: ")
        player1 = Player(player1_name, "")
        players.append(player1)
        player2_name = input("Enter Player 2's name: ")
        player2 = Player(player2_name, "")
        players.append(player2)
    
        # Randomly choose the starting player
        chosen_player = random.choice(players) 
        self.game_players = []
        chosen_player.symbol = "X"
        self.game_players.append(chosen_player)
        # The starting player gets "X"
        if chosen_player == players[0]:
            player2.symbol = "O"
            self.game_players.append(player2)
        elif chosen_player == players[1]:
            player1.symbol = "O"
            self.game_players.append(player1)
        

    def start_game(self):
        print(f"{self.game_players[0].name} you have been chosen to start the game as {self.game_players[0].symbol} ! Please make a move: ")
        print(self.game_players[1].name , self.game_players[1].symbol)
        
if __name__ == "__main__":
    game = TicTacToe3D()
    game.get_game_players()
    game.start_game()
