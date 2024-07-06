import csv
from datetime import datetime
from user import User


def readUsersFromCsv(file_path='data.csv'):
    users = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file, delimiter=';')
        for row in csv_reader:
            name = row['Name']
            totalScore = int(row['Total Score'])
            days = {
                datetime.strptime(date, '%d.%m.%Y'): int(score)
                for date, score in row.items() if date not in ['Name', 'Total Score']
            }
            user = User(name, totalScore, days)
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


def createUser(users, name, totalScore, scores):
    days = {datetime.strptime(date, '%d.%m.%Y'): score for date, score in scores.items()}
    new_user = User(name, totalScore, days)
    users.append(new_user)


def writeUsers2Csv(file_path, users):
    if not users:
        return

    # Extract the dates from the first user for the header
    dates = list(users[0].days.keys())
    dateStrs = [date.strftime('%d.%m.%Y') for date in dates]

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        # Write header
        header = ['Name', 'Total Score'] + dateStrs
        writer.writerow(header)

        # Write user data
        for user in users:
            row = [user.name, user.totalScore] + [user.days.get(date, '') for date in dates]
            writer.writerow(row)


def displayUsers(users):
    for user in users:
        print(user)


def main():
    """main method"""
    file_path = 'data.csv'  # Ensure this is the correct path to your CSV file
    users = readUsersFromCsv(file_path)

    displayUsers(users)

    newUserName = "New User"
    newUserTotalScore = 20
    newUserScores = {
        '6.07.2024': 4,
        '7.07.2024': 3,
        '8.07.2024': 5,
        '9.07.2024': 4,
        '10.07.2024': 4
    }
    createUser(users, newUserName, newUserTotalScore, newUserScores)

    # Write updated users back to CSV
    writeUsers2Csv(file_path, users)

    displayUsers(users)

    findUserOnDate(users, "Dua Lipa", '9.07.2024')


if __name__ == "__main__":
    main()
