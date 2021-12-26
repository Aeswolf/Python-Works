"""
This is a program the prints the pairs of numbers for a given sum
"""


# function to print the required pairs
def pairs(arr, required_sum):
    for _ in arr:
        for __ in arr:
            if _ + __ == required_sum:
                print(f"({_}, {__})")


# alternative function to print the required pairs
def alternative_pairs(arr, required_sum):
    for _ in arr:
        required_partner = required_sum - _
        if required_partner in arr:
            print(f"({_}, {required_partner})")


arr_list = [-4, -3, -2, -10, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 100, 11]
pairs(arr_list, 12)
print("_____________________________________________")
alternative_pairs(arr_list, 12)