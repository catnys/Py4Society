class City:
    def __init__(self, keyword: str, countryCode: str = None, include: list = None, max: int = None) -> None:
        self.keyword = keyword
        self.countryCode = countryCode
        self.max = max
        self.include = include

    def getKeyword(self):
        return self.keyword

    def setKeyword(self, keyword: str):
        self.keyword = keyword

    def getCountryCode(self):
        return self.countryCode

    def setCountryCode(self, countryCode: str):
        self.countryCode = countryCode

    def getMax(self):
        return self.max

    def setMax(self, max: int):
        self.max = max
