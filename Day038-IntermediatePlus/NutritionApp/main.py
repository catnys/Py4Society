import requests

APP_ID = "<YOUR-APP-ID>"
APP_KEY = '<YOUR KEY HERE>'
BASE = "https://trackapi.nutritionix.com"
END_POINT = "/v2/natural/exercise"
NLP_ENDPOINT = BASE + END_POINT


GENDER = "<YOUR GENDER HERE>"
WEIGHT_KG = "<YOUR WEIGHT KG HERE>"
HEIGHT_CM = "<YOUR HEIGHT CM HERE>"
AGE = "<YOUR AGE HERE>"

exercise = input("Tell me which exercises you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nutritionConfig = {
    "query": exercise
}


response = requests.post(url=NLP_ENDPOINT,json=nutritionConfig, headers=headers)
print(response.json())





