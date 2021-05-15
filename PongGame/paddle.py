from turtle import Turtle

X_COORD = 350
Y_COORD = 0


class Paddle(Turtle):
    def __init__(self, player_side):
        """Take 'left' or 'right' as input to place the paddle on given side"""
        super().__init__()
        if player_side == 'right':
            self.goto(X_COORD, Y_COORD)
        elif player_side == 'left':
            self.goto(-X_COORD, Y_COORD)
        self.shape('square')
        self.setheading(90)
        self.shapesize(1, 5)
        self.penup()
        self.color('white')

    def up(self):
        self.forward(20)

    def down(self):
        self.back(20)
