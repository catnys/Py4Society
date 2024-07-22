import requests
from datetime import datetime

APP_ID = "<YOUR_APP_ID>"
APP_KEY = '<YOUR_APP_KEY>'
NLP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/7ebd65597e9bab5f78f93992004eb226/myWorkouts/workouts"

GENDER = "<YOUR_GENDER>"
WEIGHT_KG = "<YOUR_WEIGHT_KG>"
HEIGHT_CM = "<YOUR_HEIGHT_CM>"
AGE = "<YOUR_AGE>"
TODAY = datetime.now().strftime("%m/%d/%Y")
NOW = datetime.now().strftime("%H:%M:%S")

exercisInput = input("Tell me which exercises you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nutritionConfig = {
    "query": exercisInput
}

# POST Nutritionix API

response = requests.post(url=NLP_ENDPOINT, json=nutritionConfig, headers=headers)
result = response.json()
duration = response.json()["exercises"][0]["duration_min"]
sport = response.json()["exercises"][0]["user_input"]
calories = response.json()["exercises"][0]["nf_calories"]

#########

headers = {
    "Authorization": "Bearer Howimetyourmother"
}

"""
# GET from Sheety API
result = requests.post(url=SHEETY_ENDPOINT, headers=headers)
"""

# POST for Sheety API

for exercise in result["exercises"]:
    data2send = {
        "workout": {
                    "Date": TODAY,
                    "Time": NOW,
                    "Exercise": sport,
                    "Duration": duration,
                    "Calories": calories
                    }
    }

    responseSheetPost = requests.post(url=SHEETY_ENDPOINT, json=data2send, headers=headers)
    print(responseSheetPost.json())
