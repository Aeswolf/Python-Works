"""
This file is to aid understand the implementation of the konigsberg graph
In this file a graph data structure is represented using the namedtuple module from the collections module
"""

from collections import namedtuple


# A function to provide the adjacency matrix for the konigsberg graph
def adjacency_matrix(graph_instance):
    # Creating a multidimensional matrix for the result
    resulting_matrix = [[0 for node in graph_instance.nodes] for node in graph_instance.nodes]
    # for loop for adding 1 to an element in the list where necessary
    for edge in graph_instance.edges:
        # Creating two indices for the each element of the multidimensional matrix
        index_one, index_two = edge[0], edge[1]
        resulting_matrix[index_one][index_two] += 1
        resulting_matrix[index_two][index_one] += 1
    return resulting_matrix


# A function to provide the adjacency list for the konigsberg graph
def adjacency_list(graph_instance):
    """
    :param graph_instance:
    :return: a dictionary representation of the edges of the graph
    """
    # Creating a dictionary whose keys are the nodes in the graph to be passed
    adjacency_dictionary = {node: [] for node in graph_instance.nodes}
    # for loop to help assign each node in the graph with corresponding connection
    for edge in graph_instance.edges:
        # Creating two keys to help map each node in the graph
        key_one, key_two = edge[0], edge[1]
        adjacency_dictionary[key_one].append(key_two)
        adjacency_dictionary[key_two].append(key_one)
    return adjacency_dictionary


# Creating a Graph blueprint using namedtuple
Graph = namedtuple("Graph", ["nodes", "edges"])

# Creating the nodes involved in this graph
nodes = ["A", "B", "C", "D"]

# Creating the edges of the graph
edges = [("A", "B"), ("A", "B"), ("A", "C"), ("A", "C"), ("A", "D"), ("B", "D"), ("C", "D")]

# Creating an instance of the Graph namedtuple
graph = Graph(nodes, edges)

# calling the adjacency_list function
print(adjacency_list(graph))

# Printing the graph
print(graph)

# Creating a node made up of integers
integer_nodes = range(4)

# Creating the edges for the integer nodes
integer_edges = [(0, 1), (0, 1), (0, 2), (0, 2), (0, 3), (1, 3), (2, 3)]

# Creating a graph for the integer nodes
graph_integer = Graph(integer_nodes, integer_edges)

# calling the adjacency_matrix
print(adjacency_matrix(graph_integer))
