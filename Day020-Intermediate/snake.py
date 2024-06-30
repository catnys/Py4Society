from turtle import Turtle


class Snake(Turtle):
    # add constructor
    def __init__(self, health=1, length=3):
        super().__init__()
        self.health = health
        self.length = length

    # getters and setters

    def getHealth(self):
        return self.health

    def getLength(self):
        return self.length

    def setHealth(self, health):
        self.health = health

    def setLength(self, length):
        self.length = length

    def __str__(self):
        return f"{self.length},{self.health}"

    # Custom methods
    def moveForward(self):
        self.forward(10)

    def moveBackward(self):
        self.backward(10)

    def turnLeft(self):
        self.left(10)

    def turnRight(self):
        self.right(10)
