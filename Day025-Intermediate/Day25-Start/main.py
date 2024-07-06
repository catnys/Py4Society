import csv

file_path = 'weather_data.csv'

with open(file_path, mode='r') as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)  # Skip the header row
    for row in csv_reader:
        print(row)