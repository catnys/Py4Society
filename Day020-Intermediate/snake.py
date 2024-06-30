class Snake:
    # add constructor
    def __init__(self, health=1, length=3):
        self.health = health
        self.length = length

    # getters and setters

    def getHealth(self):
        return self.health

    def getLength(self):
        return self.length

    def setHealth(self, health):
        self.health = health

    def setLength(self, length):
        self.length = length

    def __str__(self):
        return f"{self.length},{self.health}"
