from inputimeout import inputimeout

from two_dem_tic import TwoDemBoard
from player import Player
import random


class ThreeDemBoard:
    boards_list = []

    def __init__(self):
        self.game_players = []
        self.players = []
        for _ in range(3):
            self.boards_list.append(TwoDemBoard())
        for i in range(3):
            self.boards_list[i].init_board()

    def print_all(self):
        for i in range(3):
            self.boards_list[i].print_board(i + 1)

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
            try:
                desired_cell = inputimeout(prompt=f"Enter desired cell number (1-9): ", timeout=5)
                if desired_cell.isdigit():
                    desired_cell = int(desired_cell)
                    if 1 <= desired_cell <= 9:
                        flag = False
                    else:
                        print("Wrong Number, we only have 9 cells!")
                else:
                    print("Please enter a number between 1 to 9 to choose a cell")
                return desired_cell

            except Exception:
                # Declare the timeout statement
                time_over = 'Your time is over!'
                print(time_over)
    def move_on_which_board(self, choice):
        board_num = self.__get_board_num()
        if board_num in [1, 2, 3]:
            self.boards_list[board_num - 1].print_board(board_num)
            try:
                choice_on_board = self.__get_desired_cell()
                if not self.boards_list[board_num - 1].change_value_on_board(choice_on_board, choice):
                    self.move_on_which_board(choice)
            except Exception:
                # Declare the timeout statement
                time_over = 'Your time is over round 2!'
                print(time_over)

        self.print_all()

    # Inside (Private) function that checks for a 3D Column that includes the same values and type (str), three 'X' or three 'O'.
    # Input: only the self.board_lists that is built in our class
    # returns True,'X' or 'O' if the board cell is equal to the same boards cells in the two other boards.
    def __check_3d_col_winner(self):
        # A for loop that runs on all three boards 0-8 indexes:
        for i in range(9):
            if self.boards_list[0].board_list[i] == self.boards_list[1].board_list[i] == self.boards_list[2].board_list[i] \
                    and isinstance(self.boards_list[0].board_list[i], str):  # <---Check for strings type ONLY 'X' or 'O'-NOT pre-filled integers.
                return True, self.boards_list[0].board_list[i]
        # for loop finished and it did Not find a match for a win
        return (False,)

    # Inside (Private) function that checks for a 3D Diagonal that includes the same values, three 'X' or three 'O'.
    # Input: only the self.board_lists that is built in our class
    # returns True,'X' or 'O' if the indexes 0,4,8  or 2,4,6 on the 3 boards are equal.
    def __check_3d_diagonal_winner(self):
        if (
                self.boards_list[0].board_list[0] == self.boards_list[1].board_list[4] ==
                self.boards_list[2].board_list[8] or
                self.boards_list[0].board_list[2] == self.boards_list[1].board_list[4] ==
                self.boards_list[2].board_list[6] or
                self.boards_list[2].board_list[0] == self.boards_list[1].board_list[4] ==
                self.boards_list[0].board_list[8] or
                self.boards_list[2].board_list[2] == self.boards_list[1].board_list[4] ==
                self.boards_list[0].board_list[6]):
            # return True, if one of the diagonal mathces a win:
            return True, self.boards_list[0].board_list[4]
        else:
            return False,

    def check_for_3d_winner(self, winner_player):
        col_3d_win = self.__check_3d_col_winner()
        diagonal_3d_win = self.__check_3d_diagonal_winner()
        if self.boards_list[0].check_for_winner() or self.boards_list[1].check_for_winner() or self.boards_list[
            2].check_for_winner() \
                or col_3d_win[0] or diagonal_3d_win[0]:
            print(f"{winner_player.name} is the Winner! ;)")
            winner_player.add_win_count()
            for i in range(3):
                self.boards_list[i].init_board()
            return True
        else:
            return False
        # col_3d_win = self.__check_3d_col_winner()
        # diagonal_3d_win = self.__check_3d_diagonal_winner()
        # if col_3d_win[0]:
        #     print(f"we have a Winner. {col_3d_win[1]} Player!")
        #     return True
        # elif diagonal_3d_win[0]:
        #     print(f"we have a Winner. {diagonal_3d_win[1]} Player!")
        #     return True
        # else:
        #     return False
        ###continue the check of 3d winner..

    def start_game(self):
        self.get_game_players()
        print(f"{self.game_players[0].name} you have been chosen to start the game as {self.game_players[0].symbol}!")
        flag = True
        while flag:
            print(f"{self.game_players[0].name} Move:")
            self.move_on_which_board(self.game_players[0].symbol)
            if self.check_for_3d_winner(self.game_players[0]) or self.is_tie():
                flag = False
                return
            print(f"{self.game_players[1].name} Move:")
            self.move_on_which_board(self.game_players[1].symbol)
            if self.check_for_3d_winner(self.game_players[1]) or self.is_tie():
                flag = False
                return

    def is_tie(self):
        if self.boards_list[0].is_board_full() and self.boards_list[1].is_board_full() and self.boards_list[2].is_board_full():
            print("Game Over..")
            print("It's a Tie!")
            for board in self.boards_list:
                board.init_board()
            return True
        return False
