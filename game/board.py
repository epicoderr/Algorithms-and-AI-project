import random

class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0]*size for _ in range(size)]
        self.score = 0

    def new_game(self, size=4):
        # Will probably be useful for when a player wants a new game
        self.grid = [[0]*size for _ in range(size)]

    def get_empty(self):
        # Gets empty cells
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == 0]
    
    def add_tile(self, position, value):
        # Adds a value to a tile
        row, column = position
        self.grid[row][column] = value

    def add_random_tile(self):
        # Adds a random tile (either 2 or 4) to a random spot
        empty_cells = self.get_empty()
        if not empty_cells:
            return False
        position = random.choice(empty_cells)
        value = 4 if random.random() < 0.1 else 2
        self.add_tile(position, value)
        return True
    
    def merge_tiles(self):
        return True
    
    def move_tiles(self, direction):
        if direction == 'RIGHT':
        
        if direction == 'LEFT':
            
        if direction == 'UP':
        
        if direction == 'DOWN':
        return True

    def update_score(self, cell_value):
        #A simple way to update the score when tiles are merged, may change this up if it seems more convenient to do another way
        return self.score + cell_value
    
    
