
class Flight:
    def __init__(self, originLocationCode, destinationLocationCode,departureDate,returnDate,adults, children, travelClass,currencyCode, maxPrice):
        self.originLocationCode = originLocationCode
        self.destinationLocationCode = destinationLocationCode
        self.departureDate = departureDate
        self.returnDate = returnDate
        self.adults = adults
        self.children = children
        self.travelClass = travelClass
        self.currencyCode = currencyCode
        self.maxPrice = maxPrice

    # Getters and Setters

    def getOriginLocationCode(self):
        return self.originLocationCode

    def setOriginLocationCode(self, originLocationCode):
        self.originLocationCode = originLocationCode

    def getDestinationLocationCode(self):
        return self.destinationLocationCode

    def setDestinationLocationCode(self, destinationLocationCode):
        self.destinationLocationCode = destinationLocationCode

    def getDepartureDate(self):
        return self.departureDate

    def setDepartureDate(self, departureDate):
        self.departureDate = departureDate

    def getReturnDate(self):
        return self.returnDate

    def setReturnDate(self, returnDate):
        self.returnDate = returnDate

    def getAdults(self):
        return self.adults

    def setAdults(self, adults):
        self.adults = adults

    def getChildren(self):
        return self.children

    def setChildren(self, children):
        self.children = children

    def getTravelClass(self):
        return self.travelClass

    def setTravelClass(self, travelClass):
        self.travelClass = travelClass

    def getCurrencyCode(self):
        return self.currencyCode

    def setCurrencyCode(self, currencyCode):
        self.currencyCode = currencyCode

    def getMaxPrice(self):
        return self.maxPrice

    def setMaxPrice(self, maxPrice):
        self.maxPrice = maxPrice


