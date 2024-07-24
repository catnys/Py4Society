from bs4 import BeautifulSoup
import requests

response = requests.get('https://appbrewery.github.io/news.ycombinator.com')
soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all(name='a', class_='storylink')
for article in articles:
    print(article.text)

