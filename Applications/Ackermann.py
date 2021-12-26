"""
This is a program that utilizes the Ackermann function to obtain a list of numbers
"""


# the ackermann function
def ackermann_function(lower_limit=0, upper_limit=0, memo=None):
    if memo is None:
        memo = dict()

    if (lower_limit, upper_limit) in memo.keys():
        return memo[(lower_limit, upper_limit)]

    if lower_limit == 0:
        return upper_limit + 1

    elif lower_limit > 0 and upper_limit == 0:
        memo[(lower_limit, upper_limit)] = ackermann_function(lower_limit - 1, 1, memo)

    elif lower_limit > 0 and upper_limit > 0:
        memo[(lower_limit, upper_limit)] = ackermann_function(lower_limit - 1, ackermann_function(lower_limit, upper_limit - 1), memo)

    return memo[(lower_limit, upper_limit)]


# the main function
def main():
    print(ackermann_function(3, 6))


main()
