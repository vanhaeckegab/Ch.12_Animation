'''
ANIMATION PROJECT
-----------------
Your choice!!! Have fun and be creative.

'''
import arcade
import random
import math
SW = 1440
SH = 780

class Car:
    def __init__(self, x, y, c, s):
        self.x = x
        self.y = y
        self.c = c
        self.s = s
        self.move = 0
        self.actual = 0

    def draw_car(self):
        arcade.draw_polygon_outline([[400 * (2 / 3) + self.x, 70 + self.y], [390 * (2 / 3) + self.x, 60 + self.y],
                                    [400 * (2 / 3) + self.x, 60 + self.y], [400 * (2 / 3) + self.x, 15 + self.y],
                                    [0 + self.x, 15 + self.y], [0 + self.x, 45 + self.y],
                                    [120 * (2 / 3) + self.x, 55 + self.y], [190 * (2 / 3) + self.x, 85 + self.y],
                                    [275 * (2 / 3) + self.x, 85 + self.y], [325 * (2 / 3) + self.x, 60 + self.y],
                                    [370 * (2 / 3) + self.x, 60 + self.y], [380 * (2 / 3) + self.x, 70 + self.y]],
                                    arcade.color.BLACK, 3)
        arcade.draw_polygon_filled([[400 * (2 / 3) + self.x, 70 + self.y], [390 * (2 / 3) + self.x, 60 + self.y],
                                    [400 * (2 / 3) + self.x, 60 + self.y], [400 * (2 / 3) + self.x, 15 + self.y],
                                    [0 + self.x, 15 + self.y], [0 + self.x, 45 + self.y],
                                    [120 * (2 / 3) + self.x, 55 + self.y], [190 * (2 / 3) + self.x, 85 + self.y],
                                    [275 * (2 / 3) + self.x, 85 + self.y], [325 * (2 / 3) + self.x, 60 + self.y],
                                    [370 * (2 / 3) + self.x, 60 + self.y], [380 * (2 / 3) + self.x, 70 + self.y]],
                                   self.c)
        arcade.draw_polygon_filled([[130 * (2 / 3) + self.x, 55 + self.y], [190 * (2 / 3) + self.x, 81 + self.y],
                                    [275 * (2 / 3) + self.x, 81 + self.y], [315 * (2 / 3) + self.x, 60 + self.y]],
                                   arcade.color.BATTLESHIP_GREY)
        arcade.draw_line(235 * (2 / 3) + self.x, 82 + self.y, 235 * (2 / 3) + self.x, 55 + self.y, self.c, 10)
        arcade.draw_circle_filled(60 * (2 / 3) + self.x, 20 + self.y, 20, arcade.color.BATTLESHIP_GREY)
        arcade.draw_circle_filled(320 * (2 / 3) + self.x, 20 + self.y, 20, arcade.color.BATTLESHIP_GREY)

    def update_car(self):
        self.move += 1
        if self.move % 2 == 0:
            r = random.randint(0, 3)
            self.x += r
            self.y += r
            self.actual = r
        else:
            self.x -= self.actual
            self.y -= self.actual


class Tree:
    def __init__(self, h, x, s, r, t):
        self.h = h
        self.x = x
        self.s = s
        self.r = r
        self.t = t  # Type will be a random number, one or two, it will determine if it is a pine or normal tree

    def draw_tree(self):
        if self.t == 0:
            def leaf(x, h, rad, l):
                arcade.draw_circle_filled(rad * math.cos(math.radians(45 * l)) + x,
                                          rad * math.sin(math.radians(45 * l)) + h, rad, arcade.color.DARK_JUNGLE_GREEN)
            arcade.draw_rectangle_filled(self.x, self.h/2, self.r * 4 / 5, self.h, arcade.color.BROWN)
            arcade.draw_circle_filled(self.x, self.h, self.r * 1.75, arcade.color.BANGLADESH_GREEN)
            for i in range(8):
                leaf(self.x, self.h, self.r * 1.75, i)
        else:
            arcade.draw_rectangle_filled(self.x, self.h / 2, self.r * 4 / 5, self.h, arcade.color.BROWN)
            arcade.draw_polygon_outline(
                [[self.x, self.h * 1.4], [self.x + self.h * 3 / 10, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 10 - self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 9 - self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 8 - self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 7 - self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 - self.r / 2, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 + self.r / 2, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 7 + self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 8 + self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 9 + self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 10 + self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x - self.h * 3 / 10, self.h * 1.25 - self.h / 5]], arcade.color.BLACK, 3)
            arcade.draw_polygon_filled(
                [[self.x, self.h * 1.4], [self.x + self.h * 3 / 10, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 10 - self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x + self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 9 - self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x + self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 8 - self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x + self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 7 - self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x + self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 - self.r / 2, self.h * 1.25 - self.h],
                 [self.x + self.h * 3 / 6 + self.r / 2, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 6, self.h * 1.25 - self.h],
                 [self.x - self.h * 3 / 7 + self.r / 2, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 7, self.h * 1.25 - 4 * self.h / 5],
                 [self.x - self.h * 3 / 8 + self.r / 2, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 8, self.h * 1.25 - 3 * self.h / 5],
                 [self.x - self.h * 3 / 9 + self.r / 2, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 9, self.h * 1.25 - 2 * self.h / 5],
                 [self.x - self.h * 3 / 10 + self.r / 2, self.h * 1.25 - self.h / 5],
                 [self.x - self.h * 3 / 10, self.h * 1.25 - self.h / 5]], arcade.color.APPLE_GREEN)

    def update_tree(self):
        self.x += self.s

        if self.x > SW + 100:
            self.x -= SW + 100
            self.t = random.randint(0, 1)


