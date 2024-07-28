
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("cyan")
        self.penup()
        self.score = 0
        self.life = 2
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-230, 240)
        self.write(f"Score: {self.score} \nlife: {self.life}", align="center", font=("Courier", 15, "bold"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! \nScore: {self.score} \nlife: {self.life}", align="center", font=("Courier", 30, "bold"))
