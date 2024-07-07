import turtle
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
guessedStates = []

while len(guessedStates) < 50:
    data = pandas.read_csv("50_states.csv")
    allStates = data["state"].tolist()
    usrAnswer = screen.textinput(title=f" {len(guessedStates)}/50 are correct", prompt="Which State do you want to guess?").title()

    if usrAnswer.lower() == "exit":
        missingStates = []
        for state in allStates:
            if state not in guessedStates:
                missingStates.append(state)
        newData = pandas.DataFrame({"state": missingStates})
        newData.to_csv("learn_states.csv", index=False)
        break
    if usrAnswer in allStates:
        guessedStates.append(usrAnswer)
        t = turtle.Turtle()
        t.speed(0)
        t.hideturtle()
        t.penup()
        stateData = data.loc[data["state"] == usrAnswer]
        t.goto(int(stateData["x"]), int(stateData["y"]))
        t.write(usrAnswer, align="center", font=("Arial", 12, "normal"))

screen.exitonclick()