from get_move import check_overlap


class Game():
    def __init__(self, COMPUTER_START=True):
        self.WIN_STATE = False
        self.X_WIN_STATE = False
        self.O_WIN_STATE = False
        self.WINNER = None
        self.BOARD_STATE = {} 
        self.x_overlap = []
        self.o_overlap = []

    def check_win(self,Xs=[],Os=[]):
        self.X_WIN_STATE, self.x_overlap     = check_overlap(Xs)
        self.O_WIN_STATE, self.o_overlap     = check_overlap(Os)
        self.WIN_STATE                       = self.O_WIN_STATE or self.X_WIN_STATE

        if self.O_WIN_STATE:
            self.WINNER = 'The machine'
        elif self.X_WIN_STATE:
            self.WINNER = 'You'






