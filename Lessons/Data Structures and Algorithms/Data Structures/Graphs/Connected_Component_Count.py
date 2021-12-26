"""
This program aids to count the number separately connected components in a given graph
To achieve this, i employ a variable called count whose value increases by one after a traversal is completed
I will employ the depth first traversal algorithm for the traversal
"""

from collections import namedtuple


# a function to count the  number of connected components
def count_connected_components(nodes, adjacency_list_of_graph):
    global nodes_visited

    # making the nodes_visited an empty set
    nodes_visited = set()

    # creating the variable count to count the number of connected components
    count = 0

    # for loop to iterate through each node
    for node in nodes:
        # making a traversal through the graph using the node at hand as the starting node and
        # incrementing the count variable
        if node not in nodes_visited:
            count += depth_first_traversal(adjacency_list_of_graph, node, nodes_visited)

    # returning the number of connected components
    return count


# a function to traverse through the nodes of the graph using the depth of the node
def depth_first_traversal(graph_adjacency_list, starting_node, visited_nodes=None):
    # creating a stack using the list in python and initializing it with the starting_node
    stack = [starting_node]

    # Handling the visited nodes if it empty
    if visited_nodes is None:
        visited_nodes = set()

    # creating the variable count to count the number of connected components
    count = 0

    # using a while loop to traverse the graph
    while len(stack) != 0:
        # popping the last element in the graph and assigning it to a variable called current_node
        current_node = stack.pop()

        # adding the current_node to the stack once popped
        visited_nodes.add(current_node)

        # Print each popped node
        print("current node => ", current_node)
        print("visited node => ", visited_nodes)

        # using a for loop to access the neighbour nodes of the current_node
        for neighbour_node in graph_adjacency_list[current_node]:
            # if the neighbour_node has not already been visited, add it to the stack
            if neighbour_node not in visited_nodes:
                stack.append(neighbour_node)

    count += 1
    return count


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


# Creating a graph template
Graph = namedtuple('Graph', ['nodes', 'edges'])

# a list to hold all the nodes present in the graph
graph_nodes = [1, 2, 3, 4, 5, 6, 7, 8]

# a list to hold all the edges(relationships amongst nodes) of the graph
graph_edges = [(1, 2), (4, 6), (5, 6), (6, 7)]

# Creating an instance of the graph class and passing the necessary nodes and edges
graph_instance = Graph(graph_nodes, graph_edges)

# Printing the adjacency_list representation of the graph
print(create_adjacency_list(graph_instance))

# Observing the depth first traversal
depth_first_traversal(create_adjacency_list(graph_instance), 6)

# checking the result
print(count_connected_components(graph_nodes, create_adjacency_list(graph_instance)))