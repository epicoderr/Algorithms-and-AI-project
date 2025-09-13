import unittest
from game.board import Board

#I have set it up so I can do tests in the future and I have one very simple one to start

class TestSolitaire(unittest.TestCase):

    def setUp(self):
        self.game = Board()
        self.game.new_game()
        for _ in range(2):
            self.game.add_random_tile() 

    def test_initial_board_has_two_tiles(self):
        # Counts all the non-zero tiles on the board and then looks at if its exactly 2
        tile_count = sum(1 for row in self.game.grid for tile in row if tile != 0)
        self.assertEqual(tile_count, 2)