import sys
from board import BOARD, PROMPT

# Numbers to Alphabet and Alphabet to Numbers
NUM_ALPHA = {'1': 'a', '2': 'b', '3': 'c', '4': 'd', '5': 'e', '6': 'f', '7': 'g', '8': 'h', '9': 'i'}
ALPHA_NUM = dict(zip(NUM_ALPHA.values(), NUM_ALPHA.keys()))

BOARD_START = {'a': '_', 'b': '_', 'c': '_', 'd': '_', 'e': '_', 'f': '_', 'g': '_', 'h': '_', 'i': '_'}

winning_combinations = [
    ['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
    ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
    ['1', '5', '9'], ['3', '5', '7']
]


def check_square_availability(game, square):
    # receive '1' check available, return True/False
    convert = NUM_ALPHA.get(square)
    if game.BOARD_STATE.get(convert) == "_":
        return True  # Its open!
    else:
        return False


def check_winning(Xs_or_Os):
    # Check overlap with winning combinations for Os or Xs
    # return True if its a winning combination
    if len(Xs_or_Os) < 3:
        return False
    else:
        for combination in winning_combinations:
            # Get overlap between X/O values and each combination
            check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
            # If we get an overlap of 3, someone has won!!
            if len(check_overlap) == 3:
                return True
    return False


def decode_move(some_string, X_or_O, game):
    # Convert '1' to {'a':'X'} or {'a':'O'} to update BOARD_STATE 
    if some_string == 'q':
        sys.exit(0)
    elif some_string.isdigit() and 10 > int(some_string) > 0:
        availability = check_square_availability(game, some_string)
        if availability:
            alpha = NUM_ALPHA.get(some_string)
            return {alpha: X_or_O}
    else:
        return {}


class Game():
    def __init__(self):
        self.WIN_STATE = False
        self.X_WIN_STATE = False
        self.O_WIN_STATE = False
        self.WINNER = None
        self.BOARD_STATE = BOARD_START.copy()


    def print_board(self):
        # os.system('clear')
        board = BOARD.format(**self.BOARD_STATE)
        print(board)
        print(PROMPT)
        return board


    def did_anyone_win(self, X_or_O):
        if X_or_O == "X":
            self.X_WIN_STATE = check_winning(self.get_Xs())

        if X_or_O == "O":
            self.O_WIN_STATE = check_winning(self.get_Os())

        self.WIN_STATE = self.O_WIN_STATE or self.X_WIN_STATE

        if self.O_WIN_STATE:
            self.WINNER = 'The machine'
            self.WIN_STATE = True
        elif self.X_WIN_STATE:
            self.WINNER = 'You'
            self.WIN_STATE = True
        return self.WIN_STATE


    def get_Xs(self):
        # Get list of X values: '1','2'
        Xs = []
        for key, value in self.BOARD_STATE.items():  # e.g. 'a','X'
            if value == 'X':
                Xs.append(ALPHA_NUM[key])  # e.g. '1'
        return Xs


    def get_Os(self):
        # Get list of O values: '1','2'
        Os = []
        for key, value in self.BOARD_STATE.items():
            if value == 'O':
                Os.append(ALPHA_NUM[key])
        return Os





