"""
This program calculates the number of possible ways by which a traveller can move from the corner of a m x n matrix to
the bottom right corner of the matrix
"""


# function to cunt the number of ways one can move on the grid
def number_of_ways_to_travel_grid(number_of_rows, number_of_columns, memo=None):
    if memo is None:
        memo = dict()

    number_tuple = (number_of_rows, number_of_columns)
    # base cases
    if number_tuple in memo.keys():
        return memo[number_tuple]

    if number_of_columns == 0 or number_of_rows == 0:
        return 0

    if number_of_columns == 1 and number_of_rows == number_of_columns:
        return 1

    memo[number_tuple] = number_of_ways_to_travel_grid(number_of_rows - 1, number_of_columns, memo) + number_of_ways_to_travel_grid(number_of_rows, number_of_columns - 1, memo)

    print(memo)

    return memo[number_tuple]


print(number_of_ways_to_travel_grid(4, 15))