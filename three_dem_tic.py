from two_dem_tic import TwoDemBoard
from player import Player
import random


class ThreeDemBoard:
    board_list = []
    def __init__(self):
        self.game_players = []
        self.players = []
        for _ in range(3):
            self.board_list.append(TwoDemBoard())
        for i in range(3):
            self.board_list[i].init_board()

    def print_all(self):
        for i in range(3):
            self.board_list[i].print_board(i+1)

    def get_players(self):
        print("Welcome To Tic Tac Toe Game in 3D ! The best game on the planet!")
        for i in range(1, 3):
            player_name = input(f"Enter Player {i}'s name: ")
            player = Player(player_name)
            self.players.append(player)

    def get_game_players(self):
        # Randomly choose the starting player
        chosen_player = random.choice(self.players)
        self.game_players = []
        chosen_player.symbol = "X"
        self.game_players.append(chosen_player)
        # The starting player gets "X"
        if chosen_player == self.players[0]:
            self.players[1].symbol = "O"
            self.game_players.append(self.players[1])
        elif chosen_player == self.players[1]:
            self.players[0].symbol = "O"
            self.game_players.append(self.players[0])

    @staticmethod
    def __get_board_num():
        flag = True
        while flag:
            board_num = input(f"Enter board number (1-3): ")
            if board_num.isdigit():
                board_num = int(board_num)
                if 1 <= board_num <= 3:
                    flag = False
                else:
                    print("Wrong Number, we only have 3 boards!")
            else:
                print("Please enter a number between 1 to 3 to choose a board")
        return board_num

    @staticmethod
    def __get_desired_cell():
        flag = True
        while flag:
            desired_cell = input(f"Enter desired cell number (1-9): ")
            if desired_cell.isdigit():
                desired_cell = int(desired_cell)
                if 1 <= desired_cell <= 9:
                    flag = False
                else:
                    print("Wrong Number, we only have 9 cells!")
            else:
                print("Please enter a number between 1 to 9 to choose a cell")
        return desired_cell

    def move_on_which_board(self, choice):
        board_num = self.__get_board_num()
        if board_num in [1, 2, 3]:
            self.board_list[board_num-1].print_board(board_num)
            choice_on_board = self.__get_desired_cell()
            if not self.board_list[board_num-1].change_value_on_board(choice_on_board, choice):
                self.move_on_which_board(choice)

        self.print_all()

    def check_for_3d_winner(self, winner_player):
        if self.board_list[0].check_for_winner() or self.board_list[1].check_for_winner() or self.board_list[2].check_for_winner():
            print(f"{winner_player.name} is the Winner! ;)")
            winner_player.add_win_count()
            for i in range(3):
                self.board_list[i].init_board()
            return True
        else:
            return False

        ###continue the check of 3d winner..

    def start_game(self):
        self.get_game_players()
        print(
            f"{self.game_players[0].name} you have been chosen to start the game as {self.game_players[0].symbol}!\n"
            f"Please make a move: ")
        while True:
            self.move_on_which_board(self.game_players[0].symbol)
            if self.check_for_3d_winner(self.game_players[0]):
                return
            self.move_on_which_board(self.game_players[1].symbol)
            if self.check_for_3d_winner(self.game_players[1]):
                return

