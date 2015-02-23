from get_move import check_overlap, ALPHA_NUM, winning_combinations

class Game():
    def __init__(self):
        self.WIN_STATE = False
        self.X_WIN_STATE = False
        self.O_WIN_STATE = False
        self.WINNER = None
        self.BOARD_STATE = {} 
        self.Xs = []
        self.Os = []

    def did_anyone_win(self,Xs=[],Os=[]):
        self.X_WIN_STATE    = check_winning(Xs)
        self.O_WIN_STATE    = check_winning(Os)
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







def check_winning(Xs_or_Os):
    # Check overlap with winning combinations for Os or Xs
    # return True if its a winning combination
    if type(Xs_or_Os) != list:
        raise Exception('An error occured!')
    elif len(Xs_or_Os) < 3:
        return False
    else:
        for combination in winning_combinations:
            # Get overlap between X/O values and each combination 
            check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
            # If we get an overlap of 3, someone has won!!
            if len(check_overlap) == 3:
                return True 
    return False


