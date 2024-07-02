import random as random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars = []

    def createCar(self):
        rand = random.randint(1, 6)
        if rand == 1:
            newCar = Turtle("square")
            newCar.color(random.choice(COLORS))
            newCar.penup()
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.goto(300, random.randint(-250, 250))
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)
