"""
This is a program the uses the euclid's algorithm to determine the greatest common divisor of two given numbers
"""


# the function that implements the algorithm
def greatest_common_divisor(lower_number, upper_number):
    if upper_number % lower_number == 0:
        return lower_number
    else:
        return greatest_common_divisor(upper_number % lower_number, lower_number)


# the main function
def main():
    print(greatest_common_divisor(100278, 820))


main()