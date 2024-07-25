def read_morse_codes_from_file(filename):
    morse_code_map = {}
    with open(filename, 'r') as file:
        for line in file:
            # Strip leading/trailing whitespace and newline characters
            line = line.strip()

            # Split the line into the letter and Morse code
            letter, morse_code = line.split(maxsplit=1)

            # Store the letter-Morse code pair in the dictionary
            morse_code_map[letter] = morse_code

    return morse_code_map


# Usage
filename = 'text.txt'
morse_code_map = read_morse_codes_from_file(filename)

userInput = input('Enter a morse code: ')
cypher_text = ""

for letter in userInput:
    print(f"Letter:  {letter.upper()}, morse code: {morse_code_map[letter.upper()]}")
    if letter in morse_code_map:
        cypher_text += morse_code_map[letter] + " "

