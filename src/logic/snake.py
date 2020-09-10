import arcade, copy
from src.logic.grid import Grid

class Snake(Grid):
    def __init__(self, row_count, col_count, cell_width, cell_height, margin):
        super().__init__(row_count, col_count, cell_width, cell_height, margin)
        self.init_snake_position()

    # inits
    def init_snake_position(self):
        self.grid[1][0]["type"] = 1
        self.grid[1][0]["position"] = 1

        self.grid[0][0]["type"] = 2
        self.grid[0][0]["position"] = 2

        self.grid[0][1]["type"] = 2
        self.grid[0][1]["position"] = 3

        self.grid[0][2]["type"] = 2
        self.grid[0][2]["position"] = 4

        self.grid[1][2]["type"] = 2
        self.grid[1][2]["position"] = 5

        self.grid[2][2]["type"] = 2
        self.grid[2][2]["position"] = 6

        self.set_snake_length(6)


    def move_up(self):
        snake = self.get_snake_position()
        self.set_snake_length(snake[-1]["length"])
        new_snake = copy.deepcopy(snake)

        for i in range(self.get_snake_length()):
            if i == 0:
                # actual new values
                new_snake[i]["row"] = snake[i]["row"] + 1
            elif i == snake[-1]["length"] - 1:
                new_snake[i] = snake[-3]
                new_snake[i]["position"] = snake[-1]["length"]
            else:
                new_snake[i] = snake[i-1]
                new_snake[i]["position"] = snake[i-1]["position"]
                new_snake[i]["position"] += 1

        self.update_snake_pos(new_snake)

    def update_snake_pos(self, snake):
        old_snake = self.get_snake_position()
        # unset old snake cells
        for i in range(self.get_snake_length()):
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

    # setters
    def set_snake_length(self, length):
        self.snake_length = length

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
