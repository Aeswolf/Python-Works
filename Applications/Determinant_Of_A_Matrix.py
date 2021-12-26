"""
this is a program that calculates the determinant of a given square matrix.
"""


# function to calculate the determinant of square matrix
def calculate_determinant(matrix):
    """
    :param matrix: the matrix whose determinant is to be determined
    :return: the determinant of the matrix passed
    """

    # determinant to store the result
    determinant = 0

    # for loop to estimate the determinant of the matrix passed to the function
    for _ in range(len(matrix)):
        determinant += ((-1) ** (0 + _)) * (matrix[0][_] * determinant_of_two_by_two_matrix(pick_up_array(matrix, 0, _)))

    return determinant


# function to evaluate the determinant of a 2 x 2 matrix
def determinant_of_two_by_two_matrix(matrix):
    """
    :param matrix: the subdivided matrix whose determinant is to be evaluated
    :return: the determinant of a 2 x 2 matrix passed or subdivided matrix whose subdivided matrix is a 2 x 2 matrix
    """
    # checking if the matrix passed is a 2 x 2 matrix
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

    return calculate_determinant(matrix)


# function to pick up the necessary elements for the calculation from the matrix
def pick_up_array(matrix, current_row, current_column):
    # the 2D array to hold the 2 x 2 matrix being picked up
    two_d_array = []

    # the 1D array for storing each row of the matrix being picked up
    sub_array = []

    # nested for loop to aid with the elements to be picked up
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if row == current_row or column == current_column:
                continue
            sub_array.append(matrix[row][column])
        if sub_array != [] and sub_array not in two_d_array:
            two_d_array.append(sub_array)
            sub_array = []

    return two_d_array


print("The determinant of the matrix is", calculate_determinant([[1, 0, 0, 1], [0, 1, 0, 1], [0, 0, 1, 1], [1, 0, 1, 0]]))