import requests
import pandas as pd
from flight import Flight
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

AMADEUS_API_KEY = 'YOUR_API_KEY'
AMADEUS_API_SECRET = 'YOUR_API_SECRET'

AMADEUS_BASE = "https://test.api.amadeus.com/v2"
AMADEUS_FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"
AUTH_URL = "https://test.api.amadeus.com/v1/security/oauth2/token"

TODAY = datetime.today().date()
SIX_MONTHS_LATER = TODAY + relativedelta(months=+6)

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


def displayFlightOffersInterval():
    AMADEUS_ACCESS_TOKEN = getBearerToken()  # Get a new token for each call

    # Generate date range for the next 6 months
    date_range = pd.date_range(start=TODAY, end=SIX_MONTHS_LATER, freq='D')

    for single_date in date_range:
        # Construct request parameters for each date
        parameters = {
            'originLocationCode': 'IST',  # Example origin location code
            'destinationLocationCode': 'LAX',  # Example destination location code
            'departureDate': single_date.strftime('%Y-%m-%d'),
            'adults': 1  # Example adult count
        }

        # Make the API call
        response = requests.get(url=CURRENT_ENDPOINT, params=parameters,
                                headers={'Authorization': f'Bearer {AMADEUS_ACCESS_TOKEN}'})
        data = response.json()

        # Check if 'data' key exists in the response
        if 'data' in data:
            for offer in data['data']:
                priceInfo = offer.get('price', {})
                totalPrice = priceInfo.get('total', 'N/A')
                currency = priceInfo.get('currency', 'N/A')
                print(
                    f"Date: {single_date.strftime('%Y-%m-%d')}, Flight Offer ID: {offer['id']}, Price: {totalPrice} {currency}")
        else:
            print(f"No flight offers found for {single_date.strftime('%Y-%m-%d')}")


def retrieveCities(filename="base_price_data.csv"):
    """Function to return city names from file"""
    # Load the CSV file, skipping the header row
    df = pd.read_csv(filename, delimiter=';', skiprows=1)

    # Correctly access the first column by its integer index
    cityNames = df.iloc[:, 0].tolist()  # Using .iloc for integer-location based indexing

    # Return the list of city names
    return cityNames

def main():
    """Main function"""
    # Retrieve city names and store them in a variable
    cities = retrieveCities()

    # Optionally, print the list of city names
    print(cities)

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
