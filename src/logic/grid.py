import arcade
from src.extensions.switch import Switch

class Grid():
    def __init__(self, row_count, col_count, cell_width, cell_height, margin):
        self.row_count = row_count
        self.col_count = col_count
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin

        self.init_grid()
        self.init_grid_sprite_list()

    # inits
    def init_grid(self):
        self.grid = []
        for row in range(self.row_count):
            self.grid.append([])
            for col in range(self.col_count):
                self.grid[row].append(0)

    def init_grid_sprite_list(self):
        self.grid_sprite_list = arcade.SpriteList()
        for row in range(self.row_count):
            for col in range(self.col_count):
                x = col * (self.cell_width + self.margin) + (self.cell_width / 2 + self.margin)
                y = row * (self.cell_height + self.margin) + (self.cell_height / 2 + self.margin)
                sprite = arcade.SpriteSolidColor(self.cell_width, self.cell_height, arcade.color.WHITE)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)

    def draw_sprite_grid(self):
        self.grid_sprite_list.draw()
                
    # event redraw
    def redraw_sprites(self):
        for row in range(self.row_count):
            for col in range(self.col_count):
                position = row * self.col_count + col
                print(Switch()._by_grid_value(self.grid[row][col]))
                self.grid_sprite_list[position].color = Switch()._by_grid_value(self.grid[row][col])

    # setters
    def set_cell_value(self, row, column, value):
        self.grid[row][column] = value

    # getters
    def get_cell_value(self, row, column):
        return self.grid[row][column]
