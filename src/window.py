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

        self.snake = Snake(ROW_COUNT, COLUMN_COUNT, CELL_WIDTH, CELL_HEIGHT, MARGIN, 1.0)
        self.game_over = False

    def redraw_all(self):
        self.snake.redraw_sprites()

    def on_draw(self):
        arcade.start_render()

        self.snake.draw_sprite_grid()
        if self.game_over:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, arcade.color.YELLOW, 36, width=0, align="left", anchor_x="center", anchor_y="center")

    def on_update(self, delta_time):
        self.snake.on_update(delta_time)
        self.redraw_all()

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
        if not self.snake.is_doomed():
            print(self.snake.move_query_is_empty)
            if self.snake.move_query_is_empty:
                print('HERE')
                if symbol == 119:
                    self.snake.query_move_up()

                if symbol == 115:
                    self.snake.query_move_down()

                if symbol == 97:
                    self.snake.query_move_left()

                if symbol == 100:
                    self.snake.query_move_right()

                if self.snake.is_doomed():
                    self.game_over = True
        else:
            self.game_over = True
            

