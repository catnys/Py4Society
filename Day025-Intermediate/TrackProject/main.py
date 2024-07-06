import csv
from user import User

def read_users_from_csv(file_path='data.csv'):
    users = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            name = row['Name']
            total_score = int(row['Total Score'])
            days = {date: int(score) for date, score in row.items() if date not in ['Name', 'Total Score']}
            user = User(name, total_score, days)
            users.append(user)
    return users

def main():
    """main method"""
    file_path = 'data.csv'  # Ensure this is the correct path to your CSV file
    users = read_users_from_csv(file_path)

    for user in users:
        print(user)

if __name__ == "__main__":
    main()