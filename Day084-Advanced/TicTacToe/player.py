
class Player:
    def __init__(self, symbol: str, isWinner: bool = False):
        self.symbol = symbol
        self.isWinner = isWinner

    # define getters and setters
    def setSymbol(self, symbol: str):
        self.symbol = symbol

    def getSymbol(self):
        return self.symbol

    def setIsWinner(self, isWinner: bool):
        self.isWinner = isWinner

    def getIsWinner(self):
        return self.isWinner
