from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 600


def exit_game():
    global is_on
    is_on = False


def check_wall_collision():
    check_positive = snake.head.xcor() >= SCREEN_WIDTH/2 or snake.head.ycor() >= SCREEN_HEIGHT/2
    check_negative = snake.head.xcor() <= -SCREEN_WIDTH/2 or snake.head.ycor() <= -SCREEN_HEIGHT/2
    return check_negative or check_positive


def check_tail_collision():
    # if len(snake.snake) < 5:
    #     return False
    # else:
    for s in snake.snake[1:]:
        if snake.snake[0].distance(s) <= 5:
            return True


screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor('black')
screen.title("My snake game. Press 'x' to exit")
screen.tracer(0)

is_on = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
screen.onkey(exit_game, 'x')
speed = 0.1
while is_on:
    screen.update()
    time.sleep(speed)
    snake.move()
    # food.next_loc()

    if snake.head.distance(food) < 18:
        food.refresh()
        snake.add_length()
        scoreboard.inc_score()
        speed -= 0.002
    if check_wall_collision() or check_tail_collision():
        # exit_game()
        snake.reset_snake()
        scoreboard.reset_score()

# screen.exitonclick()
