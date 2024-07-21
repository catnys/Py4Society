import requests

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '<API KEY>'

weatherParams = {
    'lat': 34.052235,
    'long': -118.243683,
    'appid': API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weatherParams)
print(response.json())