import arcade
# from config import *

column_cords_x = {
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
row_cords_y = {
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
    def __init__(self, block_name: str, row, column, angle):
        super().__init__(hit_box_algorithm='Detailed', filename=f'images/{block_name}.png', angle=angle)
        self.block_name = block_name
        self.row = row
        self.column = column
        self.change_position()

    def change_position(self):
        if self.block_name == 'block4x1':
            self.center_x = column_cords_x.get(self.row) + self.texture.width // 2 - 1
            self.center_y = row_cords_y.get(self.column) + self.texture.height // 2
        if self.block_name == 'block2x2':
            self.center_x = column_cords_x.get(self.row) + self.texture.width // 2 - 1
            self.center_y = row_cords_y.get(self.column) + self.texture.height // 2 - 1
        if self.block_name == 'block2':
            self.center_x = column_cords_x.get(self.row) + self.texture.width // 2
            self.center_y = row_cords_y.get(self.column) + self.texture.height // 2 - 1
        if self.block_name == 'block1':
            self.center_x = column_cords_x.get(self.row) + self.texture.width // 2
            self.center_y = row_cords_y.get(self.column) + self.texture.height // 2 - 1

    def update(self):
        self.change_position()
