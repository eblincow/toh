import os

PROMPT = "\nEnter a square: "

BOARD = """\n\n        TIC_TAC_TOE\n\n

     _{a}_   _{b}_   _{c}_                    | 1 2 3 |\
     \n                                        | 4 5 6 |  
     _{d}_   _{e}_   _{f}_                    | 7 8 9 |\
         \n                                 
     _{g}_   _{h}_   _{i}_                    X = You\
\n                                        O = Machine 
     
     \n\n             """


DEFAULT_LAYOUT = { 'a': '_', 'b':'_', 'c':'_', 'd':'_', 'e':'_', 'f':'_', 'g':'_', 'h':'_', 'i':'_' }

def print_board(board_dict=DEFAULT_LAYOUT.copy()):
    new_board = DEFAULT_LAYOUT.copy()
    new_board.update(board_dict)
    os.system('clear')
    board = BOARD.format(**new_board)
    print(board)
    print(PROMPT)
    return new_board





