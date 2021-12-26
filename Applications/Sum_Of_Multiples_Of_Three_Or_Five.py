"""
This is a program that print the sum of the all the multiples of three or five below a specified range
"""


# function to return the sum of the multiples of three or five below a specified range
def sum_of_multiples_of_three_or_five(specified_range):
    # variable sum_of_multiples to hold the required sum
    sum_of_multiples = 0

    # for loop to identify all the multiples of five or three
    for _ in range(specified_range):
        if _ % 3 == 0 or _ % 5 == 0:
            print("Multiple => ", _)
            sum_of_multiples += _

    return sum_of_multiples


print("Sum of multiples <=> ", sum_of_multiples_of_three_or_five(1000))