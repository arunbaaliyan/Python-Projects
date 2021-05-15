from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'bold')
X_COORD = 0
Y_COORD = 180


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(X_COORD, Y_COORD)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'{self.l_score}  {self.r_score}', align=ALIGNMENT, font=FONT)

    def l_score_inc(self):
        self.l_score += 1
        self.update_score()

    def r_score_inc(self):
        self.r_score += 1
        self.update_score()
