from copy import copy


def f(i, j, array):
    helper_array = copy(array) 
    replacer = (2 ** 25) - 1
    for index in range(i-1, j):
        helper_array[index] = replacer
    bitwise_sum_of_elements_of_array = helper_array[0]
    for index in range(1, len(helper_array)):
        bitwise_sum_of_elements_of_array &= helper_array[index]
    return bitwise_sum_of_elements_of_array


A = [1, 2, 3, 4]

actual_sum = -1 * f(1, len(A), A)
for first_index in range(len(A)):
    for second_index in range(first_index, len(A) + 1):
        actual_sum += f(first_index + 1, second_index, A)
print(actual_sum)
