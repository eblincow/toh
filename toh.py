
from board import print_board
from get_move import decode_move, check_win, decode_board_state
# while loop with raw_input and main logic


COMPUTER_START = False

BOARD_STATE = {}

WIN_STATE = False

print_board()

while WIN_STATE == False:
    move = decode_move(raw_input())
    BOARD_STATE.update(move)
    print_board(BOARD_STATE) 
    #our_move = generate_move(BOARD_STATE.copy())
    #BOARD_STATE.update(our_move)
    print_board(BOARD_STATE)
    print(decode_board_state(BOARD_STATE))
    #WIN_STATE = check_win(BOARD_STATE)
    
