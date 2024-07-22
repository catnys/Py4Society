import requests
from flight import Flight


AMADEUS_API_KEY = '<KEY>'
AMADEUS_API_SECRET = '<KEY>'
AMADEUS_BASE = ""
AMADEUS_FLIGHT_OFFERS_ENDPOINT = "shopping/flight-offers"

flight = Flight("LAX", "JFK", "2023-04-01", "2023-04-15", "2", 0, "Economy", "USD", 500)

print(flight)
