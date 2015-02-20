import os

INTRO = "Welcome to toh \n an unbeatable tic-tac-toh game.\n"

FIRST = "Press a number 1 to 9 to select the square of your choice.\n"

BOARD = """\n\nTIC_TAC_TOE\n\n

     _{a}_   _{b}_   _{c}_                    | 1 2 3 |\
     \n                                        | 4 5 6 |  
     _{d}_   _{e}_   _{f}_                    | 7 8 9 |\
         \n                                 
     _{g}_   _{h}_   _{i}_                    X = You, O = Machine 
     
     \n\n             """


DEFAULT_LAYOUT = { 'a': '_', 'b':'_', 'c':'_', 'd':'_', 'e':'_', 'f':'_', 'g':'_', 'h':'_', 'i':'_' }

# clear the terminal somehow
#os.clear()



def print_board(board_dict=DEFAULT_LAYOUT):
    os.system('clear')
    print(BOARD.format(**board_dict))


print_board()

print_board()


