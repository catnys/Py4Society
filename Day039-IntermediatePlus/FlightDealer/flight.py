from datetime import datetime

from travel_class import TravelClass


class Flight:
    def __init__(self, originLocationCode: str, destinationLocationCode: str, departureDate: str,
                 returnDate: str = None, adults: int = 1, children: int = None, travelClass: TravelClass = None,
                 currencyCode: str = None, max: int = None, maxPrice: int = None, nonStop: str = "true") -> None:
        if not originLocationCode or not destinationLocationCode or not departureDate or not adults:
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
        self.max = max
        self.maxPrice = maxPrice
        self.nonStop = nonStop

    def __str__(self) -> str:
        return f"Flight from {self.originLocationCode} to {self.destinationLocationCode}, departing on {self.departureDate} and returning on {self.returnDate}. Adults: {self.adults}, Children: {self.children}, Travel Class: {self.travelClass}, Currency: {self.currencyCode}, Max Price: {self.maxPrice}"

    # Custom Methods

    def checkDateFormat(self, date: str) -> bool:
        """
        Validates if the provided date string is in the correct format ('YYYY-MM-DD').

        This method attempts to parse the input date string using the datetime.strptime function with the specified format. If the parsing succeeds,
        it implies the date string is in the correct format, and the method returns True. If the parsing fails due to a ValueError exception,
        it means the date string does not match the expected format, and the method raises a ValueError with a descriptive message.

        Args:
            date (str): The date string to be validated.

        Returns:
            bool: True if the date string is in the correct format, False otherwise.

        Raises:
            ValueError: If the date string is not in the expected 'YYYY-MM-DD' format.
        """
        # Attempt to parse the date string with the expected format
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            # Raise a ValueError if the date string does not match the expected format
            raise ValueError("Invalid date format. Expected YYYY-MM-DD")

    def formatDate(self, date: datetime) -> str:
        """
        Formats a given date object into a string representing the date in 'YYYY-MM-DD' format.

        Args:
            date (datetime): The original date object to be formatted.

        Returns:
            str: The formatted date string.
        """
        return date.strftime("%Y-%m-%d")

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

    def getMax(self):
        return self.max

    def setMax(self, max):
        self.max = max

    def getMaxPrice(self):
        return self.maxPrice

    def setMaxPrice(self, maxPrice):
        self.maxPrice = maxPrice

    def getNonStop(self):
        return self.nonStop

    def setNonStop(self, nonStop):
        self.nonStop = nonStop
