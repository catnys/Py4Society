import requests
import os
from flight import Flight

AMADEUS_API_KEY = 'YOUR_API_KEY'
AMADEUS_API_SECRET = 'YOUR_API_SECRET'

AMADEUS_BASE = "https://test.api.amadeus.com/v2"
AMADEUS_FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"
AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

CURRENT_ENDPOINT = AMADEUS_BASE + AMADEUS_FLIGHT_OFFERS_ENDPOINT


############

def getBearerToken():
    # Auth
    body = {
        'grant_type': 'client_credentials',
        'client_id': AMADEUS_API_KEY,
        'client_secret': AMADEUS_API_SECRET,
    }
    response = requests.post(url=AUTH_URL, data=body)
    print(response.json()['access_token'])
    return response.json()['access_token']


AMADEUS_ACCESS_TOKEN = getBearerToken()


flight = Flight(originLocationCode="LAX", destinationLocationCode="JFK", departureDate="2024-09-01")
print(flight)

"""
headers = {'Authorization': 'Bearer ' + AMADEUS_ACCESS_TOKEN}

parameters = {
    'originLocationCode': flight.getOriginLocationCode(),
    'destinationLocationCode': flight.getDestinationLocationCode(),
    'departureDate': flight.getDepartureDate(),
    'adults': flight.getAdults(),
}

response = requests.get(url=CURRENT_ENDPOINT, params=parameters, headers=headers)
print(response.json())
"""
