from datetime import datetime
from typing import Dict


class User:
    def __init__(self, name, totalScore, days):
        self.name = name
        self.totalScore = totalScore
        self.days = days

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getTotalScore(self):
        return self.totalScore

    def setTotalScore(self, totalScore):
        self.totalScore = totalScore

    def addDay(self, dateString: str, score: int) -> None:
        date = datetime.strptime(dateString, '%d.%m.%Y')
        self.days[date] = score
        self.totalScore += score

    def __repr__(self):
        return f"User(name={self.name}, totalScore={self.totalScore}, days={self.days})"
