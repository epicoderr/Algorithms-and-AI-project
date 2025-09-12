import random

Directions = ("up", "down", "left", "right")
class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0]*size for _ in range(size)]
        self.score = 0

    def get_empty(self):
        return [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == 0]
    
    def add_tile(self, position, value):
        row, column = position
        self.grid[row][column] = value

    def add_random_tile(self):
        empty_cells = self.get_empty()
        if not empty_cells:
            return False
        position = random.choice(empty_cells)
        value = 4 if random.random() < 0.1 else 2
        self.add_tile(position, value)
        return True
    
    def move_tiles(self):
        return True

    def update_score(self):
        return True
    
