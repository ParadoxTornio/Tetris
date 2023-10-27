import random
import arcade
from config import *
from sprites import Block


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.blocks_list = None

        self.physics_engine = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.block_1 = None
        self.block_2 = None
        self.block2x2 = None
        self.block4x1 = None
        self.block1x1 = None
        self.next_block = None
        self.next_block_name = None
        self.next_block_image = None
        self.blocks_images = None
        self.ground = None
        self.game_field = [[0 for _ in range(0, 10)] for _ in range(0, 20)]

        self.background = arcade.load_texture('images/background.png')

    def setup(self):
        self.ground = arcade.Sprite('images/ground.png', center_x=176, center_y=0, hit_box_algorithm='Simple')
        self.blocks_list = arcade.SpriteList()

        self.block_1 = Block('block1', 8, 20, 0)
        self.block_2 = Block('block2', 1, 5, 0)
        self.block2x2 = Block('block2x2', 1, 8, 0)
        self.block4x1 = Block('block4x1', 1, 15, 0)

        self.blocks_list.append(self.block_1)
        self.blocks_list.append(self.block_2)
        self.blocks_list.append(self.block2x2)
        self.blocks_list.append(self.block4x1)
        self.blocks_images = ['block1',
                              'block2',
                              'block4x1',
                              'block2x2']
        self.next_block_name = random.choice(self.blocks_images)
        self.next_block_image = arcade.load_texture(f'images/{self.next_block_name}.png')
        self.next_block = Block(self.next_block_name, 5, 2, 0)
        self.blocks_list.append(self.next_block)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.blocks_list.draw()
        for block in self.blocks_list:
            block.draw_hit_box(color=arcade.color.RED)
        # if self.next_block
        arcade.draw_lrwh_rectangle_textured(375, 490, self.next_block_image.width // 2,
                                            self.next_block_image.height // 2, self.next_block_image)
        self.ground.draw()
        self.ground.draw_hit_box(color=arcade.color.RED)

    def update_player_speed(self):
        pass

    def on_update(self, delta_time):
        self.blocks_list.update()

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        if key == arcade.key.D:
            self.next_block.angle -= 90
            print(self.next_block.angle)
        if key == arcade.key.A:
            self.next_block.angle += 90
            print(self.next_block.angle)
        if key == arcade.key.DOWN:
            # self.next_block.center_y -= 35
            self.next_block.column += 2
        if key == arcade.key.RIGHT:
            # self.next_block.center_x += 35
            self.next_block.row += 1
        if key == arcade.key.LEFT:
            # self.next_block.center_x -= 35
            self.next_block.row -= 1


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
