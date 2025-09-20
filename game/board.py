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
    
    def update_score(self, cell_value):
        #A simple way to update the score when tiles are merged, may change this up if it seems more convenient to do another way
        self.score += cell_value
    
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
    
    def has_valid_moves(self):
        #Useful for seeing if there are valid moves
        if self.get_empty():
            return True
        
        for r in range(self.size):
            for c in range(self.size):
                if c < self.size - 1 and self.grid[r][c] == self.grid[r][c+1]:
                    return True
                if r < self.size - 1 and self.grid[r][c] == self.grid[r+1][c]:
                    return True
        
        return False

    def display(self):
        #Used AI for this, its just a display for the user
        print("-" * (6 * self.size + 1))
        for row in self.grid:
            print("|", end="")
            for cell in row:
                if cell == 0:
                    print(" " * 5 + "|", end="")
                else:
                    print(f"{cell:^5}|", end="")
            print()
            print("-" * (6 * self.size + 1))
        print(f"Current Score: {self.score}")
    
    def rotate_clockwise(self):
        transposed_grid = list(zip(*self.grid))
    
        rotated_grid = [list(row)[::-1] for row in transposed_grid]
    
        self.grid = rotated_grid
    
    def move_tiles(self, direction):
        changed = False
        # This is handled for the direction being right by default, and then for the other directions I just rotate to make it work
        if direction in ["RIGHT", "LEFT", "UP", "DOWN"]:
            if direction == "LEFT":
                self.rotate_clockwise()
                self.rotate_clockwise()
        
            elif direction == "UP":
                self.rotate_clockwise()
                self.rotate_clockwise()
                self.rotate_clockwise()
            
            elif direction == "DOWN":
                self.rotate_clockwise()

            # We first get all non zero values and then add zeros to the left to shift the row
            for i in range(self.size):
                row = self.grid[i]
                new_row = [cell for cell in row if cell != 0]
                shifted_row = [0] * (self.size - len(new_row)) + new_row
            # We see if we need to merge anything and do that
                for j in range(self.size - 1, 0, -1):
                    if shifted_row[j] == shifted_row[j-1] and shifted_row[j] != 0:
                        shifted_row[j] *= 2
                        self.update_score(shifted_row[j])
                        shifted_row[j-1] = 0
            #We shift again in case a merge occured
                new_row = [tile for tile in shifted_row if tile != 0]
                final_row = [0] * (self.size - len(new_row)) + new_row

                if final_row != self.grid[i]:
                    changed = True
            
                self.grid[i] = final_row

            # We change it back to how it was
            if direction == "LEFT":
                self.rotate_clockwise()
                self.rotate_clockwise()
        
            elif direction == "UP":
                self.rotate_clockwise()
            
            elif direction == "DOWN":
                self.rotate_clockwise()
                self.rotate_clockwise()
                self.rotate_clockwise()

        if changed == True:
            self.add_random_tile()
            return True
        else:
            return False
    
    
