"""
This is a program that converts any positive value passed to the binary format
"""


def convert_to_binary(value):
    """
    :param value:
    :return: the binary format of the value passed
    """
    binary_value = ""
    count = 0
    while value != 0:
        binary_value += str(value % 2)
        count += 1
        value //= 2
    return int(binary_value[::-1]), count


print(convert_to_binary(6463598))

