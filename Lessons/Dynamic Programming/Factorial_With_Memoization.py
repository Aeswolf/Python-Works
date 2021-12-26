"""
This is a program that evaluates the factorial of a given number
"""


# function to determine the factorial of a given number
def factorial_of(number, memo=None):
    """
    :param number: the number whose factorial is to be determined`
    :param memo: a dictionary to hold the already determined factorials
    :return: the factorial of a given number
    """
    # if the memo parameter is none, set it to an empty dictionary
    if memo is None:
        memo = dict()

    if number in memo.keys():
        return memo[number]

    if 0 <= number <= 1:
        return 1

    memo[number] = number * factorial_of(number - 1, memo)

    return memo[number]


print(factorial_of(9))