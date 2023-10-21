import arcade
from config import *
from sprites import Block


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.blocks_list = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.first_block = None

        self.background = arcade.load_texture('images/background.png')

    def setup(self):

        self.blocks_list = arcade.SpriteList()

        self.first_block = Block('block4x1', 1, 1)

        self.blocks_list.append(self.first_block)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
        self.blocks_list.draw()

    def update_player_speed(self):
        pass

    def on_update(self, delta_time):
        self.blocks_list.update()

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
