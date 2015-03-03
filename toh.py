#!/usr/bin/env python

# main game file with core while loop

import sys, os
from game import Game, decode_move # remembers game state
from getch import getch # used for immediate keyboard input(no enter key)
from decision import Decision
import time


COMPUTER_START = True

# TEMPORARY REMOVE ME JUST DEBUGGING
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
        if not COMPUTER_START:
            Xs_move(game)
            game.print_board()
            if not game.WIN_STATE:
                Os_move(game)
                game.print_board()
        elif COMPUTER_START:
            Os_move(game)
            game.print_board()
            #### BUG BUG BUG ####
            ### when Os_move wins, it declares game.WIN_STATE
            # but that doesnt get checked until the next run of this while loop
            # so we get another move by Xs_move
            if not game.WIN_STATE:
                Xs_move(game)
                game.print_board()
        # no open spaces, game is finished
        if (list(game.BOARD_STATE.values()).count('_') == 0):
            print("Its a draw!")
            break

    if game.WINNER:
        print("{winner} won!".format(winner=game.WINNER))
    another_game = input("Play again? y/n\n")
    if another_game in ('n','q'):
        sys.exit(0) # quit
    else:
        main() # play again


def Xs_move(game):
    # get the Xs move
    # True = somebody won
    # False = nobody won
    # move = decode_move(getch(),"X", game)
    # temporary !
    move = decode_move(input(),"X",game)
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
    # True = somebody won
    decision = Decision(game)
    our_move = decision.move

    print("Our move = " + repr(our_move))
    game.BOARD_STATE.update(our_move)
    # sleep?
    time.sleep(1)
    decision.update() # refresh X and Os after move
    if len(decision.Os) > 2:
        print(decision.Os)
        game.did_anyone_win("O")



if __name__ == '__main__':
    main()

