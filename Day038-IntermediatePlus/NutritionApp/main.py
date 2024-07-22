import requests

APP_ID = "<YOUR-APP-ID>"
APP_KEY = '<YOUR KEY HERE>'
NLP_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/7ebd65597e9bab5f78f93992004eb226/myWorkouts/workouts"


GENDER = "<YOUR GENDER HERE>"
WEIGHT_KG = "<YOUR WEIGHT KG HERE>"
HEIGHT_CM = "<YOUR HEIGHT CM HERE>"
AGE = "<YOUR AGE HERE>"


# Methods
def readExcel(response):
    """Reads excel file and returns list of rows"""

def writeExcel(workout, rows):
    """Writes excel file to workout"""

exercise = "Running for 15 minutes."  # input("Tell me which exercises you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

nutritionConfig = {
    "query": exercise
}

response = requests.post(url=NLP_ENDPOINT, json=nutritionConfig, headers=headers)
exerciseDuration = response.json()["exercises"][0]["duration_min"]
exerciseType = response.json()["exercises"][0]["user_input"]
print(exerciseType)
print(exerciseDuration)
print(response.json())
