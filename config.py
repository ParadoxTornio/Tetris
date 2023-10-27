import arcade

COLOR_LIST = [arcade.color.GREEN,
              arcade.color.AERO_BLUE,
              arcade.color.GRAY,
              arcade.color.DIAMOND,
              arcade.color.DARK_RED,
              arcade.color.BRONZE]

SPRITE_SCALING = 0.5

BLOCK_SIZE = 27

SCREEN_WIDTH = 450
SCREEN_HEIGHT = 700
SCREEN_TITLE = "game"

MOVEMENT_SPEED = 5

SHAPES_DICT = {
    'I': [[1],
          [2],
          [1],
          [1]],
    'T': [[1, 2, 1],
          [0, 1, 0]],
    'O': [[1, 1],
          [2, 1]],
    'L': [[1, 0],
          [2, 0],
          [1, 1]],
    'J': [[0, 1],
          [0, 2],
          [1, 1]],
    'S': [[0, 1, 1],
          [1, 2, 0]],
    'Z': [[1, 1, 0],
          [0, 2, 1]],
    '.': [[2]]
}

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
