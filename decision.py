# determine which next move is best
from game import decode_move, winning_combinations, NUM_ALPHA

import random



# winning
# fatal
# open
# random

# winning move - you win
# fatal move - you prevent yourself from losing, prevent a fatal move
# open - find an open square, where a row is possible
# random - random 


class Decision():
    
    def __init__(self, game):
        self.game = game
        self.X_almost_matches = self._find_almost_matches(game.get_Xs()) 
        self.O_almost_matches = self._find_almost_matches(game.get_Os()) 
        
        #An almost match on O implies a final square 
        self.winning_square = self.find_winning_square() # final O square
        #An almost match on X implies a fatal square 
        self.fatal_square = self.find_fatal_square() # fatal X square 
        # fallback if none are final or fatal 
        self.open_square = self.find_open_square() # an open O square 
        # the final output move, e.g. '1'
        self.move = decode_move(self.decide(),"O")

    def decide(self):
        if self.winning_square:
            return self.winning_square
        elif self.fatal_square:
            return self.fatal_square
        else:
            return self.open_square


    def check_square_availability(self,square):
        convert = NUM_ALPHA.get(square)  
        if self.game.BOARD_STATE.get(convert) == "_":
            return True # Its open!
        else:
            return False
    
    
    def _find_almost_matches(self,Xs_or_Os):
        almost_matches= [] 
        
        for combination in winning_combinations:
            # Get overlap between X/O values and each combination 
            check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
            # If we get an overlap of 2, theres a dangerous square!!
            if len(check_overlap) == 2:
                almost_matches.append(check_overlap)
        print("Almost matches = " + repr(almost_matches))
        return almost_matches


    def _find_final_square(self, almost_matches):
        # This function returns the final square necessary for a row of three


        final_square = None
        final_squares = []

        for almost_match in almost_matches:

            for combination in winning_combinations:
                # find the combination which it overlaps
                if len(set(combination).intersection(almost_match))==2:
                    combo = combination[:] # make a copy of combination
                    for square in almost_match:
                       combo.remove(square) # find the last unselected square 
                    final_squares.append(combo[0]) 
        print(repr(final_squares)) 
        for final in final_squares:
            if self.check_square_availability(final):
                final_square = final
        print("Final square seems to be = " + repr(final_square))
        return final_square


    def find_winning_square(self):
        winning_square = self._find_final_square(almost_matches=self.O_almost_matches)
        return winning_square 
    
    def find_fatal_square(self):
        # call find_final_square but with Xs (user's squares) as input
        # finds the squares you need to fill to prevent user from winning
        fatal_square = self._find_final_square(almost_matches=self.X_almost_matches) 
        return fatal_square 
        
        

    def find_open_square(self):
        return '1'







