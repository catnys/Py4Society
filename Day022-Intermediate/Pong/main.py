from turtle import Turtle, Screen


def setScreen(screen: Screen):
    """Adjust the screen of the pong game"""
    screen.listen()
    screen.bgcolor('black')
    screen.setup(800, 600)
    screen.title("Pong")
    screen.exitonclick()


def main():
    """"main function"""
    screen = Screen()
    setScreen(screen)


if __name__ == "__main__":
    main()
