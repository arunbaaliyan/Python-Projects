from turtle import Turtle
import random

COLOR = 'blue'
MIN_COORD = -280
MAX_COORD = 280


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color(COLOR)
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(MIN_COORD, MAX_COORD)
        y = random.randint(MIN_COORD, MAX_COORD)
        # color = (random.random(), random.random(), random.random())
        # self.color(color)
        self.goto(x, y)

#
# class Food:
#     def __init__(self):
#         self.t = Turtle('circle')
#         self.initialize_food()
#
#     def initialize_food(self):
#         self.t.color('blue')
#         self.t.penup()
#         self.t.shapesize(0.5, 0.5, 1)
#
#     def next_loc(self):
#         x = random.randint(-500, 500)
#         y = random.randint(-500, 500)
#         self.t.goto(x, y)
