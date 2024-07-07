sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
"""
What is the Airspeed Velocity of an Unladen Swallow?
Example Output
{
'What': 4, 
'is': 2, 
'the': 3, 
'Airspeed': 8, 
'Velocity': 8, 
'of': 2, 
'an': 2, 
'Unladen': 7, 
'Swallow?': 8
}

"""

# 🚨 Don't change code above 👆
# Write your code below 👇

original_string = "hello world ?"
stringList = original_string.split(" ")
myDict = {word: len(word) for word in stringList if word.isalpha()}
print(myDict)



#
# uppercase_string = ''.join([char.upper() for char in original_string])
# print(uppercase_string)
#
