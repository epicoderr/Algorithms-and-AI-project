import unittest
import math
from game.board import Board
from ai.expectiminimax import expectiminimax
from ai.heuristic import heuristic

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
        self.game.new_game()
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

    def test_rotate_four_times_returns_original(self):
        #Tests that rotating 4 times does a full loop correctly back to the original position
        self.game.grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]
        original = self.game.grid
        
        self.game.rotate_clockwise()
        self.game.rotate_clockwise()
        self.game.rotate_clockwise()
        self.game.rotate_clockwise() # Back to original
        
        self.assertEqual(self.game.grid, original)

    def test_has_valid_moves_empty(self):
        self.game.new_game() 
        # Board has empty spaces and thus it should have a valid moves
        self.assertTrue(self.game.has_valid_moves())

    def test_has_valid_moves_full(self):
        self.game.new_game() 
        # Board is full but has a valid move
        self.game.grid = [
            [2, 2, 8, 4],
            [4, 64, 16, 8],
            [128, 16, 32, 2],
            [2, 4, 64, 4]
        ]
        self.assertTrue(self.game.has_valid_moves())

    def test_move_tiles_merge(self):
        #Tests that merges work as expected
        self.game.new_game() 
        self.game.grid = [
            [2, 2, 4, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_grid = [
            [0, 0, 4, 8],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        initial_score = self.game.score

        #We replace the function and then add it back because otherwise the grids cannot be reloably compared
        original = self.game.add_random_tile
        self.game.add_random_tile = lambda: True 

        self.game.move_tiles("RIGHT")

        self.game.add_random_tile = original
       
        self.assertEqual(self.game.grid, expected_grid)
        self.assertEqual(self.game.score, initial_score + 12)

    def test_move_tiles_triple_merge(self):
        #Tests that merges work as expected if theres a scenario like this where we need to merge the two rightmost ones
        self.game.new_game() 
        self.game.grid = [
            [2, 2, 2, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        expected_grid = [
            [0, 0, 2, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        initial_score = self.game.score

        #We replace the function and then add it back because otherwise the grids cannot be reloably compared
        original = self.game.add_random_tile
        self.game.add_random_tile = lambda: True 

        changed = self.game.move_tiles("RIGHT")

        self.game.add_random_tile = original
       
        self.assertTrue(changed)
        self.assertEqual(self.game.grid, expected_grid)
        self.assertEqual(self.game.score, initial_score + 4)

    def test_move_tiles_merge_and_rotation(self):
        #Tests that merges work as expected alongside a rotation
        self.game.new_game() 
        self.game.grid = [
            [0, 0, 0, 4],
            [0, 0, 0, 4],
            [0, 0, 0, 2],
            [0, 0, 0, 2]
        ]
        expected_grid = [
            [0, 0, 0, 8],
            [0, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        initial_score = self.game.score

        #We replace the function and then add it back because otherwise the grids cannot be reloably compared
        original = self.game.add_random_tile
        self.game.add_random_tile = lambda: True 

        changed = self.game.move_tiles("UP")

        self.game.add_random_tile = original
       
        self.assertTrue(changed)
        self.assertEqual(self.game.grid, expected_grid)
        self.assertEqual(self.game.score, initial_score + 12)
    
    def test_move_tiles_no_change(self):
        self.game.new_game() 
        self.game.grid = [
            [2, 4, 8, 16],
            [0, 0, 0, 4],
            [0, 0, 0, 2],
            [0, 0, 0, 2]
        ]
        
        original = self.game.grid
        initial_score = self.game.score
        
        changed = self.game.move_tiles("RIGHT")
        
        self.assertFalse(changed)
        self.assertEqual(self.game.grid, original)
        self.assertEqual(self.game.score, initial_score)

    def test_no_valid_moves(self):
        #Tests if has_valid_moves is able to recognize a board with none
        self.game.new_game() 

        self.game.grid = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [2, 4, 8, 16],
            [32, 64, 128, 256]
        ]
        
        self.assertFalse(self.game.has_valid_moves())

    def test_heuristic_weighted_score(self):
        #Tests whether the score is calcluated accurately
        WEIGHT_MATRIX = [
        [16, 8, 4, 2],
        [8, 4, 2, 1],
        [4, 2, 1, 0],
        [2, 1, 0, 0]
    ]
        self.game.new_game() 
        self.game.grid = [
            [128, 64, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        # Expected weighted score: (128 * 16) + (64 * 8) = 2048 + 512 = 2560
        expected_weighted_score = 2560

        # Manually calculate the weighted component then compare
        actual_weighted_score = 0
        for r in range(4):
            for c in range(4):
                actual_weighted_score += self.game.grid[r][c] * WEIGHT_MATRIX[r][c]

        self.assertEqual(actual_weighted_score, expected_weighted_score)

    def test_expectiminimax_base_case(self):
        #Tests whether the expectiminimax is applying the heuristic correctly
        depth = 0
        is_max_player = True
        
        expected_value = heuristic(self.game) 
        
        value, best_move = expectiminimax(self.game, depth, is_max_player)
        
        self.assertEqual(value, expected_value)
        self.assertIsNone(best_move)

    def test_expectiminimax_no_valid_moves_max_player(self):
        #Tests if expectiminimax is able to recognize a board with no moves as MAX player
        self.game.new_game() 
        self.game.grid = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [2, 4, 8, 16],
            [32, 64, 128, 256]
        ]
        
        depth = 1 
        is_max_player = True
        
        value, best_move = expectiminimax(self.game, depth, is_max_player)
        
        # When no valid moves change the board state, max_value remains at -math.inf
        self.assertEqual(value, -math.inf)
        self.assertIsNone(best_move)

    def test_expectiminimax_no_valid_moves_chance_player(self):
        #Tests if expectiminimax is able to recognize a board with no moves as CHANCE
        self.game.new_game() 
        self.game.grid = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [2, 4, 8, 16],
            [32, 64, 128, 256]
        ]
        
        depth = 1 
        is_max_player = False
        
        expected_heuristic_value = heuristic(self.game)
        value, best_move = expectiminimax(self.game, depth, is_max_player)
        
        # When no valid moves change the board state, max_value remains at -math.inf
        self.assertEqual(value, expected_heuristic_value)
        self.assertIsNone(best_move)

    def test_expectiminimax_max_player_move(self):
        #Tests that max player is able to identify a correct move
        self.game.new_game()
        self.game.grid = [
            [2, 0, 0, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]

        depth = 1 
        value, best_move = expectiminimax(self.game, depth, True)
        
        # Only left and right can be correct moves here since they result in a merge and point increase
        self.assertIn(best_move, ["LEFT", "RIGHT"])
        self.assertTrue(value > -math.inf)
    
    def test_expectiminimax_chance_player_calculation(self):
        # Simulates a calculation the chance player makes
        # We set up a board where the game can either continue or end depending on whether it randomly adds a 2 or 4
        # It is then possible to calculate and verify whether the chance player is doing it correctly
        self.game.new_game()
        self.game.grid = [
            [2, 0, 8, 16],
            [32, 64, 128, 256],
            [512, 1024, 8, 16],
            [32, 64, 128, 256]
        ]
        
        depth = 1
        is_max_player = False
        
        board_2 = Board()
        board_2.grid = [row[:] for row in self.game.grid]
        board_2.grid[0][1] = 2
        value_2 = heuristic(board_2)

        board_4 = Board()
        board_4.grid = [row[:] for row in self.game.grid]
        board_4.grid[0][1] = 4
        value_4 = heuristic(board_4)

        prob_2 = 0.9
        prob_4 = 0.1
        expected_value = (prob_2 * value_2 + prob_4 * value_4) / 1
        
        value, best_move = expectiminimax(self.game, depth, is_max_player)
        
        self.assertAlmostEqual(value, expected_value)
        self.assertIsNone(best_move)

    def test_move_tiles_invalid_direction(self):
        #Tests that the user cannnot put an invalid direction as an input
        self.game.new_game() 
        self.game.grid = [
            [2, 4, 8, 16],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        original_grid = [row[:] for row in self.game.grid]
        initial_score = self.game.score
        
        changed = self.game.move_tiles("INVALID")
        
        self.assertFalse(changed)
        self.assertEqual(self.game.grid, original_grid)
        self.assertEqual(self.game.score, initial_score)

    def test_new_game_resets_state(self):
        #Tests that new game is working properly
        self.game.score = 100
        self.game.grid = [
            [2, 4, 8, 16],
            [32, 64, 128, 256],
            [2, 4, 8, 16],
            [32, 64, 128, 256]
        ]
        
        self.game.new_game()
        self.assertEqual(self.game.score, 0)
        self.assertTrue(all(cell == 0 for row in self.game.grid for cell in row))

    def test_get_empty_and_add_tile(self):
        # Tests the functions of get_empty and add_tile
        self.game.new_game()
        empty_before = self.game.get_empty()
        self.assertEqual(len(empty_before), 16)

        position = (0, 0)
        self.game.add_tile(position, 2)
        empty_after = self.game.get_empty()
        self.assertEqual(len(empty_after), 15)
        self.assertEqual(self.game.grid[0][0], 2)
