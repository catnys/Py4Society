from turtle import Turtle, Screen
from paddle import Paddle


def setScreen(screen: Screen):
    """Adjust the screen of the pong game"""
    screen.bgcolor('black')
    screen.setup(800, 600)
    screen.title("Pong")
    screen.tracer(0)


def refreshScreen(screen: Screen):
    """Refresh the screen of the pong game"""
    screen.update()


def main():
    """"main function"""
    isGameOn = True
    screen = Screen()

    setScreen(screen)
    screen.listen()

    rightPaddle = Paddle((350,0))
    leftPaddle = Paddle((-350,0))

    screen.onkey(rightPaddle.moveUp, "Up")
    screen.onkey(rightPaddle.moveDown, "Down")
    screen.onkey(leftPaddle.moveUp, "w")
    screen.onkey(leftPaddle.moveDown, "s")

    while isGameOn:
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
