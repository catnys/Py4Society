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
