class Player:
    def __init__(self, type: str,isWinner = False):
        self.type = type
        self.isWinner = isWinner

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def setIsWinner(self, isWinner):
        self.isWinner = isWinner

    def getIsWinner(self):
        return self.isWinner

