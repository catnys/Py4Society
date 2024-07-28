import time
from turtle import Screen
from paddel import Paddle
from ball import Ball
from score import Score
from bricks import Bricks

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
score = Score()
bricks = Bricks()
initial_score = 0

screen.listen()
screen.onkey(fun=paddle.move_left, key="Left")
screen.onkey(fun=paddle.move_right, key="Right")

game_on = True

while game_on:
    time.sleep(ball.speed)
    screen.tracer(1)
    screen.update()
    ball.move()

    # collision with wall and paddle
    if ball.xcor() < -270 or ball.xcor() > 270:
        ball.bounce_in_x()
    if ball.ycor() > 270:
        ball.bounce_in_y()
    if ball.ycor() < -320:
        screen.tracer(0)
        ball.reset_ball()
        score.life -= 1
        score.update_score()
        ball.x_move *= -1
        screen.tracer(1)
    if ball.distance(paddle) < 60 and ball.ycor() < -250:
        ball.bounce_in_y()

    for brick in bricks.bricks:
        if ball.distance(brick) < 30:
            screen.tracer(0)
            bricks.delete_brick(brick)
            score.score += 1
            score.update_score()
            ball.bounce_in_y()
            screen.tracer(1)

    if score.score-initial_score > 5:
        ball.increase_speed()
        initial_score = score.score

    if score.life == 0 or len(bricks.bricks) == 0:
        screen.clearscreen()
        screen.tracer(0)
        ball.hideturtle()
        paddle.hideturtle()
        score.game_over()
        screen.tracer(1)
        game_on = False

screen.exitonclick()

//paddel.py
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

//ball.py
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

//bricks.py
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

//score.py
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.penup()
        self.score = 0
        self.life = 2
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-230, 240)
        self.write(f"Score: {self.score} \nlife: {self.life}", align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! \nScore: {self.score} \nlife: {self.life}", align="center", font=("Courier", 30, "bold"))
