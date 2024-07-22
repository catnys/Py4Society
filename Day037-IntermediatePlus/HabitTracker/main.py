import requests

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_API_KEY = "<KEY>"
TOKEN = "<TOKEN>"
USERNAME = "katniss"


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
    "id": "<graph-id>",
    "name": "Sports Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# {'message': 'Success.', 'isSuccess': True}
response = requests.post(PIXELA_GRAPH_ENDPOINT, json=graphConfig, headers=headers)
print(response.json())
