
from board import *
from decision import *
from game import *
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

    def test_Xs_and_Os(self):

        # test the functions Xs and Os
        game1 = Game()
        game1.BOARD_STATE = start
        self.assertEqual(set(game1.get_Xs()),set(['1','3']))
        self.assertEqual(set(game1.get_Os()),set(['2']))

        game2 = Game()
        game2.BOARD_STATE = Xwin
        self.assertEqual(set(game2.get_Xs()),set(['1','2','3']))

        game3 = Game()
        game3.BOARD_STATE = Owin
        self.assertEqual(game3.get_Xs(),[])
        self.assertEqual(set(game3.get_Os()),set(['1','2','3']))

        game4 = Game()
        game4.BOARD_STATE = complex1
        self.assertEqual(set(game4.get_Xs()),set(['1','2','5']))
        self.assertEqual(set(game4.get_Os()),set(['3','4']))



    def test_check_overlap(self):
        non_winning_combinations = [['1','2','5'],['1','3','9'],['1','1','1'],['0','22','33'],['-1','-2','3'],['4','5'],['5','6','1']]
        winning_combinations = [['1','2','3'],['1','5','9'],['8','5','2']]
        for non_winner in non_winning_combinations:
            self.assertFalse(check_overlap(non_winner), "check_overlap should return False for non winners")
            
        for winner in winning_combinations:
            self.assertTrue(check_overlap(winner))
            self.assertTrue(type(check_overlap(winner)==list))


    def test_check_win(self):
        pass

    def test_find_almost_matches(self):
        #self.assertEqual(find_almost_matches(['1','2']),[[1,2]])
        #self.assertEqual(find_almost_matches(['1']),[])
        pass





if __name__ == '__main__':
    unittest.main()
