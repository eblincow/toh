# main game file with core while loop

import sys, os
from board import print_board # prints board
from get_move import decode_move # gets move, analyzes board
from game import Game # remembers game state
from getch import getch # used for immediate keyboard input(no enter key)
from decision_move import generate_move
import datetime

COMPUTER_START = False



def main():
    global COMPUTER_START
    # COMPUTER_START alternates True/False with each new game 
    COMPUTER_START = not COMPUTER_START 
    
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
    


def Xs_move(game):
    # get the Xs move
    move = decode_move(getch())
    game.BOARD_STATE.update(move)
    print_board(game.BOARD_STATE)
    # get Xs
    xs_list = game.get_Xs() 
    game.did_anyone_win(xs_list)
  

def Os_move(game):
    # get the Os move
    #our_move = generate_move(game.BOARD_STATE.copy())
    our_move = generate_move(game)
    
    #BOARD_STATE.update(our_move)
    # sleep?
    #print_board(game.BOARD_STATE)        
    os_list = game.get_Os() 
    game.did_anyone_win(os_list)





if __name__ == '__main__':
    main()

