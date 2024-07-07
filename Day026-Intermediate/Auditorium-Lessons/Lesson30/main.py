import os


def readFile(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the lines of the file and strip newline characters
        numbers_list = [int(line.strip()) for line in file]
    return numbers_list

list1 = readFile('file1.txt')
list2 = readFile('file2.txt')

commonList = [x for x in list2 if x in list1]

# Print the list to verify the content
print(list1)
print(list2)
print("-----")

# Write your code above 👆
print(commonList)
