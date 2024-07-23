import requests
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
    token = requests.post(url=AUTH_URL, data=body).json()['access_token']
    print(token)
    return token


def displayFlightPrices(data):
    # Access the 'data' array from the JSON response
    flightOffers = data.get('data', [])

    for offer in flightOffers:
        # Extract price and currency information
        priceInfo = offer.get('price', {})
        totalPrice = priceInfo.get('total', 'N/A')
        currency = priceInfo.get('currency', 'N/A')

        print(f"Flight Offer ID: {offer['id']}, Price: {totalPrice} {currency}")

AMADEUS_ACCESS_TOKEN = getBearerToken()


flight = Flight(originLocationCode="IST", destinationLocationCode="LAX", departureDate="2024-07-24")
print(flight)


# Header with content type as per Amadeus documentation
header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': 'Bearer ' + AMADEUS_ACCESS_TOKEN
}

parameters = {
    'originLocationCode': flight.getOriginLocationCode(),
    'destinationLocationCode': flight.getDestinationLocationCode(),
    'departureDate': flight.getDepartureDate(),
    'adults': flight.getAdults()
}

response = requests.get(url=CURRENT_ENDPOINT, params=parameters, headers=header)
data = response.json()
print(data)
print("-----\n")
displayFlightPrices(data)

