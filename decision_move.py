
# determine which next move is best
from get_move import winning_combinations



class Decision():
    
    def __init__(self, game):
        self.game = game
        self.X_almost_matches = find_almost_matches(game.get_Xs) 
        self.O_almost_matches = find_almost_matches(game.get_Os) 
        self.fatal_square = find_fatal_square() # fatal X square 
        self.final_square = find_final_square() # final O square
        self.open_square = find_open_square() # an open O square 
        self.decision = decide()

    def generate_move(self):
        # block Xs move  
        find_almost_matches(game.Xs)


    def find_almost_matches(self,Xs_or_Os):
        almost_matches= [] 
        
        for combination in winning_combinations:
            # Get overlap between X/O values and each combination 
            check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
            # If we get an overlap of 2, theres a dangerous square!!
            if len(check_overlap) == 2:
                almost_matches.append(check_overlap)
        print("Almost matches = " + repr(almost_matches))
        return almost_matches


    def find_fatal_square(self,almost_matches):
        # receives [1,2] and outputs 3
        pass






