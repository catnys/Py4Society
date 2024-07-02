import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.goUp,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.createCar()
    carManager.moveCars()

    # Detect collision
    for car in carManager.allCars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect cross the line
    if player.hasFinishLine():
        player.goToStart()
        carManager.moveCars()
        carManager.levelUp()
        scoreboard.increase_level()

screen.exitonclick()
