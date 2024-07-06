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

    def __repr__(self):
        return f"User(name={self.name}, totalScore={self.totalScore}, days={self.days})"
