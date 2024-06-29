from turtle import Turtle, Screen
import random

startRace = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
turtles = []

#Create 6 turtles
for turtle_index in range(0, 6):
    turtleNode = Turtle(shape="turtle")
    turtleNode.penup()
    turtleNode.color(colors[turtle_index])
    turtleNode.goto(x=-230, y=y_positions[turtle_index])
    turtles.append(turtleNode)

if user_bet:
    startRace = True

while startRace:
    for turtle in turtles:
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            startRace = False
            winColor = turtle.pencolor()
            if winColor == user_bet:
                print(f"You've won! The {winColor} turtle is the winner!")
            else:
                print(f"You've lost! The {winColor} turtle is the winner!")

        #Make each turtle move a random amount.
        randomDistant = random.randint(0, 10)
        turtle.forward(randomDistant)

screen.exitonclick()