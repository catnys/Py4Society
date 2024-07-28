import requests
from bs4 import BeautifulSoup
import csv

def scrape_nba_stats(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Assuming the data is within table tags and each row contains player details
    table = soup.find_all('table')[0]  # Adjust the index if there are multiple tables
    rows = table.find_all('tr')

    player_data = []

    for row in rows[1:]:  # Skip header row
        columns = row.find_all('td')
        player_name = columns[0].text.strip()
        position = columns[1].text.strip()
        avg_points = columns[2].text.strip()

        player_data.append([player_name, position, avg_points])

    return player_data

def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Player Name', 'Position', 'Average Points Per Game'])  # Header
        writer.writerows(data)

if __name__ == "__main__":
    url = 'http://example-nba-stats-site.com'  # Replace with the actual URL
    data = scrape_nba_stats(url)
    save_to_csv(data, 'nba_player_stats.csv')
    print("Data successfully scraped and saved to nba_player_stats.csv")
