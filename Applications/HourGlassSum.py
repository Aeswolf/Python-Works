def pickup_array(current_row, current_column, actual_array):
    """
    :param current_row: stores the value of the current row being accessed in the actual array
    :param current_column: stores the value of the current column being accessed in the actual array
    :param actual_array: stores the content of the actual array being considered
    :return: a 3 by 3 array picked from the actual array based on the current row and column in the array
    """
    # the 3 by 3 sub-array to store the values to be returned
    new_array = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # the row and column to be used to accessed each possible cell of the new array
    row_for_new_array, column_for_new_array = 0, 0

    # nested for loops to aid in the successful pick up of the correct elements in the actual array
    for new_row in range(current_row, current_row + 3):
        for new_column in range(current_column, current_column + 3):
            # performing the pickup of the values
            new_array[row_for_new_array][column_for_new_array] = actual_array[new_row][new_column]
            column_for_new_array += 1
        row_for_new_array += 1
        column_for_new_array = 0
    return new_array


def hour_glass_array_sum(picked_up_array):
    sum_of_picked_up_values = 0
    for row_in_array in range(len(picked_up_array)):
        for column_in_array in range(len(picked_up_array[0])):
            if row_in_array == 1 and row_in_array != column_in_array:
                continue
            sum_of_picked_up_values += picked_up_array[row_in_array][column_in_array]
    return sum_of_picked_up_values


def evaluate(array):
    sum_of_arrays = []
    for row in range(len(array) - 2):
        for column in range(len(array[0]) - 2):
            sum_of_arrays.append(hour_glass_array_sum(pickup_array(row, column, array)))

    largest_possible_sum = sum_of_arrays[0]

    for index in range(1, len(sum_of_arrays)):
        if largest_possible_sum < sum_of_arrays[index]:
            largest_possible_sum = sum_of_arrays[index]

    return largest_possible_sum


print(evaluate([
    [0, -1, 2, 3, 4, -50],
    [-6, -7, 8, -9, 10, -11],
    [-12, -13, -14, -15, -16, 17],

    [-18, -19, -20, -21, 22, -23],
    [-24, -25, -26, -27, -28, -29],
    [-30, 31, -32, -33, 34, -35]
]))

print(evaluate([
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [-1, -2, -3, -4, -5, -6, -7, -8, -9],
    [-9, -8, -7, -6, -5, -4, -3, -2, -1],
    [2, 4, 6, 8, 10, 12, 14, 16, 18],
    [18, 16, 14, 12, 10, 8, 6, 4, 2],
    [1, 3, 5, 7, 9, 11, 13, 15, 17],
    [17, 15, 13, 11, 9, 7, 5, 3, 1],
    [5, 10, 15, 20, 25, 30, 35, 40, 45]
]))