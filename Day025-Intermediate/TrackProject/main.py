import csv
from datetime import datetime
from user import User


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


def checkCharacterInList(message: str, charList: list):
    for char in message:
        for i in range(len(charList)):
            if char in charList[i]['char']:
                return True
    return False


def calculatePoints(letter):
    if letter == 'c':
        points = 5
    elif letter == 'e':
        points = 1


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

def displayUsers(users):
    """display all users"""
    for user in users:
        print(user)


def main():
    """main method"""
    """
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

    # Example usage of adding a new day with scores
    newDay = '11.07.2024'
    newDayScores = {
        "New User": 5,
        "Dua Lipa": 7  # Ensure the user names are correct
    }
    addDay2Users(users, newDay, newDayScores)

    # Write updated users back to CSV
    writeUsers2Csv(file_path, users)

    displayUsers(users)
    print("-----")
    findUserScoreOnDate(users, "Dua Lipa", '11.07.2024')
    """

    message = "cccex"
    print("-----")
    evaluateMessage(message)


if __name__ == "__main__":
    main()
