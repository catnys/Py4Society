import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

movieNames = []
# Adjusted to find the correct <h3> element with class "title"
for article in soup.find_all(name="h3", attrs={"class": "title"}):
    print(article.text.strip())
    movieNames.append(article.text.strip())


with open("movies.txt", "w") as file:
    for i in range(len(movieNames)-1, -1, -1):
        file.write(movieNames[i] + "\n")



