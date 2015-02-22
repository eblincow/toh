from get_move import check_overlap, ALPHA_NUM

class Game():
    def __init__(self):
        self.WIN_STATE = False
        self.X_WIN_STATE = False
        self.O_WIN_STATE = False
        self.WINNER = None
        self.BOARD_STATE = {} 
        self.Xs = []
        self.Os = []

    def check_win(self,Xs=[],Os=[]):
        self.X_WIN_STATE    = check_overlap(Xs)
        self.O_WIN_STATE    = check_overlap(Os)
        self.WIN_STATE      = self.O_WIN_STATE or self.X_WIN_STATE

        if self.O_WIN_STATE:
            self.WINNER = 'The machine'
        elif self.X_WIN_STATE:
            self.WINNER = 'You'


    def get_Xs(self):
        # Get list of X values: '1','2'
        for key,value in self.BOARD_STATE.items(): #e.g. 'a','X'
            if value=='X':
                self.Xs.append(ALPHA_NUM[key]) # e.g. '1'
        return self.Xs


    def get_Os(self):
        # Get list of O values: '1','2'
        for key, value in self.BOARD_STATE.items():
            if value=='O':
                self.Os.append(ALPHA_NUM[key])
        return self.Os




