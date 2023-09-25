from three_dem_tic import ThreeDemBoard

my_list = []
if __name__ == '__main__':
    board = ThreeDemBoard()
    board.get_players()
    flag = True
    while flag:
        board.print_all()
        board.start_game()
        print("Score: ")
        print(f"{board.game_players[0].name}: {board.game_players[0].win_count}")
        print(f"{board.game_players[1].name}: {board.game_players[1].win_count}")
        new_game = input("would you like to play another game(y/n)?")
        while new_game != "y" and new_game != "n":
            new_game = input("please enter 'y' to start new game or 'n' to quit!")
        if new_game == "n":
            print("Goodbye, have a good day..")
            flag = False
        else:
            print("Let's Start Another Game:")

