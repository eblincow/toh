from board import *
from decision import *
from game import *
import unittest


start = {'a': 'X', 'b': 'O', 'c': 'X', 'd': '_', 'e': '_', 'f': '_', 'g': '_', 'h': '_', 'i': '_'}
Xwin = {'a': 'X', 'b': 'X', 'c': 'X', 'd': '_', 'e': '_', 'f': '_', 'g': '_', 'h': '_', 'i': '_'}
Owin = {'a': 'O', 'b': 'O', 'c': 'O', 'd': '_', 'e': '_', 'f': '_', 'g': '_', 'h': '_', 'i': '_'}
complex1 = {'a': 'X', 'b': 'X', 'c': 'O', 'd': 'O', 'e': 'X', 'f': '_', 'g': '_', 'h': '_', 'i': '_'}


class TestBoard(unittest.TestCase):
    def setUp(self):
        pass

    def test_print_board(self):
        # These counts are inflated by 1 because of the menu printed X = You, O = Machine
        game = Game()
        self.assertEqual(game.print_board().count("X"), 1)
        game.BOARD_STATE = start
        self.assertEqual(game.print_board().count("X"), 3)
        game.BOARD_STATE = Xwin
        self.assertEqual(game.print_board().count("X"), 4)
        game.BOARD_STATE = Owin
        self.assertEqual(game.print_board().count("O"), 5)


    def test_decode_move(self):
        g1 = Game()
        self.assertEqual(decode_move("1", "X", g1), {'a': 'X'})
        self.assertEqual(decode_move("5", "X", g1), {'e': 'X'})
        self.assertEqual(decode_move("9", "X", g1), {'i': 'X'})
        self.assertEqual(decode_move("text", [], g1), {})
        self.assertEqual(decode_move("15", [], g1), {})

    def test_get_Xs_and_Os(self):
        # test the functions Xs and Os
        game1 = Game()
        game1.BOARD_STATE = start
        self.assertEqual(set(game1.get_Xs()), set(['1', '3']))
        self.assertEqual(set(game1.get_Os()), set(['2']))

        game2 = Game()
        game2.BOARD_STATE = Xwin
        self.assertEqual(set(game2.get_Xs()), set(['1', '2', '3']))

        game3 = Game()
        game3.BOARD_STATE = Owin
        self.assertEqual(game3.get_Xs(), [])
        self.assertEqual(set(game3.get_Os()), set(['1', '2', '3']))

        game4 = Game()
        game4.BOARD_STATE = complex1
        self.assertEqual(set(game4.get_Xs()), set(['1', '2', '5']))
        self.assertEqual(set(game4.get_Os()), set(['3', '4']))


    def test_check_overlap(self):
        non_winning_combinations = [['1', '2', '5'], ['1', '3', '9'], ['1', '1', '1'], ['0', '22', '33'],
                                    ['-1', '-2', '3'], ['4', '5'], ['5', '6', '1']]
        winning_combinations = [['1', '2', '3'], ['1', '5', '9'], ['8', '5', '2']]
        for non_winner in non_winning_combinations:
            self.assertFalse(check_winning(non_winner), "check_overlap should return False for non winners")

        for winner in winning_combinations:
            self.assertTrue(check_winning(winner))
            self.assertTrue(type(check_winning(winner) == list))


    def test_find_dangerous_squares(self):
        game = Game()
        decision = Decision(game)
        self.assertEqual(decision._find_dangerous_square(['1', '2']), '3')
        self.assertEqual(decision._find_dangerous_square(['2', '3']), '1')
        self.assertEqual(decision._find_dangerous_square(['1', '9']), '5')
        self.assertEqual(decision._find_dangerous_square(['3', '9']), '6')
        # No dangerous square
        self.assertEqual(decision._find_dangerous_square(['2', '9']), None)


    def test_did_anyone_win(self):
        g = Game()
        g.BOARD_STATE = {'a': 'X', 'b': 'X', 'c': 'X'}
        self.assertEqual(g.did_anyone_win("X"), True)

        g = Game()
        g.BOARD_STATE = {'a': 'O', 'd': 'O', 'g': 'O'}
        self.assertEqual(g.did_anyone_win("O"), True)

        g = Game()
        g.BOARD_STATE = {'a': 'O', 'd': 'X', 'g': 'O'}
        self.assertEqual(g.did_anyone_win("O"), False)
        self.assertEqual(g.did_anyone_win("X"), False)


    def test_check_square_availability(self):
        g = Game()
        g.BOARD_STATE = start
        self.assertEqual(check_square_availability(g, '1'), False)
        self.assertEqual(check_square_availability(g, '2'), False)
        self.assertEqual(check_square_availability(g, '4'), True)
        self.assertEqual(check_square_availability(g, '6'), True)


if __name__ == '__main__':
    unittest.main()
