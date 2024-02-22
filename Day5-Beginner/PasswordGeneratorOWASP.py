import random
import string

def generate_strong_password(length=12):
    # Define character sets for different types of characters
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = uppercase_letters + lowercase_letters + digits + symbols

    # Ensure at least one character from each set is included in the password
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the rest of the password length with random characters
    for _ in range(length - 4):
        password.append(random.choice(all_characters))

    # Shuffle the characters to make the password more random
    random.shuffle(password)

    # Convert the list of characters to a string
    password_str = ''.join(password)

    return password_str

# Example: Generate a strong password with default length (12 characters)
password = generate_strong_password()
print("Generated Password:", password)
