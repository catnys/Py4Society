import requests

OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/forecast'
API_KEY = '<YOUR_API_KEY>'

weatherParams = {
    'lat': 45.657974,
    'lon': 25.601198,
    'cnt': 4,
    'appid': API_KEY
}
isRain = False
response = requests.get(OWM_ENDPOINT, params=weatherParams)
# print(response.json()['list'][0]['weather'][0]['id'])

for hour in response.json()['list']:
    wcode = hour['weather'][0]['id']
    isRain = True if int(wcode) < 700 else False

if isRain:
    print(f"bring an umbrella.")

