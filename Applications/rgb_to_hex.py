"""
This is program that converts the usual the rgb to the 6-digit hexadecimal format
The rgb values should lie with the range of 0 - 255
The programs uses three functions namely rgb(r, g, b),
"""


def dec_to_hex(number):
    if number == 10:
        return 'A'
    elif number == 11:
        return 'B'
    elif number == 12:
        return 'C'
    elif number == 13:
        return 'D'
    elif number == 14:
        return 'E'
    elif number == 15:
        return 'F'
    else:
        return str(number)


def rgb(r, g, b):
    string = ""
    values_list = [r, g, b]
    for color_value in values_list:
        string += convert_dec_to_hex(color_value)
    return f"{string}"


def convert_dec_to_hex(number):
    converted = ""
    if number < 0:
        return "00"
    elif 0 <= number <= 15:
        return f"0{dec_to_hex(number)}"
    else:
        if number > 255:
            number = 255
        while number != 0:
            converted += dec_to_hex(number % 16)
            number //= 16
        return converted[::-1]


def main():
    rgb_color_code_input = input("Enter the rgb color code in the for r, g, b: ")
    color_code_characters_list = rgb_color_code_input.split(",")
    print(color_code_characters_list)
    rgb_color_code_values = []
    for character in color_code_characters_list:
        code_value = ""
        for letter in character:
            if letter.isnumeric() and character[character.index(letter) - 1] == "-":
                code_value += "-" + letter
            elif letter.isnumeric():
                code_value += letter
        rgb_color_code_values.append(int(code_value))
    red_code_value, green_code_value, blue_code_value = rgb_color_code_values
    print(f"rgb({red_code_value}, {green_code_value}, {blue_code_value})", " in hexadecimal code is ", rgb(red_code_value, green_code_value, blue_code_value))


main()