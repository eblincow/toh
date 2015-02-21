
from board import print_board
from get_move import decode_move, decode_board_state, check_win
# while loop with raw_input and main logic


COMPUTER_START = False

BOARD_STATE = {}

WIN_STATE = False
X_WIN_STATE = False
O_WIN_STATE = False

print_board()

while WIN_STATE == False:
    move = decode_move(raw_input())
    BOARD_STATE.update(move)
    print_board(BOARD_STATE) 
    #our_move = generate_move(BOARD_STATE.copy())
    #BOARD_STATE.update(our_move)
    
    decoded_board_state = decode_board_state(BOARD_STATE) 
    print("decoded_board_state = " + repr(decoded_board_state))
    X_WIN_STATE, overlap = check_win(decoded_board_state[0]) 
    O_WIN_STATE, overlap = check_win(decoded_board_state[1])
    print("X_WIN_STATE: " + repr(X_WIN_STATE))
    print("O_WIN_STATE: " + repr(O_WIN_STATE))
    WIN_STATE = X_WIN_STATE or O_WIN_STATE
