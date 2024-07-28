from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, -200)
        self.x_move = 5
        self.y_move = 5
        self.speed = 0.0000001
        self.move()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce_in_y(self):
        self.y_move *= -1
        self.move()

    def bounce_in_x(self):
        self.x_move *= -1
        self.move()

    def reset_ball(self):
        self.goto(0, -200)
        self.y_move *= -1
        self.x_move *= -1

    def increase_speed(self):
        self.speed *= 0.00000000009
