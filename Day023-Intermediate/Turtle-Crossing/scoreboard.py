from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.highestScore = 0
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def reset(self):
        if self.highestScore < self.score:
            self.highestScore = self.score
        self.score = 0


    def increaseScore(self):
        self.score += 1
        self.update_scoreboard()
