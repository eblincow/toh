#!/usr/bin/env python

# main game file with core while loop

import sys, os
from game import Game, decode_move # remembers game state
from getch import getch # used for immediate keyboard input(no enter key)
from decision import Decision

COMPUTER_START = False



def main():
    global COMPUTER_START
    # COMPUTER_START alternates True/False with each new game 
    COMPUTER_START = not COMPUTER_START

    game = Game() # Basically just a container for the game state vars
    os.system('clear')
    game.print_board()

    # Main loop 
    while game.WIN_STATE == False:
        if COMPUTER_START:
            print("Xs move")
            Xs_move(game)
            game.print_board()
            print("Os move")
            Os_move(game)
            game.print_board()
        elif not COMPUTER_START:
            Os_move(game)
            game.print_board()
            Xs_move(game)
            game.print_board()
        # no open spaces, game is finished
        if (list(game.BOARD_STATE.values()).count('_') <= 1):
            print("Its a draw!")
            break

    if game.WINNER:
        print("{winner} won!".format(winner=game.WINNER))
    another_game = input("Play again? y/n")
    if another_game in ('n','q'):
        sys.exit(0) # quit
    else:
        main() # play again


def Xs_move(game):
    # get the Xs move
    # move = decode_move(getch(),"X", game)
    # temporary !
    move = decode_move(input(),"X",game)
    if move:
        game.BOARD_STATE.update(move)
    else:
        Xs_move(game)
    # get Xs
    game.did_anyone_win()  

def Os_move(game):
    # get the Os move
    our_move = Decision(game).move

    print("Our move = " + repr(our_move))
    game.BOARD_STATE.update(our_move)
    # sleep?
    #print_board(game.BOARD_STATE)        
    game.did_anyone_win()



if __name__ == '__main__':
    main()

