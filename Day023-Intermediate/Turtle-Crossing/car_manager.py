from random import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []

    def createCars(self):
        newCar = Turtle("square")
        newCar.color(random.choice(COLORS))
        newCar.penup()
        newCar.shapesize(stretch_wid=2, stretch_len=1)
        newCar.goto(300, random.randint(-250, 250))
        self.allCars.append(newCar)