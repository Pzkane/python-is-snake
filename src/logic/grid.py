import arcade

class Grid():
    def __init__(self, row_count, col_count, cell_width, cell_height, margin):
        self.row_count = row_count
        self.col_count = col_count
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin

        self.set_grid()
        self.set_grid_sprite_list()

    # init draw
    def draw_sprite_grid(self):
        self.grid_sprite_list.draw()

    # event redraw
    def redraw_sprites(self):
        for row in range(self.row_count):
            for col in range(self.col_count):
                position = row * self.col_count + col
                if self.grid[row][col]:
                    self.grid_sprite_list[position].color = arcade.color.GREEN
                else:
                    self.grid_sprite_list[position].color = arcade.color.BLACK

    # setters
    def set_grid(self):
        self.grid = []
        for row in range(self.row_count):
            self.grid.append([])
            for col in range(self.col_count):
                self.grid[row].append(False)

    def set_cell_value(self, row, column, value):
        self.grid[row][column] = value

    def set_grid_sprite_list(self):
        self.grid_sprite_list = arcade.SpriteList()
        for row in range(self.row_count):
            for col in range(self.col_count):
                x = col * (self.cell_width + self.margin) + (self.cell_width / 2 + self.margin)
                y = row * (self.cell_height + self.margin) + (self.cell_height / 2 + self.margin)
                sprite = arcade.SpriteSolidColor(self.cell_width, self.cell_height, arcade.color.BLACK)
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list.append(sprite)
    
    # getters
    def get_cell_value(self, row, column):
        return self.grid[row][column]
