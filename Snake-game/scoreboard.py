from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Courier", 20, 'bold')
COLOR = 'white'
X_COORD = 0
Y_COORD = 270


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.penup()
        self.hideturtle()
        self.color(COLOR)
        self.goto(X_COORD, Y_COORD)
        self.update_score()

    def read_high_score(self):
        with open('high_score.txt') as file:
            self.high_score = int(file.read())

    def inc_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score : {self.score} High Score : {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as file:
                file.write(f'{self.high_score}')
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='GAME OVER', align=ALIGNMENT, font=FONT)