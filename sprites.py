import arcade
from config import *


# blocks_images = {'block1': arcade.load_texture('images/block1.png'), 'block2': arcade.load_texture('images/block2.png'),
#                  'block4x1': arcade.load_texture('images/block4x1.png'),
#                  'block2x2': arcade.load_texture('images/block2x2.png')}
row_cords_x = {
    1: 5,
    2: 40,
    3: 75,
    4: 110,
    5: 145,
    6: 180,
    7: 215,
    8: 250,
    9: 285,
    10: 320}
column_cords_y = {
    1: 670,
    2: 635,
    3: 600,
    4: 565,
    5: 530,
    6: 495,
    7: 460,
    8: 425,
    9: 390,
    10: 355,
    11: 320,
    12: 285,
    13: 250,
    14: 215,
    15: 180,
    16: 145,
    17: 110,
    18: 75,
    19: 40,
    20: 5}


class Block(arcade.Sprite):
    def __init__(self, block_name: str, row, column):
        super().__init__(hit_box_algorithm='Detailed', filename=f'images/{block_name}.png')
        self.block_name = block_name
        self.row = row
        self.column = column
        # self.texture = blocks_images.get(self.block_name)
        if self.block_name == 'block4x1':
            self.center_x = row_cords_x.get(row) + self.texture.width // 2 - 1
            self.center_y = column_cords_y.get(column) + self.texture.height // 2
        if self.block_name == 'block2x2':
            self.center_x = row_cords_x.get(row) + self.texture.width // 2 - 1
            self.center_y = column_cords_y.get(column) + self.texture.height // 2 - 1
        if self.block_name == 'block2':
            self.center_x = row_cords_x.get(row) + self.texture.width // 2
            self.center_y = column_cords_y.get(column) + self.texture.height // 2 - 1
        if self.block_name == 'block1':
            self.center_x = row_cords_x.get(row) + self.texture.width // 2
            self.center_y = column_cords_y.get(column) + self.texture.height // 2 - 1

