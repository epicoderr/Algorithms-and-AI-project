import math

#Weight matrix corresponding to the board: so basically where do we want the large value tiles
#A snake pattern such as this works quite well, I will continue testing
WEIGHT_MATRIX = [
    [65536, 32768, 16384, 8192],
    [512,   1024,  2048,  4096],
    [256,   128,   64,    32],
    [1,     2,     4,     8],
]

# Heuristic weights for combining the features, may be adjusted
W_W_SCORE = 0.5
W_SMOOTH = 1.0
W_EMPTY = 10.0

def heuristic(board):
    grid = board.grid

    # Positional Weighted Score: using the weight matrix to give a score to our position
    weighted_score = 0
    for row in range(4):
        for cell in range(4):
            tile_val = grid[row][cell]
            if tile_val > 0:
                weighted_score += tile_val * WEIGHT_MATRIX[row][cell]

    # Smoothness: which means prioritizing tiles that are close in value
    smoothness = 0
    for row in range(4):
        for cell in range(4):
            tile_val = grid[row][cell]
            if tile_val > 0:
                log_val = math.log2(tile_val)
                # Check right neighbor
                if cell < 3 and grid[row][cell+1] > 0:
                    smoothness -= abs(log_val - math.log2(grid[row][cell+1]))
                # Check bottom neighbor
                if row < 3 and grid[row+1][cell] > 0:
                    smoothness -= abs(log_val - math.log2(grid[row+1][cell]))

    # Empty Cells: so how free is the player to move
    empty_cells = len(board.get_empty())

    # Combining all of the components into a final evaluation
    return (W_W_SCORE * weighted_score) + \
           (W_SMOOTH * smoothness) + \
           (W_EMPTY * empty_cells)
