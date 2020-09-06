import arcade
from src.logic.grid import Grid

class Snake(Grid):
    def __init__(self, row_count, col_count, cell_width, cell_height, margin):
        super().__init__(row_count, col_count, cell_width, cell_height, margin)
        self.init_snake_position()

    # inits
    def init_snake_position(self):
        self.grid[0][0] = 2
        self.grid[1][0] = 2
        self.grid[2][0] = 1

    def move_up(self):
        snake_length = 2
        count = 0
        for row in range(self.row_count):
            if count < snake_length:
                for col in range(self.col_count):
                    if self.grid[row][col] == 1:
                        print('found')
                        self.grid[row+1][col] = 1;
                        self.grid[row][col] = 0;
                        count += 1
                    elif self.grid[row][col] == 2:
                        print('found')
                        self.grid[row+1][col] = 2
                        self.grid[row][col] = 0
                        count += 1

    # getters
    def get_grid(self):
        return self.grid
