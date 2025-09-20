import unittest
from game.board import Board

class TestSolitaire(unittest.TestCase):

    def setUp(self):
        self.game = Board()
        self.game.add_random_tile()
        self.game.add_random_tile()

    def test_initial_board_has_two_tiles(self):
        # Counts all the non-zero tiles on the board and then looks at if its exactly 2
        tile_count = sum(1 for row in self.game.grid for tile in row if tile != 0)
        self.assertEqual(tile_count, 2)
    
    def test_update_score(self):
        # Sets a score then updates it and sees if it lines up
        self.game.score = 100
        self.game.update_score(260)
        self.assertEqual(self.game.score, 360)
    
    def test_rotate_clockwise(self):
        # Board state before the rotation
        self.game.grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        
        # Expected board after one rotation
        expected_grid = [
            [13, 9, 5, 1],
            [14, 10, 6, 2],
            [15, 11, 7, 3],
            [16, 12, 8, 4]
        ]
        
        self.game.rotate_clockwise()
        self.assertEqual(self.game.grid, expected_grid)

    def test_has_valid_moves_empty(self):
        # Board has empty spaces and thus it should have a valid moves
        self.assertTrue(self.game.has_valid_moves())