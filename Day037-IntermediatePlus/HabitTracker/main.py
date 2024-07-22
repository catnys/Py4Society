import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_API_KEY = "<KEY>"
TOKEN = "<TOKEN>"
USERNAME = "katniss"
GRAPH_ID = "<GRAPH_ID>"


PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"


Parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "no"
}

# response = requests.post(url=PIXELA_ENDPOINT, json=Parameters)
# print(response.json())


graphConfig = {
    "id": GRAPH_ID,
    "name": "Sports Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
"""
# {'message': 'Success.', 'isSuccess': True}
response = requests.post(PIXELA_GRAPH_ENDPOINT, json=graphConfig, headers=headers)
print(response.json())
"""

PIXELA_CREATE_PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{GRAPH_ID}"

pixelData = {
    "date": "20240402",
    "quantity": "9.75"
}

""""
response = requests.post(url=PIXELA_CREATE_PIXEL_ENDPOINT,json=pixelData, headers=headers)
print(response.json())
"""

print(TODAY.strftime("%d/%m/%Y"))

