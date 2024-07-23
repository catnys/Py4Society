import requests
from flight import Flight

AMADEUS_API_KEY = '<your-api-key>'
AMADEUS_API_SECRET = '<your-api-secret>'
AMADEUS_BASE = "https://test.api.amadeus.com/v2"
AMADEUS_FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"



CURRENT_ENDPOINT = AMADEUS_BASE + AMADEUS_FLIGHT_OFFERS_ENDPOINT

############


# Auth
AUTH_ENDPOINT = "https://test.api.amadeus.com/v1/security/oauth2/token/"

headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

authParams = {
    'grant_type': 'client_credentials',
    'client_id': AMADEUS_API_KEY,
    'client_secret': AMADEUS_API_SECRET,
}

response = requests.post(url=AUTH_ENDPOINT, headers=headers, data=authParams)
print(response.json())

"""
flight = Flight("LAX", "JFK", "2023-04-01", "2023-04-15", "2", 0, "Economy", "USD", 500)

parameters = {
    'originLocationCode': flight.getOriginLocationCode(),
    'destinationLocationCode': flight.getDestinationLocationCode(),
    'departureDate': flight.getDepartureDate(),
    'adults': flight.getAdults(),
}

response = requests.get(url=CURRENT_ENDPOINT, params=parameters)
print(response.json())

print(flight)
"""


