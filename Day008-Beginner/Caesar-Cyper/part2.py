alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = 'decrypt' #input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = 'hello' # input("Type your message:\n").lower()
shift = 5 # int(input("Type the shift number:\n"))

def encrypt(text, shift):
    cipher_text = ""
    for char in text:
        index = int(alphabet.index(char))
        newIndex = (index + shift) % int(len(alphabet))
        cipher_text += alphabet[newIndex]
    print(cipher_text)
    return cipher_text


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(text, shift):
    decrypt_text = ""

    #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    #e.g.
    #cipher_text = "mjqqt"
    #shift = 5
    #plain_text = "hello"
    #print output: "The decoded text is hello"
    for letter in text:
        index = int(alphabet.index(letter))
        newIndex = (index - shift) % len(alphabet)
        decrypt_text += alphabet[newIndex]

    print(decrypt_text)
    return decrypt_text


#TODO-3: Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a message.


def main():
    encrypted_text = encrypt(text,shift)
    decrypted_text = decrypt(encrypted_text,shift)

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.


if __name__ == "__main__":
    main()