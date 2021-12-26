"""
This program aids to count the number separately connected components in a given graph
To achieve this, i employ a variable called count whose value increases by one after a traversal is completed
I will employ the depth first traversal algorithm for the traversal
"""

from collections import namedtuple


# a function to count the  number of connected components
def count_connected_components(adjacency_list_of_graph):
    global nodes_visited

    # setting the nodes_visited to an empty set
    nodes_visited = set()

    # setting the variable count to 0
    count = 0

    # using the for loop to access each node in the adjacency list
    for node in adjacency_list_of_graph.keys():
        # making the call to the recursive depth first traversal function
        if recursive_depth_first_traversal(adjacency_list_of_graph, node, nodes_visited) is True:
            # incrementing the count variable
            count += 1

    return f"Components counted => {count}"


# a function to create an adjacency list of the various node relationships
def create_adjacency_list(graph):
    """
    :param graph:
    :return: a dictionary laying out all the various relations between the individual nodes
    """
    # adjacency_dictionary variable to hold the various node relations
    adjacency_dictionary = {node: [] for node in graph.nodes}

    # using each edge and a for loop to express the relations between each node
    for edge in graph.edges:
        # creating the list relations
        adjacency_dictionary[edge[0]].append(edge[1])
        adjacency_dictionary[edge[1]].append(edge[0])

    # returning the adjacency list
    return adjacency_dictionary


# a function for the recursive traversal
def recursive_depth_first_traversal(graph_adjacency_list, starting_node, visited_nodes):
    # Printing the current node of the graph
    print(starting_node)

    # An if statement to check whether the current node is present in the nodes visited list
    if starting_node in visited_nodes:
        return False

    # if not, add the current node to the nodes visited list
    visited_nodes.add(starting_node)

    # accessing the neighbours of the current node
    for neighbour_node in graph_adjacency_list[starting_node]:
        # calling the function recursively
        recursive_depth_first_traversal(graph_adjacency_list, neighbour_node, visited_nodes)

    return True


# Creating a graph template
Graph = namedtuple('Graph', ['nodes', 'edges'])

# a list to hold all the nodes present in the graph
graph_nodes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# a list to hold all the edges(relationships amongst nodes) of the graph
graph_edges = [(1, 2), (4, 6), (5, 6), (6, 7), (7, 8), (7, 9)]

# Creating an instance of the graph class and passing the necessary nodes and edges
graph_instance = Graph(graph_nodes, graph_edges)

print(count_connected_components(create_adjacency_list(graph_instance)))