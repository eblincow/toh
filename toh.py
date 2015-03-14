#!/usr/bin/env python

# main game file with core while loop

import sys, os
from game import Game, decode_move # remembers game state
from getch import getch # used for immediate keyboard input(no enter key)
from decision import Decision
import time


COMPUTER_START = True

def main():
    global COMPUTER_START
    # COMPUTER_START alternates True/False with each new game 
    COMPUTER_START = not COMPUTER_START

    game = Game() # game state vars and methods
    os.system('clear')
    game.print_board()

    # Main loop 
    while game.WIN_STATE == False:
        # User begins
        if not COMPUTER_START:
            Xs_move(game)
            game.print_board()
            if not game.WIN_STATE:
                Os_move(game)
                game.print_board()
        # Computer begins
        elif COMPUTER_START:
            Os_move(game)
            game.print_board()
            if not game.WIN_STATE:
                Xs_move(game)
                game.print_board()

        # no open spaces, game is finished
        if (list(game.BOARD_STATE.values()).count('_') == 0):
            print("Its a draw!")
            break

    # Check if somebody won
    if game.WINNER:
        print("{winner} won!".format(winner=game.WINNER))
    another_game = input("Play again? y/n\n")
    if another_game=='n' or another_game=='q':
        sys.exit(0) # quit
    else:
        main() # play again


def Xs_move(game):
    # get the Xs move
    # move = decode_move(getch(),"X", game)
    # temporary !
    move = decode_move(getch(),"X",game)
    if move:
        game.BOARD_STATE.update(move)
    else:
        Xs_move(game)
    # get Xs
    decision = Decision(game)
    if len(decision.Xs) > 2:
        game.did_anyone_win("X")

def Os_move(game):
    # get the Os move
    decision = Decision(game)
    our_move = decision.move
    game.BOARD_STATE.update(our_move)
    time.sleep(0.25)
    decision.update() # refresh X and Os after move
    if len(decision.Os) > 2:
        game.did_anyone_win("O")



if __name__ == '__main__':
    main()

