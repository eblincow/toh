import sys
# get the moves and make them

ALPHANUMERIC_TRANSLATION = {'1':'a','2':'b','3':'c','4':'d','5':'e','6':'f','7':'g','8':'h','9':'i'}


def decode_move(some_string):
    if some_string == 'q':
        sys.exit(0)
    elif some_string.isdigit() and 10 > int(some_string) > 0:
        alpha = ALPHANUMERIC_TRANSLATION.get(some_string)
        return {alpha:'X'}
    else:
        return {}
