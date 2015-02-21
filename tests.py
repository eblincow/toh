
from board import *
from get_move import *
import unittest


start = {'a':'X','b':'O','c':'X'}
Xwin = {'a':'X','b':'X','c':'X'}
Owin = {'a':'O','b':'O','c':'O'}
complex1 = {'a':'X','b':'X','c':'O','d':'O','e':'X'}



class TestBoard(unittest.TestCase):

    def setUp(self):
        pass
                        
    def test_print_board(self):
        self.assertEqual(print_board(),{'c': '_', 'b': '_', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': '_', 'h': '_'})
        self.assertEqual(print_board(start),{'c': 'X', 'b': 'O', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': 'X', 'h': '_'})
        self.assertEqual(print_board(Xwin),{'c': 'X', 'b': 'X', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': 'X', 'h': '_'})
        self.assertEqual(print_board(Owin),{'c': 'O', 'b': 'O', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': 'O', 'h': '_'})


    def test_decode_move(self):
        self.assertEqual(decode_move("1"),{'a':'X'})
        self.assertEqual(decode_move("5"),{'e':'X'})
        self.assertEqual(decode_move("9"),{'i':'X'})
        self.assertEqual(decode_move("text"),{})
        self.assertEqual(decode_move("15"),{})

    def test_decode_board_state(self):
        # returns Xs, Os
        self.assertEqual(decode_board_state(start)[0],['1','3'])
        self.assertEqual(decode_board_state(start)[1],['2'])

        self.assertEqual(set(decode_board_state(Xwin)[0]),set(['1','2','3']))
        self.assertEqual(decode_board_state(Xwin)[1],[])

        self.assertEqual(set(decode_board_state(Owin)[0]),set([]))
        self.assertEqual(set(decode_board_state(Owin)[1]),set(['1','2','3']))

        self.assertEqual(set(decode_board_state(complex1)[0]),set(['1','2','5']))
        self.assertEqual(set(decode_board_state(complex1)[1]),set(['3','4']))



    def test_check_overlap(self):
        non_winning_combinations = [['1','2','5'],['1','3','9'],['1','1','1'],['0','22','33'],['-1','-2','3'],['4','5'],['5','6','1']]
        winning_combinations = [['1','2','3'],['1','5','9'],['8','5','2']]
        for non_winner in non_winning_combinations:
            self.assertFalse(check_overlap(non_winner)[0], "check_overlap should return False for non winners")
            self.assertTrue(type(check_overlap(non_winner)[1]==list),"check_overlap should return list of overlap as second item")
            
        self.assertTrue(len(check_overlap(['1','2','5'])[1])>0,"the returned list shouldnt be empty")

        for winner in winning_combinations:
            self.assertTrue(check_overlap(winner)[0])
            self.assertTrue(type(check_overlap(winner)[1]==list))
            self.assertTrue(len(check_overlap(winner)[1])==3,"winning check_overlaps should have 3 digits")


    def test_check_win(self):
        pass









if __name__ == '__main__':
    unittest.main()
