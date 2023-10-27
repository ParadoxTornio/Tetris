import random
import arcade
from config import *


class Figure:
    def __init__(self):
        self.row = 0
        self.column = 5
        self.shape = random.choice(list(SHAPES_DICT.values()))
        self.color = random.choice(COLOR_LIST)

    def change_position(self):
        pass

    def update(self):
        pass

    def add_to_game_field(self, game_field):
        pass

    def draw(self):
        for row in range(len(self.shape)):
            for column in range(len(self.shape[0])):
                if self.shape[row][column] != 0:
                    arcade.draw_rectangle_filled((self.column + column) * BLOCK_SIZE, (self.row + row) * BLOCK_SIZE,
                                                 BLOCK_SIZE, BLOCK_SIZE, self.color)
