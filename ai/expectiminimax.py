from game.board import Board
from ai.heuristic import heuristic
import math
import copy

def expectiminimax(board, depth, is_max_player):
    if depth == 0:
        return heuristic(board), None

    if is_max_player:
        #So if it is AIs turn, we do the standard minimax algorithm where we look at what the opponent or in this case random chance might do
        max_value = -math.inf
        best_move = None
        possible_moves = ["UP", "DOWN", "LEFT", "RIGHT"]
        for move in possible_moves:
            new_board = copy.deepcopy(board)
            
            if new_board.move_tiles(move):
                value, _ = expectiminimax(new_board, depth - 1, False)
                
                if value > max_value:
                    max_value = value
                    best_move = move

        return max_value, best_move
    else:
        #This is where we get the expected value using the probabilities of a 2 or 4 appearing in order to try and find the best move
        expected_value = 0
        empty_cells = board.get_empty()

        if not empty_cells:
            return heuristic(board), None
        
        prob_2 = 0.9
        prob_4 = 0.1

        for cell in empty_cells:
            new_board_2 = copy.deepcopy(board)
            new_board_2.add_tile(cell, 2)
            value_2, _ = expectiminimax(new_board_2, depth - 1, True)
                    
            new_board_4 = copy.deepcopy(board)
            new_board_4.add_tile(cell, 4)
            value_4, _ = expectiminimax(new_board_4, depth - 1, True)
                    
            expected_value += (prob_2 * value_2 + prob_4 * value_4)
                
        expected_value /= len(empty_cells)
                
        return expected_value, None