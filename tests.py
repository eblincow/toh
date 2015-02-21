
from board import *
import unittest


start = {'a':'X','b':'O','c':'X'}
Xwin = {'a':'X','b':'X','c':'X'}
Owin = {'a':'O','b':'O','c':'O'}



class TestBoard(unittest.TestCase):

    def setUp(self):
        pass
                        
    def test_print_board(self):
        self.assertEqual(print_board(),{'c': '_', 'b': '_', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': '_', 'h': '_'})
        self.assertEqual(print_board(start),{'c': 'X', 'b': 'O', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': 'X', 'h': '_'})
        self.assertEqual(print_board(Xwin),{'c': 'X', 'b': 'X', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': 'X', 'h': '_'})
        self.assertEqual(print_board(Owin),{'c': 'O', 'b': 'O', 'i': '_', 'e': '_', 'g': '_', 'd': '_', 'f': '_', 'a': 'O', 'h': '_'})


if __name__ == '__main__':
    unittest.main()
