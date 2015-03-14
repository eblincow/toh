# determine which next move is best
from game import decode_move, winning_combinations, check_square_availability
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
        self.Xs = game.get_Xs()
        self.Os = game.get_Os()

        # A dangeorus square for O implies a winning square
        self.winning_square = self.find_winning_square() # final O square
        # A dangerous square for X implies a fatal square
        self.fatal_square = self.find_fatal_square() # fatal X square 
        # fallback if none are final or fatal 
        self.open_square = self.find_open_square() # an open O square 
        # the final output move, e.g. '1'
        self.move = decode_move(self.decide(),"O",game)


    def decide(self):
        if self.winning_square:
            return self.winning_square
        elif self.fatal_square:
            return self.fatal_square
        else:
            return self.open_square


    def update(self):
        self.Xs = self.game.get_Xs()
        self.Os = self.game.get_Os()


    def _find_dangerous_square(self,Xs_or_Os):
        # receives e.g. [1,2] and returns 3
        # finds a dangerous square - e.g. square leading to a win
        for combination in winning_combinations:
            # Get overlap between X/O values and each combination 
            check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
            # If we get an overlap of 2, and the third square isn't occupied
            # theres a dangerous square!!
            if len(check_overlap) == 2:
                # now we should go all the way and find the dangerous square
                # and check if its open, if so return it
                final_square = [x for x in combination if x not in check_overlap][0]
                check = check_square_availability(self.game,final_square)
                if check:
                    return final_square


    def find_winning_square(self):
        winning_square = self._find_dangerous_square(self.Os)
        return winning_square 
    
    def find_fatal_square(self):
        # call find_final_square but with Xs (user's squares) as input
        # finds the squares you need to fill to prevent user from winning
        fatal_square = self._find_dangerous_square(self.Xs)
        return fatal_square 
        

    def find_open_square(self):
        open_square = None
        while not open_square:
            new_try = str(random.randint(0,9))
            open_square = check_square_availability(self.game, new_try)
        # optimize later to check for 'two open' because otherwise dumb
        return new_try






