from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        if random.randint(1,6) == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            new_car.shapesize(1, 2)
            self.all_cars.append(new_car)

    def move(self, level):
        move_speed = STARTING_MOVE_DISTANCE + (level-1) * MOVE_INCREMENT
        for car in self.all_cars:
            if car.xcor() < -320:
                car.hideturtle()
                self.all_cars.remove(car)
                # self.all_cars.pop(self.all_cars.index(car))
            car.forward(move_speed)
