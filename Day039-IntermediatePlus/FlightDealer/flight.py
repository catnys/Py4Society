from datetime import datetime

from TravelClass import TravelClass


class Flight:
    def __init__(self, originLocationCode: str, destinationLocationCode: str, departureDate: str,
                 returnDate: str = None, adults: int = 1, children: int = None, travelClass: TravelClass = None,
                 currencyCode: str = None, maxPrice: int = None) -> None:
        if not originLocationCode or not destinationLocationCode or not departureDate or not returnDate:
            raise TypeError(
                "Compulsory parameters (originLocationCode, destinationLocationCode, departureDate, returnDate) must be provided.")

        self.originLocationCode = originLocationCode
        self.destinationLocationCode = destinationLocationCode
        self.departureDate = departureDate
        self.returnDate = returnDate
        self.adults = adults
        self.children = children
        self.travelClass = travelClass
        self.currencyCode = currencyCode
        self.maxPrice = maxPrice

    def __str__(self) -> str:
        return f"Flight from {self.originLocationCode} to {self.destinationLocationCode}, departing on {self.departureDate} and returning on {self.returnDate}. Adults: {self.adults}, Children: {self.children}, Travel Class: {self.travelClass}, Currency: {self.currencyCode}, Max Price: {self.maxPrice}"

    # Custom Methods

    def checkDateFormat(self, date):
        # Validate departureDate format
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            raise ValueError("Invalid date format. Expected YYYY-MM-DD")



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
