"""
This file provides an implementation and understanding of regular expressions in python
A regular expression is a special text string that describes a search pattern
To use regular expressions in python, you must import the  re module
"""


def add_number(string):
    length_of_string = len(string)
    split_string = [letter for letter in string]
    count_numeric_strings = 0
    for letter in split_string:
        if letter.isnumeric():
            count_numeric_strings += 1
    difference = length_of_string - count_numeric_strings
    number_list = split_string[count_numeric_strings - 2:count_numeric_strings + 1]
    if count_numeric_strings >= 1:
        value = str(int("".join(split_string[difference:])) + 1)
        split_string = split_string[:difference]
        split_string.append(value)
    else:
        split_string.append(str(1))
    return "".join(split_string)


print(add_number("Hello099"))
