"""
This file implements a special case of the caesar cipher
In this encryption process, the usually shift value in the caesar cipher has a constant value
of 13
"""


# the rot13_encode method to implement the encoding of the message
def rot13_encode(_message):
    encoded_string = ''
    for letter in _message:
        if letter.islower():
            encoded_string += chr(((ord(letter) - 84) % 26) + 97)
        elif letter == " ":
            encoded_string += " "
        else:
            encoded_string += chr(((ord(letter) - 52) % 26) + 65)
    return encoded_string


# the rot13_decode method to implement the decoding of the encoded message
def rot13_decode(encoded_string):
    decoded_string = ""
    for letter in encoded_string:
        if letter.islower():
            decoded_string += chr(((ord(letter) - 110) % 26) + 97)
        elif letter == " ":
            decoded_string += " "
        else:
            decoded_string += chr(((ord(letter) - 78) % 26) + 65)
    return decoded_string


# Alerting the user to enter to message to be encoded or decoded
message = input("Enter message : ")

# Prompting the use to make a choice between encoding the message or decoding it
print("What do you wish to do with the message?")
print("1 : Encode")
print("2 : Decode")

# Storing the user's choice
user_choice = int(input("Choice : "))

# conditional statement to help implement the decoding or encoding
if user_choice == 1:
    print("Encoded message =>", rot13_encode(message))
elif user_choice == 2:
    print("Decoded message =>", rot13_decode(message))
else:
    raise Exception("Invalid choice")

