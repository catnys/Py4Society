import time

from snake import Snake
from turtle import Screen, Turtle


def setUpScreen(screen):
    screen.setup(width=800, height=600)
    screen.bgcolor('black')
    screen.title("Snake Game")
    screen.tracer(0)

def main():
    """main function"""
    segments = []
    tim = Snake()
    screen = Screen()
    setUpScreen(screen)

    startingPosition = [(0,0), (-20,0), (-40,0)]

    for pos in startingPosition:
        newSegment = Turtle("square")
        newSegment.color('white')
        newSegment.penup()
        newSegment.goto(pos)
        segments.append(newSegment)


    isGameOn = True
    while isGameOn:
        screen.update()
        time.sleep(0.1)

    for segment in range(len(segments) -1, 0, -1):
        newX = segments[segment-1].xcor()
        newY = segments[segment-1].ycor()
        segments[segment].goto(newX, newY)
    segments[0].forward(20)
    segments[0].left(90)


    screen.exitonclick()


if __name__ == "__main__":
    main()
