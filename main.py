import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

FINISH_LINE_Y = 280  # Variable to determine if finish line in game

# Class objects
player = Player()
cars = CarManager()
score_board = Scoreboard()

# Method to control turtle
screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.spawn_cars()  # it generates cars randomly
    cars.move_car()  # It moves cars
    if player.ycor() > FINISH_LINE_Y:  # If this is true, it means that player crossed to the other side successfully
        cars.increment_speed()  # It speeds cars up
        player.reset_position()  # Player returns to initial position
        score_board.level_up()  # Update score and highest level

    for car in cars.cars:
        if player.distance(car) < 25:  # If car object touches player, then continue
            player.reset_position()  # Player returns to initial position
            cars.reset_cars_speed()  # It resets car speed
            score_board.reset_level()  # It resets level

screen.exitonclick()
