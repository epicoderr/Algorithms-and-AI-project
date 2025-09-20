from game.board import Board
# placeholder heuristic
def heuristic(board):
    score_weight = 1
    empty_cell_weight = 10
    
    current_score = board.score
    
    empty_cells = len(board.get_empty())
    
    return (current_score * score_weight) + (empty_cells * empty_cell_weight)