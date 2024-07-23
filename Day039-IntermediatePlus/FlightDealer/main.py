import requests
import pandas as pd
import csv
from flight import Flight
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

AMADEUS_API_KEY = 'YOUR_API_KEY'
AMADEUS_API_SECRET = 'YOUR_API_SECRET'

AMADEUS_BASE = "https://test.api.amadeus.com/v2"
AMADEUS_FLIGHT_OFFERS_ENDPOINT = "/shopping/flight-offers"
AMADEUS_CITIES_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
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

    df = pd.read_csv(filename, sep=';', header=0)

    # Extract the first column into a list
    first_column_list = df.iloc[:, 0].str.upper().tolist()

    # Print the list
    print(first_column_list)
    return first_column_list


def getIATA(cityNames):
    """Function to retrieve IATA codes for given city names."""
    token = getBearerToken()

    headers = {
        'Authorization': "Bearer " + token
    }

    # Initialize an empty dictionary to store city-IATA pairs
    city_iata_dict = {}

    for cityName in cityNames:
        print(f"Processing {cityName}")

        parameters = {
            "keyword": cityName
        }

        # Make the API call
        response = requests.get(url=AMADEUS_CITIES_ENDPOINT, params=parameters, headers=headers)
        data = response.json()

        # Check if the response contains data
        if 'data' in data and len(data['data']) > 0:
            # Extract IATA codes for the city
            iata_codes = [item['iataCode'] for item in data['data'] if item['name'].lower() == cityName.lower()]

            # Check if the city is already in the dictionary
            if cityName in city_iata_dict:
                # Update existing IATA codes with new ones
                city_iata_dict[cityName].extend(iata_codes)
            else:
                # Add new city with its IATA codes
                city_iata_dict[cityName] = iata_codes
        else:
            print(f"No data found for {cityName}")

    # Convert the dictionary to a list of dictionaries
    city_iata_list = [{"city": k, "iata": v} for k, v in city_iata_dict.items()]

    return city_iata_list

def main():
    """Main function"""
    # Retrieve city names from a CSV file
    cityNames = retrieveCities("base_price_data.csv")

    # Fetch IATA codes for the retrieved city names
    city_iata_list = getIATA(cityNames)

    # Print the list of cities and their IATA codes
    print(city_iata_list)

if __name__ == "__main__":
    main()
