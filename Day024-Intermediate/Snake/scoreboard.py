from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highestScore = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.updateScoreboard()

    def updateScoreboard(self):
        self.write(f"Score: {self.score} Highest Score: {self.highestScore}", align=ALIGNMENT, font=FONT)

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()

    def setHighestScore(self, score):
        self.highestScore = int(score)

    def getHighestScore(self):
        return self.highestScore

    def getScore(self):
        return self.score
