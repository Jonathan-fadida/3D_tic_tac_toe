class TwoDemBoard:
    def __init__(self):
        self.board_list = []
    def init_board(self):

        for i in range(1,10):
            self.board_list.append(i)

    def print_board(self):
        my_str=(f'''
                     {self.board_list[0]} | {self.board_list[1]} | {self.board_list[2]} 
                    -----------
                     {self.board_list[3]} | {self.board_list[4]} | {self.board_list[5]}
                    -----------
                     {self.board_list[6]} | {self.board_list[7]} | {self.board_list[8]} 
                ''')
        print(my_str)