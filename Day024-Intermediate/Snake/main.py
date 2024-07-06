from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import os


def readFile(filename='score.txt'):
    file = open(filename, "r")
    contents = file.read()
    file.close()
    return int(contents)


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    
    # init objects
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    scoreboard.setScore()
    
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    isGameOn = True
    while isGameOn:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food using distance method
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increaseScore()

        # Detect collision with wall.
        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.gameOver()
        # Detect collision with tail.
        for segment in snake.segments:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.gameOver()

    screen.exitonclick()


if __name__ == '__main__':
    main()
