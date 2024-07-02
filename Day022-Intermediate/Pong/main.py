from turtle import Turtle, Screen


def setScreen(screen: Screen):
    """Adjust the screen of the pong game"""
    screen.listen()
    screen.bgcolor('black')
    screen.setup(800, 600)
    screen.title("Pong")


def moveUp(paddle):
    newY = paddle.ycor() + 20
    paddle.goto(paddle.xcor, newY)


def moveDown(paddle):
    newY = paddle.ycor() - 20
    paddle.goto(paddle.xcor, newY)


def main():
    """"main function"""
    screen = Screen()
    setScreen(screen)

    paddle = Turtle()
    paddle.shape('square')
    paddle.color('white')
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(350, 0)

    screen.listen()
    screen.onkey(moveUp, "Up")

    screen.exitonclick()


if __name__ == "__main__":
    main()
