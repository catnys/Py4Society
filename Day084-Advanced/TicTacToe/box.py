class Box:
    def __init__(self, type: str,isEmpty = True):
        self.type = type
        self.isEmpty = isEmpty

    def getType(self):
        return self.type

    def setType(self, type):
        self.type = type

    def setIsEmpty(self, isEmpty):
        self.isEmpty = isEmpty

    def getIsEmpty(self):
        return self.isEmpty

