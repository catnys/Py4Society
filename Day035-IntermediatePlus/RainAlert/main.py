import requests

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '<YOUR_API_KEY>'

weatherParams = {
    'lat': 34.052235,
    'lon': -118.243683,
    'appid': API_KEY
}

response = requests.get(OWM_ENDPOINT, params=weatherParams)
print(response.json())