import unittest
from snakeladder import *


class TestDiceRole(unittest.TestCase):
    def test_dice_value(self):
        self.assertGreaterEqual(dice_role(), 1)
        self.assertLessEqual(dice_role(), 6)
        self.assertIn(dice_role(), range(1, 7))


class TestSnakesLadders(unittest.TestCase):
    def test_snakes(self):
        self.assertEqual(snakes_val.get(17), 7)
        self.assertEqual(snakes_val.get(54), 34)
        self.assertEqual(snakes_val.get(87), 24)

    def test_ladders(self):
        self.assertEqual(ladder_val.get(4), 14)
        self.assertEqual(ladder_val.get(28), 84)
        self.assertEqual(ladder_val.get(63), 81)

    def test_won(self):
        try:
            self.assertEqual(is_won('P1', 100), 100)
        except SystemExit:
            pass

    def test_player_name(self):
        p1, p2 = player_names()
        self.assertTrue(type(p1), str)
        self.assertTrue(type(p2), str)


