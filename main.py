from three_dem_tic import ThreeDemBoard
#from player import Player

my_list = []
if __name__ == '__main__':
    board = ThreeDemBoard()
    board.init_board()
    board.print_board()
    print(board.change_value_on_board(3, "X"))
    board.print_board()
