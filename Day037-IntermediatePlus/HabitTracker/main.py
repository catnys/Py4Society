import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_API_KEY = "<KEY>"

Parameters = {
    "token": "<YOUR TOKEN HERE>",
    "username": "katniss",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=Parameters)
print(response.json())