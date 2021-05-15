import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# make player
player = Player()

# make cars object
car_manager = CarManager()

# make scoreeboard
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, 'space')

game_is_on = True
i = -1
car_creation_time = 0.1
# y = 6
while game_is_on:
    i += 1
    time.sleep(car_creation_time)
    screen.update()
    # if i % y == 0:
    car_manager.create_car()
    car_manager.move(scoreboard.level)
    # Detect collision with car
    for c in car_manager.all_cars:
        if player.distance(c) < 20:
            game_is_on = False
            scoreboard.game_over()
    # Detect if level is passed
    if player.is_at_finish_line():
        player.return_to_start()
        scoreboard.level_up()
        # car_creation_time *= 0.9
        # if y > 1:
        #     y -= 1

screen.exitonclick()