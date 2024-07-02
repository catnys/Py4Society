from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def moveUp(self):
        newY = self.ycor()
        if self.ycor() < 250:
            newY = self.ycor() + 20
        self.goto(self.xcor(), newY)

    def moveDown(self):
        newY = self.ycor()
        if self.ycor() > -240:
            newY = self.ycor() - 20
        self.goto(self.xcor(), newY)

