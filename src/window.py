import arcade
from src.logic.snake import Snake

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

# debug
MOUSEPRESS_ID = 0

class GameWindow(arcade.Window):
    def __init__(self):
        self.mousepress_id = MOUSEPRESS_ID
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, WINDOW_TITLE)

        arcade.set_background_color(arcade.color.WHITE)

        self.snake = Snake(ROW_COUNT, COLUMN_COUNT, CELL_WIDTH, CELL_HEIGHT, MARGIN)

    def on_draw(self):
        arcade.start_render()

        self.snake.draw_sprite_grid()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        column = int(x // (CELL_WIDTH + MARGIN))
        row = int(y // (CELL_HEIGHT + MARGIN))

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")
        if row < ROW_COUNT and column < COLUMN_COUNT:
            self.snake.set_cell_type(row, column, self.mousepress_id)
            self.mousepress_id += 1
            if self.mousepress_id > 3:
                self.mousepress_id = 0
            self.snake.redraw_sprites()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 119:
            self.snake.move_up()

        if symbol == 115:
            self.snake.move_down()

        if symbol == 97:
            self.snake.move_left()

        if symbol == 100:
            self.snake.move_right()

        self.snake.redraw_sprites()

