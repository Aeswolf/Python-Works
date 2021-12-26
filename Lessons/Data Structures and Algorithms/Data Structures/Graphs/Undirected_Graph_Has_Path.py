"""
This is a program that uses both the breadth first and depth first traversal algorithms to determine if a path exist
between a given starting node and a terminal node for an undirected graph
"""

from collections import namedtuple


# function to aid create an adjacency list for the given undirected graph
def create_adjacency_list(_graph):
    """
    :param _graph:
    :return: A dictionary representing the adjacency list of the graph
    """
    # The adjacency_dictionary variable to hold the relationships between the various nodes
    adjacency_dictionary = {node: [] for node in _graph.nodes}
    # Establishing the relationships between the various nodes using a for loop
    for edge in _graph.edges:
        adjacency_dictionary[edge[0]].append(edge[1])
        adjacency_dictionary[edge[1]].append(edge[0])

    return adjacency_dictionary


# function to determine whether a path exist between a starting node and a terminal node
def has_path(graph_adjacency_list, starting_node, destination_node):
    # creating a set and assigning it to visited nodes
    visited_nodes = set()

    # creating a stack using the list and initializing it with the starting node
    stack = [starting_node]

    # a while loop that runs so far as the stack isn't empty
    # (depicting that not all the nodes of the graph have been visited)
    while len(stack) != 0:
        # pop the last element of the stack to the variable current_node
        current_node = stack.pop()

        # Adding the current node to the visited nodes
        visited_nodes.add(current_node)

        # Printing the path for relevance
        print(f"{current_node}", end=' => ')

        # checking if the current_node is the same as the destination_node implying a path exist between them
        if current_node == destination_node:
            print("Comment : ", end='')
            return True

        # if that is not the case, then visit the neighbours of the current_node and proceeds to find a path
        # this is done using a for loop
        for neighbour_node in graph_adjacency_list[current_node]:
            # Checking if the neighbour is not already visited and pushing it into the stack
            if neighbour_node not in visited_nodes:
                # pushing each neighbour of the current node to the stack
                stack.append(neighbour_node)

    # returning false should a path not be found
    print(f"\nComment : ", end='')
    return False


# Using the namedtuple to create a templated class Graph
Graph = namedtuple('Graph', ['nodes', 'edges'])

# All the nodes present in the given graph
nodes = ['f', 'g', 'h', 'i', 'j', 'k']

# All the edges(relationships between the nodes of the graph) of the given graph
edges = [('f', 'g'), ('f', 'i'), ('g', 'h'), ('g', 'i'), ('i', 'k'), ('j', 'i')]

# An instance of the class Graph with the nodes and edges as arguments
graph = Graph(nodes, edges)

# Printing the adjacency list to console
print(create_adjacency_list(graph))
print(has_path(create_adjacency_list(graph), 'k', 'h'))