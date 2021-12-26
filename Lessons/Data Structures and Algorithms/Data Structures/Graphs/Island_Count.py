"""
This program counts the number of isolated cells on a grid.
These cells are denoted with the letter L to signify a land whilst the remaining cells are denoted with the letter W
 to signify water.
A depth first traversal will be employed to identify the islands
"""
global nodes_visited

nodes_visited = set()


# function to identify the islands in the grid
def count_island(grid_matrix):
    island_size = 100000
    count = 0
    for row in range(len(grid_matrix)):
        for column in range(len(grid_matrix[0])):
            count = traverse(grid_matrix, row, column, nodes_visited, 0)
            if count < island_size:
                island_size = count
    return island_size


# the depth_first traversal function to traverse through the grid
def traverse(matrix_grid, row_, column_, visited_nodes, count):
    row_boundary = 0 <= row_ < len(matrix_grid)
    column_boundary = 0 <= column_ < len(matrix_grid[0])
    cell_position = (row_, column_)
    if cell_position in visited_nodes or (not row_boundary or not column_boundary) or (
            matrix_grid[row_][column_] == 'W'):
        return False

    visited_nodes.add(cell_position)
    count += 1

    traverse(matrix_grid, row_ - 1, column_, nodes_visited, count)
    traverse(matrix_grid, row_ + 1, column_, nodes_visited, count)
    traverse(matrix_grid, row_, column_ - 1, nodes_visited, count)
    traverse(matrix_grid, row_, column_ + 1, nodes_visited, count)

    return count


# the grid representing the islands surrounded by water
grid = [
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'L', 'W', 'W', 'W'],
    ['W', 'W', 'W', 'L', 'W'],
    ['W', 'W', 'L', 'L', 'W'],
    ['L', 'W', 'W', 'L', 'L'],
    ['L', 'L', 'W', 'W', 'W']
]

print(count_island(grid))
