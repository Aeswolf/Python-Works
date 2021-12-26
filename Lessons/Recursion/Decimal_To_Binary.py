# function to aid convert a decimal number to a binary number
def decimal_to_binary_converter(decimal_number):
    """
    :param decimal_number: the decimal number to be converted
    :return: the binary format of the number
    """

    # base case
    if decimal_number == 0:
        return ""

    return decimal_to_binary_converter(decimal_number // 2) + str(decimal_number % 2)


print(decimal_to_binary_converter(1000000000000000000000000000000000000000333333))