class Fence:
    def __init__(self, height, x, base, diff, color, speed):
        self.h = height
        self.x = x
        self.b = base
        self.d = diff
        self.c = color
        self.s = speed

    def draw_fence(self):
        arcade.draw_rectangle_outline(self.x, self.b + self.h / 2, self.d * .75, self.h, arcade.color.BLACK, 3)
        arcade.draw_rectangle_filled(self.x, self.b + self.h / 2, self.d * .75, self.h, self.c)
        arcade.draw_triangle_outline(self.x + (self.d * .75) / 2, self.b + self.h, self.x,
                                     self.b + self.h * 1.2, self.x - (self.d * .75) / 2, self.b + self.h,
                                     arcade.color.BLACK, 3)
        arcade.draw_triangle_filled(self.x + (self.d * .75) / 2, self.b + self.h, self.x,
                                    self.b + self.h * 1.2, self.x - (self.d * .75) / 2, self.b + self.h,
                                    self.c)

    def update_fence(self):
        self.x += self.s
        if self.x > SW + 100:
            self.x = -100


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.DARK_SKY_BLUE)
        self.car = Car(1000, 120, arcade.color.ASH_GREY, 0)
        self.fences = []
        for x in range(-100, SW + 100, 25):
            height = 125
            base = 175
            diff = 25
            color = arcade.color.WHITE
            speed = 12.5
            fence = Fence(height, x, base, diff, color, speed)
            self.fences.append(fence)
        self.trees = []
        for i in range(-100, SW + 100, 175):
            h = random.randint(400, 500)
            x = i
            s = 100
            r = random.randint(40, 60)
            t = random.randint(0, 1)
            tree = Tree(h, x, s, r, t)
            self.trees.append(tree)

    def on_draw(self):
        arcade.start_render()
        for tree in self.trees:
            tree.draw_tree()
        arcade.draw_lrtb_rectangle_filled(0, SW, 175, 0, arcade.color.AO)
        arcade.draw_lrtb_rectangle_filled(0, SW, 155, 25, arcade.color.BLACK)
        arcade.draw_lrtb_rectangle_outline(-10, SW + 10, 175/2 + 15, 175/2 - 6, arcade.color.BANANA_YELLOW, 7)
        arcade.draw_rectangle_outline(SW / 2, 175 + 125 * 4 / 5, SW, 125 / 5, arcade.color.BLACK, 3)
        arcade.draw_rectangle_filled(SW / 2, 175 + 125 * 4 / 5, SW, 125 / 5, arcade.color.WHITE)
        arcade.draw_rectangle_outline(SW / 2, 175 + 125 * 2 / 5, SW, 125 / 5, arcade.color.BLACK, 3)
        arcade.draw_rectangle_filled(SW / 2, 175 + 125 * 2 / 5, SW, 125 / 5, arcade.color.WHITE)
        for fence in self.fences:
            fence.draw_fence()
        self.car.draw_car()

    def on_update(self, dt):
        for fence in self.fences:
            fence.update_fence()
        for tree in self.trees:
            tree.update_tree()
        self.car.update_car()
        print(dt)


def main():
    window = MyGame(SW, SH, "Jackson Dupuy Moment")
    arcade.run()


if __name__ == "__main__":
    main()
