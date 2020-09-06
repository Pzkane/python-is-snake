import arcade

grid_color_cases = {
    0: arcade.color.BLACK,
    1: arcade.csscolor.RED,
    2: arcade.color.GREEN,
}

class Switch():
    @staticmethod
    def _by_grid_value(value):
        return grid_color_cases.get(value, arcade.color.YELLOW)