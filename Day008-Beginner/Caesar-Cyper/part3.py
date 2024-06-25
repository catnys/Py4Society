alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def encrypt(text, shift):
    cipher_text = ""
    for char in text:
      index = int(alphabet.index(char))
      newIndex = (index + shift) % int(len(alphabet))
      cipher_text += alphabet[newIndex]
    print(cipher_text)
    return cipher_text


# TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decrypt_text = ""

    for letter in text:
      index = int(alphabet.index(letter))
      newIndex = (index - shift) % len(alphabet)
      decrypt_text += alphabet[newIndex]

    print(decrypt_text)
    return decrypt_text


def main():
    if direction == "encode":
      encrypted_text = encrypt(text, shift)
    elif direction == "decode":
      decrypted_text = decrypt(text, shift)



#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.



if __name__ == "__main__":
  main()
