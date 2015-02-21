
from board import print_board
from get_move import decode_move
# while loop with raw_input and main logic


BOARD_STATE = {}

WIN_STATE = False

print_board()

while WIN_STATE == False:
    move = decode_move(raw_input())
    BOARD_STATE.update(move)
    print_board(BOARD_STATE) 

