class Player:
    def __init__(self, type: str,isFilled = False):
        self.type = type
        self.isFilled = isFilled

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def setIsFilled(self, isFilled):
        self.isFilled = isFilled

    def getIsFilled(self):
        return self.isFilled

