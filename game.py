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
        self.next_block_image = None
        self.blocks_images = None

        self.background = arcade.load_texture('images/background.png')

    def setup(self):
        self.blocks_list = arcade.SpriteList()

        self.block_1 = Block('block1', 8, 20)
        self.block_2 = Block('block2', 1, 5)
        self.block2x2 = Block('block2x2', 1, 8)
        self.block4x1 = Block('block4x1', 1, 15)

        self.blocks_list.append(self.block_1)
        self.blocks_list.append(self.block_2)
        self.blocks_list.append(self.block2x2)
        self.blocks_list.append(self.block4x1)
        self.blocks_images = ['images/block1.png',
                              'images/block2.png',
                              'images/block4x1.png',
                              'images/block2x2.png']
        self.next_block = random.choice(self.blocks_images)
        self.next_block_image = arcade.load_texture(str(self.next_block))

        self.physics_engine = arcade.PymunkPhysicsEngine((0, 0))
        self.physics_engine.add_sprite_list(self.blocks_list, friction=0, damping=0)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.blocks_list.draw()
        # for block in self.blocks_list:
        #     block.draw_hit_box(color=arcade.color.RED)
        print(self.next_block)
        arcade.draw_lrwh_rectangle_textured(500, 400, SCREEN_WIDTH, SCREEN_HEIGHT, self.next_block_image)

    def update_player_speed(self):
        pass

    def on_update(self, delta_time):
        self.blocks_list.update()
        self.physics_engine.step()

    def on_key_press(self, key, modifiers):
        pass

    def on_key_release(self, key, modifiers):
        pass


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
