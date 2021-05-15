from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        """Create ball object"""
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = 12
        self.y_move = 12

    def refresh(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

        # if self.heading() == 45:
        #     if self.ycor() > 270:
        #         self.setheading(315)
        # elif self.heading() == 135:
        #     if self.ycor() > 270:
        #         self.setheading(225)
        # elif self.heading() == 225:
        #     if self.ycor() < -270:
        #         self.setheading(135)
        # elif self.heading() == 315:
        #     if self.ycor() < -270:
        #         self.setheading(45)
        # self.forward(20)

        #
        # if self.heading() == 0:
        #     if self.xcor() > 350:
        #         self.setheading(270)
        #     elif self.ycor() < -280:
        #         self.setheading(90)
        # elif self.heading() == 90:
        #     if self.xcor() > 350:
        #         self.setheading(180)
        #     elif self.ycor() > 280:
        #         self.setheading(0)
        # elif self.heading() == 180:
        #     if self.xcor() < -350:
        #         self.setheading(90)
        #     elif self.ycor() > 280:
        #         self.setheading(270)
        # elif self.heading() == 270:
        #     if self.xcor() < -350:
        #         self.setheading(0)
        #     elif self.ycor() > 280:
        #         self.setheading(180)
        #
        # if self.heading() == 0:
        #     diff_x = 20
        #     diff_y = -20
        # elif self.heading() == 90:
        #     diff_x = 20
        #     diff_y = 20
        # elif self.heading() == 180:
        #     diff_x = -20
        #     diff_y = 20
        # elif self.heading() == 270:
        #     diff_x = -20
        #     diff_y = -20
        # new_x = self.xcor()+diff_x
        # new_y = self.ycor()+diff_y
        # self.goto(new_x, new_y)

    def l_paddle_hit(self):
        # self.inc_speed()
        self.x_move = 12

    def r_paddle_hit(self):
        # self.inc_speed()
        self.x_move = -12

        # if self.heading() == 45:
        #     self.setheading(135)
        # elif self.heading() == 135:
        #     self.setheading(45)
        # elif self.heading() == 225:
        #     self.setheading(315)
        # elif self.heading() == 315:
        #     self.setheading(225)
        # self.forward(20)

    def reset_position(self):
        self.home()
        self.x_move *= -1
        # self.paddle_hit()

    # def inc_speed(self):
    #     self.x_move *= 1.1
    #     self.y_move *= 1.1
