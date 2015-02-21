import sys
# get the moves and make them

# Numbers to Alphabet and Alphabet to Numbers
NUM_ALPHA = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
ALPHA_NUM = dict(zip(NUM_ALPHA.values(),NUM_ALPHA.keys()))

def decode_move(some_string):
    if some_string == 'q':
        sys.exit(0)
    elif some_string.isdigit() and 10 > int(some_string) > 0:
        alpha = NUM_ALPHA.get(some_string)
        return {alpha:'X'}
    else:
        return {}


def check_win(board_state):
    if not board_state or type(board_state) != dict:
        return False
    elif list(board_state.values()).count('X') > 2:
        return False

def decode_board_state(board_state):
    Xs = []
    Os = []
    for key,value in board_state.items(): #e.g. 'a','X'
        if value=='X':
            Xs.append(ALPHA_NUM[key]) # e.g. '1'
        if value=='O':
            Os.append(ALPHA_NUM[key])
    return [Xs,Os]
