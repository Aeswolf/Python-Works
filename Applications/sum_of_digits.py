from functools import reduce

"""
This is a program that permits the user to enter two numbers.
Within the range of the numbers, the program returns a list of numbers which when raised to consecutive numbers based
index and summed equals the number itself.
"""


# A function which returns the required list
def sum_of_digits(first_number, second_number):
    # a return statement to return the required list through list comprehension
    return [number for number in range(first_number, second_number + 1) if number == _sum(number)]


# a function which calculates the sum of the digits
def _sum(number):
    number_list = str(number)
    s = 0
    for index, element in enumerate(number_list):
        print("element =>", element)
        s += (int(element)) ** (index + 1)
    return s


# the main function
def main():
    first_number = int(input("Enter the first number : "))
    second_number = int(input("Enter the second number : "))
    print(sum_of_digits(first_number, second_number))


# calling the main function
main()
