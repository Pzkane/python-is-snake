import arcade, random
from src.extensions.switch import Switch

class Grid():
    def __init__(self, row_count, col_count, cell_width, cell_height, margin):
        self.row_count = row_count
        self.col_count = col_count
        self.cell_width = cell_width
        self.cell_height = cell_height
        self.margin = margin
        
        self.food_spawned = False

        self.init_grid()
        self.init_grid_sprite_list()
        
    def spawn_food(self):
        if self.food_spawned:
            return

        free_cells = list()
        for row in range(self.row_count):
            for col in range(self.col_count):
                if (self.grid[row][col]["type"] == 0):
                    free_cells.append({
                        "row": row,
                        "col": col
                    })
        
        is_listed = False
        while not is_listed:
            rand_row = random.randint(0, self.row_count-1)
            rand_col = random.randint(0, self.col_count-1)
            for cell in free_cells:
                if cell["row"] == rand_row and cell["col"] == rand_col:
                    is_listed = True
                    break
            
        self.grid[rand_row][rand_col]["type"] = 3
        self.food_spawned = True

    # inits
    def init_grid(self):
        self.grid = []
        for row in range(self.row_count):
            self.grid.append([])
            for col in range(self.col_count):
                self.grid[row].append({
                    "type": 0,
                    "position": 0
                })

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
                self.grid_sprite_list[position].color = Switch()._by_grid_value(self.grid[row][col]["type"])

    # setters
    def set_cell_type(self, row, column, value):
        self.grid[row][column]["type"] = value

    # getters
    def get_cell(self, row, column):
        return self.grid[row][column]
