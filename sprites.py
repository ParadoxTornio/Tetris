import arcade
from config import *

blocks_images = {'block1': 'images/block1.png', 'block2': 'images/block2.png', 'block4x1': 'images/block4x1.png',
                 'block4x4': 'images/block4x4.png'}
row_cords_x = {
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
column_cords_y = {
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


class Block(arcade.Sprite):
    def __init__(self, block_name: str, row, column):
        super().__init__()
        self.block_name = block_name
        self.row = row
        self.column = column
        self.picture = arcade.load_texture(blocks_images.get(block_name))
        # self.picture = arcade.load_texture(f'images/{block_name}.png')
        self.center_x = row_cords_x.get(row)
        self.center_y = column_cords_y.get(column)

    # def on_draw(self):
    #     arcade.draw_lrwh_rectangle_textured(self.center_x, self.center_y,
    #                                         self.picture.width, self.picture.height, self.picture)
