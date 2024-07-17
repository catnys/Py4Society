import csv

myList = []

with open('file.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')
    for row in reader:
        myDictionary = {}
        for key, value in row.items():
            myDictionary[key] = value
            myList.append(myDictionary)

for element in myList:
    print(f"{element['Name']}: {element['Age']}, {element['City']}")


