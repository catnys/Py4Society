from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time


def setScreen(screen: Screen):
    """Adjust the screen of the pong game"""
    screen.bgcolor('black')
    screen.setup(800, 600)
    screen.title("Pong")
    screen.tracer(0)


def refreshScreen(screen: Screen):
    """Refresh the screen of the pong game"""
    screen.update()


def detectCollisionOnWall(ball: Ball):
    # detect collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounceY()

    if ball.xcor() < -380 or ball.xcor() > 380:
        ball.bounceX()


def detectCollisionOnPaddle(ball: Ball, rightPaddle: Paddle, leftPaddle: Paddle):
    if ball.distance(rightPaddle) < 50 and ball.xcor() > 340 or ball.distance(leftPaddle) < 50 and ball.xcor() < -340:
        ball.bounceX()


def main():
    """"main function"""
    isGameOn = True
    screen = Screen()
    ball = Ball()

    setScreen(screen)
    screen.listen()

    rightPaddle = Paddle((350, 0))
    leftPaddle = Paddle((-350, 0))

    screen.onkey(rightPaddle.moveUp, "Up")
    screen.onkey(rightPaddle.moveDown, "Down")
    screen.onkey(leftPaddle.moveUp, "w")
    screen.onkey(leftPaddle.moveDown, "s")

    while isGameOn:
        time.sleep(1 / 60)
        screen.update()
        ball.move()

        detectCollisionOnWall(ball)
        detectCollisionOnPaddle(ball, rightPaddle, leftPaddle)

    screen.exitonclick()


if __name__ == "__main__":
    main()
