from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(0, -260)

    def move_left(self):
        x = self.xcor() - 30
        y = self.ycor()
        if x > -230:
            self.goto(x, y)

    def move_right(self):
        x = self.xcor() + 30
        y = self.ycor()
        if x < 230:
            self.goto(x, y)
