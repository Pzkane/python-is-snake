import arcade, copy
from src.logic.grid import Grid

class Snake(Grid):
    def __init__(self, row_count, col_count, cell_width, cell_height, margin, time_between_moves: float = 1.0):
        super().__init__(row_count, col_count, cell_width, cell_height, margin)
        self.init_snake_position()
        self.setup(time_between_moves)

    # inits
    def init_snake_position(self):
        self.grid[1][0]["type"] = 1
        self.grid[1][0]["position"] = 1

        self.grid[0][0]["type"] = 2
        self.grid[0][0]["position"] = 2

        self.grid[0][1]["type"] = 2
        self.grid[0][1]["position"] = 3

        self.set_snake_length(6)

    def setup(self, time_between_moves):
        self.snake_is_doomed = False
        self.is_snake_longer_now = False
        self.time_since_update = 0.0
        self.time_between_moves = time_between_moves

        self.up = True
        self.down = False
        self.left = False
        self.right = False

        self.move_query_is_empty = True

    def on_update(self, delta_time: float = 1/60):
        self.time_since_update += delta_time

        if self.time_since_update > self.time_between_moves:
            self.time_since_update = 0
            if self.up:
                self.move_up()

            if self.down:
                self.move_down()

            if self.left:
                self.move_left()

            if self.right:
                self.move_right()

    def move_up(self):
        snake = self.get_snake_position()
        snake_head_row = snake[0]["row"] + 1
        if snake_head_row > self.row_count - 1:
            snake_head_row = 0

        self.update_snake_cells(snake_head_row, snake[0]["col"])

    def move_down(self):
        snake = self.get_snake_position()
        snake_head_row = snake[0]["row"] - 1
        if snake_head_row < 0:
            snake_head_row = self.row_count - 1

        self.update_snake_cells(snake_head_row, snake[0]["col"])

    def move_left(self):
        snake = self.get_snake_position()
        snake_head_col = snake[0]["col"] - 1
        if snake_head_col < 0:
            snake_head_col = self.col_count - 1

        self.update_snake_cells(snake[0]["row"], snake_head_col)

    def move_right(self):
        snake = self.get_snake_position()
        snake_head_col = snake[0]["col"] + 1
        if snake_head_col > self.col_count - 1:
            snake_head_col = 0

        self.update_snake_cells(snake[0]["row"], snake_head_col)

    def query_move_up(self):
        self.up = True
        self.down = False
        self.left = False
        self.right = False
        self.move_query_is_empty = False

    def query_move_down(self):
        self.up = False
        self.down = True
        self.left = False
        self.right = False
        self.move_query_is_empty = False

    def query_move_left(self):
        self.up = False
        self.down = False
        self.left = True
        self.right = False
        self.move_query_is_empty = False

    def query_move_right(self):
        self.up = False
        self.down = False
        self.left = False
        self.right = True
        self.move_query_is_empty = False

    def update_snake_pos(self, snake):
        old_snake = self.get_snake_position()
        # unset old snake cells
        old_snake_length = self.get_snake_length()
        if self.is_snake_longer_now:
            old_snake_length -= 1
            self.make_snake_longer(False)

        for i in range(old_snake_length):
            row = old_snake[i]["row"]
            col = old_snake[i]["col"]
            self.grid[row][col]["position"] = 0
            self.grid[row][col]["type"] = 0

        # set new snake cells
        for i in range(self.get_snake_length()):
            pos = snake[i]["position"]
            row = snake[i]["row"]
            col = snake[i]["col"]
            self.grid[row][col]["position"] = pos
            self.grid[row][col]["row"] = row
            self.grid[row][col]["col"] = col

            if i == 0:
                self.grid[row][col]["type"] = 1
            else:
                self.grid[row][col]["type"] = 2

        self.move_query_is_empty = True

    def update_snake_cells(self, snake_head_row, snake_head_col):
        snake = self.get_snake_position()
        if self.is_snake_longer_now:
            self.set_snake_length(self.get_snake_length() + 1)
        else:
            self.set_snake_length(snake[-1]["length"])
        new_snake = copy.deepcopy(snake)
        new_snake[0]["row"] = snake_head_row
        new_snake[0]["col"] = snake_head_col

        for i in range(self.get_snake_length()):
            if i == snake[-1]["length"] - 1:
                new_snake[i] = snake[-3]
                new_snake[i]["position"] = snake[-1]["length"]
            elif i != 0:
                new_snake[i] = snake[i-1]
                new_snake[i]["position"] = snake[i-1]["position"]
                new_snake[i]["position"] += 1

        print(new_snake)
        if self.check_collisions(new_snake):
            self.update_snake_pos(new_snake)
        else:
            self.snake_is_doomed = True

    def check_collisions(self, snake):
        """
        Check snake's head collision, returns 
        @Bool
        if it can proceed
        """
        # get food location and make snake grow on next step
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.grid[row][col]["type"] == 3:
                    if snake[0]["row"] == row and snake[0]["col"] == col:
                        self.make_snake_longer(True)
                        self.food_spawned = False
                        return True
        
        # check if snake has gotten into itself or barrier
        for i, s_bit in enumerate(snake):
            if i != 0 and i != self.get_snake_length() and s_bit["row"] == snake[0]["row"] and s_bit["col"] == snake[0]["col"]:
                return False

        return True

    # setters
    def set_snake_length(self, length):
        self.snake_length = length

    def make_snake_longer(self, value):
        self.is_snake_longer_now = value

    # getters
    def get_grid(self):
        return self.grid

    def get_snake_length(self):
        return self.snake_length

    def get_snake_position(self):
        """
        Returns all snake cell positions with coordinates, last array element contains snake length value
        """
        length = 0
        snake_info = []
        for row in range(self.row_count):
            for col in range(self.col_count):
                if self.grid[row][col]["type"] == 1 or self.grid[row][col]["type"] == 2:
                    snake_info.append({
                        "position": self.grid[row][col]["position"],
                        "row": row,
                        "col": col
                    })
                    length += 1
        snake_info.sort(key = lambda x: x["position"])

        snake_info.append({
            "length": length
        })

        return snake_info

    def is_doomed(self):
        return self.snake_is_doomed
