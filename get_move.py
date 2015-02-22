import sys
# get the moves and make them

# Numbers to Alphabet and Alphabet to Numbers
NUM_ALPHA = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}
ALPHA_NUM = dict(zip(NUM_ALPHA.values(),NUM_ALPHA.keys()))


winning_combinations = [
        [1,2,3],[4,5,6],[7,8,9],
        [1,4,7],[2,5,8],[3,6,9],
        [1,5,9],[3,5,7]
        ]



def decode_move(some_string):
    if some_string == 'q':
        sys.exit(0)
    elif some_string.isdigit() and 10 > int(some_string) > 0:
        alpha = NUM_ALPHA.get(some_string)
        return {alpha:'X'}
    else:
        return {}



def check_overlap(Xs_or_Os):
    # Check overlap with winning combinations for Os or Xs
    # return True/False, [overlap]
    all_close_overlaps = []
    if type(Xs_or_Os) != list:
        raise Exception('An error occured!')
    elif len(Xs_or_Os) < 3:
        return False
    else:
        for combination in winning_combinations:
            # Get overlap between X/O values and each combination 
            check_overlap = [x for x in set(combination) if str(x) in set(Xs_or_Os)]
            # If we get an overlap of 3, someone has won!!
            if len(check_overlap) == 3:
                return True 
    return False
    # use to calculate next move, feed into algorithm




