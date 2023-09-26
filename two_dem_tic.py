class TwoDemBoard:
    def __init__(self):
        self.board_list = []

    def init_board(self):
        self.board_list = []
        for i in range(1, 10):
            self.board_list.append(i)

    # a function that print the 2d board
    # prints out self.board_list in an ordered way
    # does not return anything
    def print_board(self,board_num):
        my_str = (f'''
                     Board {board_num}:
                    
                     {self.board_list[0]} | {self.board_list[1]} | {self.board_list[2]} 
                    -----------
                     {self.board_list[3]} | {self.board_list[4]} | {self.board_list[5]}
                    -----------
                     {self.board_list[6]} | {self.board_list[7]} | {self.board_list[8]} 
                ''')
        print(my_str)

    # a function that checks the player_index and player_choice correctness
    # Input: player_index: int, player_choice: str
    # returns True if player_index is between 1 and 9 and player_choice is 'X' or 'O', else false
    def __is_move_valid(self, player_index, player_choice):
        if type(player_index) != int:
            print("Wrong type value, must be a number between 1 and 9")
            return False
        if player_index < 1 or player_index > 9:
            print("Wrong int value on board, must be between 1 and 9")
            return False
        elif type(self.board_list[player_index-1]) != int:
            print(f"This place is Already Chosen, '{self.board_list[player_index-1]}'. please choose another place")
            return False
        elif player_choice != "X" and player_choice != "O":
            print("Wrong user choice")
            return False
        # good choice, we can move on to change the corresponding index
        return True

    # a function that changes the value to 'X' or 'O' for a valid user choice (between 1 and 9)
    # Input: player_index: int, player_choice: str
    # returns True if successfully changed and False for failure to make the user choose again
    def change_value_on_board(self, player_index, player_choice):
        if self.__is_move_valid(player_index, player_choice):
            self.board_list[player_index-1] = player_choice
            return True
        else:
            return False

    # a function the checks if there is a winner in the whole board
    # no input need, only calls the Private functions to check all the rows, columns and diagonals.
    # print's out the shape of the winner ('X' or 'O' Player) and returns true to finish the game,
    # otherwise returns False and the game must continue..!
    def check_for_winner(self):
        row_win = self.__check_row_winner()
        col_win = self.__check_col_winner()
        diagonal_win = self.__check_diagonal_winner()
        if row_win[0]:
            print(f"we have a Winner. {row_win[1]} Player!")
            return True
        elif col_win[0]:
            print(f"we have a Winner. {col_win[1]} Player!")
            return True
        elif diagonal_win[0]:
            print(f"we have a Winner. {diagonal_win[1]} Player!")
            return True
        else:
            return False

    # Inside (Private) function that checks for a Row that includes the same values, three 'X' or three 'O'.
    # Input: only the self.board_list that is built in our class
    # returns True,'X' or 'O' if the indexes 0,1,2 (1st row) or 3,4,5 (2nd row) or 6,7,8 (3rd row) is the same value
    def __check_row_winner(self):
        my_list = self.board_list
        for i in range(0, len(my_list), 3):
            if my_list[i] == my_list[i+1] and my_list[i] == my_list[i+2]:
                return True, my_list[i]
        # for loop finished and it did Not find a match
        return False, None

    # Inside (Private) function that checks for a Column that includes the same values, three 'X' or three 'O'.
    # Input: only the self.board_list that is built in our class
    # returns True,'X' or 'O' if the indexes 0,1,2 (1st column) or 3,4,5 (2nd col) or 6,7,8 (3rd col) is the same value
    def __check_col_winner(self):
        my_list = self.board_list
        for i in range(3):
            # check if there is a column that are equals: my_list[i] == my_list[i + 3] == my_list[i + 6]
            if my_list[i] == my_list[i + 3] and my_list[i] == my_list[i + 6]:
                return True, my_list[i]
        # for loop finished and it did Not find a match
        return (False,)

    # Inside (Private) function that checks for a Diagonal that includes the same values, three 'X' or three 'O'.
    # Input: only the self.board_list that is built in our class
    # returns True,'X' or 'O' if the indexes 0,4,8 (1st diagonal) or 2,4,6 (2nd diagonal) is the same value
    def __check_diagonal_winner(self):
        my_list = self.board_list
        if my_list[0] == my_list[4] == my_list[8] or my_list[2] == my_list[4] == my_list[6]:
            # my_list[4] should match if there is one of the diagonal matches
            return True, my_list[4]
        else:
            return (False, )

    # <<<<<<<<<<<<<<<<<<<<<<<<<<< Need to add counter after every turn >>>>>>>>>>>>>>>>>>>>>>>>>>>>

    def is_board_full(self):
        my_list = self.board_list

        for cell in my_list:
            if type(cell) == int:
                return False

        return True

# if __name__ == "__main__":
#     board = TwoDemBoard()
#     board.init_board()
#     board.change_value_on_board(1,"X")
#     board.change_value_on_board(2, "X")
#     board.change_value_on_board(3, "O")
#     board.change_value_on_board(4, "O")
#     board.change_value_on_board(5, "X")
#     board.change_value_on_board(6, "X")
#     #board.change_value_on_board(7, "X")
#     board.change_value_on_board(8, "O")
#     board.change_value_on_board(9, "O")
#     print(board.is_board_full())