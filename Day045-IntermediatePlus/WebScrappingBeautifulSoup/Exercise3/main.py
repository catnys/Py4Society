from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/news.ycombinator.com')
soup = BeautifulSoup(response.text, 'html.parser')

# print(soup.prettify())