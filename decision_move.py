
# determine which next move is best
from get_move import winning_combinations

def generate_move(game):
   find_almost_matches(game.Xs)


def find_almost_matches(Xs_or_Os):
    almost_matches= [] 
    
    for combination in winning_combinations:
        # Get overlap between X/O values and each combination 
        check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
        # If we get an overlap of 2, theres a dangerous square!!
        if len(check_overlap) == 2:
            almost_matches.append(check_overlap)
    print("Almost matches = " + repr(almost_matches))
    return almost_matches


def find_dangerous_squares(almost_matches):
    # receives [1,2] and outputs 3
    pass






