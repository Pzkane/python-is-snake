import arcade
from src.logic.grid import Grid

# Grid rows and columns count
ROW_COUNT = 15
COLUMN_COUNT = 15

# Grid cell values
CELL_WIDTH = 30
CELL_HEIGHT = 30

# The margin between each cell
# and on the edges of the screen.
MARGIN = 5

SCREEN_WIDTH = (CELL_WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (CELL_HEIGHT + MARGIN) * ROW_COUNT + MARGIN
WINDOW_TITLE = "Python is a Snek"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

        self.grid = Grid(ROW_COUNT, COLUMN_COUNT, CELL_WIDTH, CELL_HEIGHT, MARGIN)

    def on_draw(self):
        arcade.start_render()

        self.grid.draw_sprite_grid()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        column = int(x // (CELL_WIDTH + MARGIN))
        row = int(y // (CELL_HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        print(self.grid.get_cell_value(row, column))
        self.grid.set_cell_value(row, column, not self.grid.get_cell_value(row, column))
        self.grid.redraw_sprites()

