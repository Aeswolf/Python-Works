"""
This is a  program that counts the number of ways by which a given number can be expressed as the sum of 1, 3, and or 4
"""


# function to determine the number of ways
def number_of_ways(number, memo=None):
    """
    :param memo: a dictionary that stores the result of already calculated number of ways using the number as key
    :param number: The number to be passed for the evaluation
    :return: the number of ways for the sums to be expressed
    """

    if memo is None:
        memo = dict()

    if number in memo.keys():
        return memo[number]

    # Base cases
    if number == 0 or number == 1 or number == 2:
        return 1

    if number == 3:
        return 2

    if number < 0:
        return 0

    memo[number] = number_of_ways(number - 1, memo) + number_of_ways(number - 3, memo) + number_of_ways(number - 4, memo)

    print(memo)

    return memo[number]


print(number_of_ways(15))