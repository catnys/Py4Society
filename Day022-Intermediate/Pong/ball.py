from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.Xdir = 5
        self.Ydir = 5
        self.moveSpeed = 0.1

    def move(self):
        newX = self.xcor() + self.Xdir
        newY = self.ycor() + self.Ydir
        self.goto(newX, newY)

    def bounceY(self):
        self.Ydir *= -1

    def bounceX(self):
        self.Xdir *= -1
        self.moveSpeed *= 0.9

    def resetPosition(self):
        self.goto(0, 0)
        self.moveSpeed = 0.1
        self.bounceX()
