from snake import Snake
from turtle import Screen


def main():
    """main function"""
    tim = Snake()
    screen = Screen()

    screen.listen()
    screen.onkey(tim.moveForward, "w")
    screen.onkey(tim.moveBackward, "s")
    screen.onkey(tim.turnLeft, "a")
    screen.onkey(tim.turnRight, "d")
    screen.exitonclick()


if __name__ == "__main__":
    main()
