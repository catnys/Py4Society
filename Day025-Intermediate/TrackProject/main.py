import csv
from datetime import datetime
from user import User



def readUsersFromCsv(file_path='data.csv'):
    users = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            name = row['Name']
            total_score = int(row['Total Score'])
            days = {
                datetime.strptime(date, '%d.%m.%Y'): int(score)
                for date, score in row.items() if date not in ['Name', 'Total Score']
            }
            user = User(name, total_score, days)
            users.append(user)
    return users


def findUserOnDate(users, name, date_str):
    date = datetime.strptime(date_str, '%d.%m.%Y')
    user = findUserByName(users, name)
    if user:
        score = user.days.get(date, None)
        if score is not None:
            print(f"{user.name}'s score on {date_str}: {score}")
        else:
            print(f"No score found for {user.name} on {date_str}")
    else:
        print(f"{name} not found")


def findUserByName(users, name):
    for user in users:
        if user.name == name:
            return user
    return None


def createUser(name, total_score, days):
    user = User(name, total_score, days)
    return user


def writeUsersToCsv(users, file_path='data.csv'):
    with open(file_path, mode='w') as file:
        csv_writer = csv.writer(file, delimiter=';')
        for user in users:



def main():
    """main method"""
    file_path = 'data.csv'  # Ensure this is the correct path to your CSV file
    users = readUsersFromCsv(file_path)

    for user in users:
        print(user)

    findUserOnDate(users, "Dua Lipa", '9.07.2024')


if __name__ == "__main__":
    main()
