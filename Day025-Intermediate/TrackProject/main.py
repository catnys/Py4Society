import csv
from datetime import datetime, timedelta
from typing import List, Dict
from user import User


def readUsersFromCsv(file_path: str = 'data.csv') -> List[User]:
    """Read users from a CSV file"""
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


def findUserScoreOnDate(users: List[User], name: str, date_str: str) -> None:
    """Find user score on a specific date"""
    date = datetime.strptime(date_str, '%d.%m.%Y')
    user = findUserByName(users, name)
    if user:
        score = user.days.get(date)
        if score is not None:
            print(f"{user.name}'s score on {date_str}: {score}")
        else:
            print(f"No score found for {user.name} on {date_str}")
    else:
        print(f"{name} not found")


def findUserByName(users: List[User], name: str) -> User:
    """Find user by name"""
    for user in users:
        if user.name == name:
            return user
    return None


def createUser(users: List[User], name: str, totalScore: int, scores: Dict[str, int]) -> None:
    """Create a new user"""
    days = {datetime.strptime(date, '%d.%m.%Y'): score for date, score in scores.items()}
    new_user = User(name, totalScore, days)
    users.append(new_user)


def writeUsers2Csv(file_path: str, users: List[User]) -> None:
    """Write users to a CSV file"""
    if not users:
        return

    # Collect all dates present in users' records
    all_dates = set()
    for user in users:
        all_dates.update(user.days.keys())
    dateStrs = sorted([date.strftime('%d.%m.%Y') for date in all_dates])

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        # Write header
        header = ['Name', 'Total Score'] + dateStrs
        writer.writerow(header)

        # Write user data
        for user in users:
            row = [user.name, user.totalScore] + [user.days.get(datetime.strptime(date_str, '%d.%m.%Y'), '') for
                                                  date_str in dateStrs]
            writer.writerow(row)


def addMissingDates(users: List[User], end_date_str: str) -> None:
    """Add missing dates for all users up to the specified end date"""
    end_date = datetime.strptime(end_date_str, '%d.%m.%Y')
    for user in users:
        if user.days:
            start_date = max(user.days.keys())
        else:
            start_date = min(user.days.keys())

        current_date = start_date + timedelta(days=1)
        while current_date <= end_date:
            user.days[current_date] = 0
            current_date += timedelta(days=1)


def checkCharacterInList(message: str, allowedChars: List[Dict[str, int]]) -> bool:
    """Check if any character in the message is in the allowed character list"""
    return any(char in [element['char'] for element in allowedChars] for char in message)


def calculatePoints(letter: str, allowedChars: List[Dict[str, int]]) -> int:
    """Calculate points for a given letter based on allowed character list"""
    for element in allowedChars:
        if element['char'] == letter:
            return element['points']
    return 0


def evaluateMessage(message: str) -> int:
    """Evaluate the total points for a message"""
    allowedChars = [
        {'char': 'e', 'points': 1},
        {'char': 'c', 'points': 2},
        {'char': 'x', 'points': 0}
    ]

    if len(message) != 5 or not checkCharacterInList(message, allowedChars):
        print("Message is not valid: must be a string of length 5 containing allowed characters")
        return 0

    totalPoints = sum(calculatePoints(char, allowedChars) for char in message)
    print(f"Total points for '{message}': {totalPoints}")
    return totalPoints


def displayUsers(users: List[User]) -> None:
    """Display all users"""
    for user in users:
        print(user)


def main() -> None:
    """Main method"""
    file_path = 'data.csv'
    users = readUsersFromCsv(file_path)

    # Parameters
    message = "ccccc"
    username = "James asd"
    date = '13.07.2024'

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
        existing_dates = {date_str: 0 for date_str in
                          sorted([date.strftime('%d.%m.%Y') for date in users[0].days.keys()])}
        createUser(users, username, 0, existing_dates)
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
