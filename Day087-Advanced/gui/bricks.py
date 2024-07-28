
from turtle import Turtle

class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        self.bricks = []
        self.form_initial_layout()

    def form_initial_layout(self):
        x_cor = -260
        y_cor = 200
        color = ["red", "yellow", "green"]
        for i in range(0, 3):
            temp = x_cor
            for k in range(0, 2):
                temp = x_cor
                for j in range(0, 11):
                    brick = Turtle()
                    brick.shape("square")
                    brick.color(color[i])
                    brick.shapesize(stretch_wid=1, stretch_len=2)
                    brick.shape()
                    brick.penup()
                    brick.goto(temp, y_cor)
                    self.bricks.append(brick)
                    temp += 50
                y_cor -= 30

    def delete_brick(self, brick):
        if brick in self.bricks:
            brick.hideturtle()
            self.bricks.remove(brick)

