from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.snake = []
        self.initialize_snake()
        self.head = self.snake[0]
        # self.head.shape()

    def initialize_snake(self):
        for _ in range(3):
            t = Turtle('square')
            t.penup()
            t.color('white')
            t.goto(self.x, self.y)
            self.x -= 20
            self.snake.append(t)

    def add_length(self):
        t = Turtle('square')
        t.penup()
        t.color('white')
        t.goto(self.snake[-1].pos())
        self.snake.append(t)

    def move(self):
        for s in range(len(self.snake) - 1, 0, -1):
            self.snake[s].goto(self.snake[s - 1].pos())
        # self.snake[0].left(90)
        self.snake[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for s in self.snake:
            s.hideturtle()
        self.snake.clear()
        self.x = 0
        self.y = 0
        self.initialize_snake()
        self.head = self.snake[0]
        # self.head.goto(0, 0)
        # for s in self.snake[3:]:
        #     s.hideturtle()
        #     self.snake.remove(s)
