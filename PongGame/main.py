from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

tim = Turtle('circle')

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("MY PONG GAME")
screen.tracer(0)
r_paddle = Paddle('right')
l_paddle = Paddle('left')
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.up, 'Up')
screen.onkeypress(r_paddle.down, 'Down')
screen.onkeypress(l_paddle.up, 'w')
screen.onkeypress(l_paddle.down, 's')
# ball.speed(2)
tim.hideturtle()
tim.penup()
tim.color('white')
tim.setheading(90)
tim.pensize(10)

tim.goto(0, -SCREEN_HEIGHT/2+10)
while tim.ycor() <= SCREEN_HEIGHT/2:
    tim.pendown()
    tim.forward(20)
    tim.penup()
    tim.forward(20)
# screen.update()
# screen.tracer(1,10)

sleep_time = 0.05
is_game_on = True
while is_game_on:
    time.sleep(sleep_time)
    screen.update()
    ball.refresh()
    # check collision with left or right paddle
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if 330 < ball.xcor() < 370 or -370 < ball.xcor() < -330:
        if l_paddle.distance(ball) <= 50:
            sleep_time *= 0.9
            ball.l_paddle_hit()
        elif  r_paddle.distance(ball) <= 50:
            ball.r_paddle_hit()

    if ball.xcor() > 380:
        # print("Ball out of bound on right side")
        ball.reset_position()
        scoreboard.l_score_inc()
        sleep_time = 0.05

    if ball.xcor() < -380:
        # print("Ball out of bound on left side")
        ball.reset_position()
        scoreboard.r_score_inc()
        sleep_time = 0.05

    if scoreboard.l_score == 11 or scoreboard.r_score == 11:
        is_game_on = False

screen.exitonclick()
