"""
This program determines the shortest path that an individual can take to exist a maze
"""

from collections import deque

global nodes_visited

# setting the nodes_visited to an empty set
nodes_visited = set()


# function to identify the shortest path
def find_shortest_path(grid_matrix):
    count = 0
    for row_ in range(len(grid_matrix)):
        for column_ in range(len(grid_matrix[0])):
            count += breadth_first_traversal(grid_matrix, row_, column_, nodes_visited, 0)
    return count


# function to traverse through the grid using breadth first traversal
def breadth_first_traversal(grid_matrix, row_, column_, visited_nodes, count):
    boundary_for_row = 0 <= row_ < len(grid_matrix)
    boundary_for_column = 0 <= column_ < len(grid_matrix[0])
    cell_position = (row_, column_)

    if cell_position not in visited_nodes or (grid_matrix[row_][column_] != 'P' or (row_ not in boundary_for_row or column_ not in boundary_for_column)):
        return False

    visited_nodes.add(cell_position)
    count += 1

    breadth_first_traversal(grid_matrix, row_, column_ + 1, visited_nodes, count)
    breadth_first_traversal(grid_matrix, row_, column_ - 1, visited_nodes, count)
    breadth_first_traversal(grid_matrix, row_ + 1, column_, visited_nodes, count)

    return count


# Grid to represent the maze
grid = [
    ['P', 'P', 'B', 'B', 'B'],
    ['B', 'P', 'P', 'P', 'B'],
    ['P', 'P', 'B', 'P', 'P'],
    ['P', 'B', 'B', 'B', 'P'],
    ['P', 'P', 'P', 'B', 'P'],
    ['B', 'B', 'P', 'B', 'P'],
    ['B', 'P', 'P', 'B', 'P'],
    ['B', 'B', 'P', 'P', 'P']
]

for row in range(len(grid)):
    for column in range(len(grid[0])):
        print(grid[row][column], end='              ')
    print()

print(find_shortest_path(grid))