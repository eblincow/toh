# main game file with core while loop

import sys, os
from board import print_board # prints board
from get_move import decode_move, Xs,Os # gets move, analyzes board
from game import Game # remembers game state
from getch import getch # used for immediate keyboard input(no enter key)
import datetime

COMPUTER_START = True


def main():
     
    game = Game() # Basically just a container for the game state vars
    os.system('clear')

    # Main loop 
    while game.WIN_STATE == False:
        print_board(game.BOARD_STATE) 
        
        if COMPUTER_START:
            Xs_move(game)
            Os_move(game)        
        elif not COMPUTER_START:
            Os_move(game)
            Xs_move(game)
        
    
    
    
    
    print(game.WINNER + " won!")
    print("Do you want to play again? y/n\n")
    char = getch() 
    if char.lower()=='y':
        main()
    elif char.lower()=='n':
        sys.exit(0)





def Xs_move(game):
    move = decode_move(getch())
    game.BOARD_STATE.update(move)
    print_board(game.BOARD_STATE)
    # get Xs
    xs_list = Xs(game.BOARD_STATE) 
    game.check_win(xs_list)
  

def Os_move(game):
    #our_move = generate_move(game.BOARD_STATE.copy())
    #BOARD_STATE.update(our_move)
    # sleep?
    print_board(game.BOARD_STATE)        
    os_list = Os(game.BOARD_STATE) 
    print("Os just went! (cant show it yet)!" + str(datetime.datetime.now().microsecond))




main()







