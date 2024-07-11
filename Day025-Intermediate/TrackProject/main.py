import csv
from user import User
from typing import List, Dict
from datetime import datetime, timedelta
from typing import List, Dict


def readUsersFromCsv(file_path='data.csv'):
    """read users from csv file"""
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


def findUserScoreOnDate(users, name, date_str):
    """find user on specific date with given name and date"""
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
    """find user with given name"""
    for user in users:
        if user.name == name:
            return user
    return None


def createUser(users, name, totalScore, scores):
    """create new user"""
    days = {datetime.strptime(date, '%d.%m.%Y'): score for date, score in scores.items()}
    new_user = User(name, totalScore, days)
    users.append(new_user)


def writeUsers2Csv(file_path, users):
    """write users to csv file"""
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


def addDay2Users(users, date_str, scores):
    """add new day for users to csv file"""
    for user in users:  # traverse users
        user.addDay(date_str, 0)  # Initialize all users' scores for the new day to 0
    for user in users:
        if user.name in scores:
            user.addDay(date_str, scores[user.name])  # Update with provided scores
            user.totalScore += scores[user.name]  # Correct the total score increment


def addMissingDates(users: List[User], end_date_str: str) -> None:
    """Add missing dates for all users up to the specified end date"""
    end_date = datetime.strptime(end_date_str, '%d.%m.%Y')
    for user in users:
        if user.days:
            start_date = max(user.days.keys())
        else:
            start_date = end_date

        current_date = start_date + timedelta(days=1)
        while current_date <= end_date:
            user.days[current_date] = 0
            current_date += timedelta(days=1)

def checkCharacterInList(message: str, charList: list):
    for char in message:
        for i in range(len(charList)):
            if char in charList[i]['char']:
                return True
    return False


def calculatePoints(letter: str, allowedChars: list):
    points = 0
    for element in allowedChars:
        if element['char'] == letter:
            points += element['points']
            # print(f"{letter}: {element['points']}")

    return points



def evaluateMessage(message: str):
    allowedChars = [
        {
            'char': 'e',
            'points': 1
        },
        {
            'char': 'c',
            'points': 2
        },
        {
            'char': 'x',
            'points': 0
        }
    ]
    totalPoints = 0
    if len(message) != 5 or not checkCharacterInList(message, allowedChars):
        # eliminate any inappropriate message inputs
        print("value is not improperly entered: --> type: string && len --> 5 of int")

    for char in list(message):
        print(char)
        totalPoints += calculatePoints(char, allowedChars)
    print(totalPoints)

    return totalPoints

def displayUsers(users):
    """display all users"""
    for user in users:
        print(user)


def main():
    """Main method"""
    file_path = 'data.csv'
    users = readUsersFromCsv(file_path)

    # Parameters
    message = "ccccc"
    username = "Taylor Swift"
    date = '12.07.2024'

    # Add missing dates for all users
    addMissingDates(users, date)

    # Evaluate the message
    dailyScore = evaluateMessage(message)

    # Find the user
    user = findUserByName(users, username)
    if user:
        # Add the daily score to the user's record
        user.addDay(date, dailyScore)
    else:
        # If user does not exist, create the user with all previous scores set to 0
        existingDates = {date_str: 0 for date_str in sorted([date.strftime('%d.%m.%Y') for date in users[0].days.keys()])}
        createUser(users, username, existingDates)
        # Now find the user again and add the daily score
        user = findUserByName(users, username)
        if user:
            user.addDay(date, dailyScore)

    # Write the updated users back to the CSV
    writeUsers2Csv(file_path, users)
    displayUsers(users)
    findUserScoreOnDate(users, username, date)



if __name__ == "__main__":
    main()
