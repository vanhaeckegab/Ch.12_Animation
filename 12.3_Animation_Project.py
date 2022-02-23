'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random


class Car:
    def __init__(self, h, w, c, s, f):
        self.h = h
        self.w = w
        self.c = c
        self.s = s
        self.f = f

    def draw_car(self):
        arcade.draw_polygon_filled([[500 * (2 / 3), 95], [490 * (2 / 3), 85], [500 * (2 / 3), 85], [500 * (2 / 3), 40],
                                    [100 * (2 / 3), 40], [100 * (2 / 3), 70], [220 * (2 / 3), 80], [290 * (2 / 3), 110],
                                    [375 * (2 / 3), 110], [425 * (2 / 3), 85], [470 * (2 / 3), 85],
                                    [480 * (2 / 3), 95]],
                                   arcade.color.ASH_GREY)
        arcade.draw_polygon_filled([[230 * 2 / 3, 80], [290 * 2 / 3, 106], [375 * 2 / 3, 106], [415 * 2 / 3, 85]],
                                   arcade.color.BATTLESHIP_GREY)
        arcade.draw_line(335 * (2 / 3), 107, 335 * (2 / 3), 80, arcade.color.ASH_GREY, 10)
        arcade.draw_circle_filled(160 * 2 / 3, 45, 20, arcade.color.BATTLESHIP_GREY)
        arcade.draw_circle_filled(420 * 2 / 3, 45, 20, arcade.color.BATTLESHIP_GREY)


class Tree:
    def __init__(self, h, w, c, s, f, type):
        self.h = h
        self.w = w
        self.c = c
        self.s = s
        self.f = f
        self.t = type # Type will be a random number, one or two, it will determine if it is a pine or normal tree


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)


    def on_draw(self):
        arcade.start_render()
        for flake in self.balls:
            flake.draw_flake()
        arcade.draw_rectangle_filled(300, 300, 600, 10, arcade.color.BROWN)
        arcade.draw_rectangle_filled(300, 300, 10, 600, arcade.color.BROWN)

    def on_update(self, dt):
        for flake in self.balls:
            flake.update_flake()


def main():
    window = MyGame(SW, SH, "Snowfall")
    arcade.run()


if __name__ == "__main__":
    main()
