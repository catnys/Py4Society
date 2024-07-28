class Box:
    def __init__(self, letter: str = None, isEmpty = True):
        self.letter = letter
        self.isEmpty = isEmpty

    # define getters and setters

    def getLetter(self):
        return self.letter

    def setLetter(self, letter):
        self.letter = letter

    def setIsEmpty(self, isEmpty):
        self.isEmpty = isEmpty

    def getIsEmpty(self):
        return self.isEmpty
