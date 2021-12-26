"""
Modelling a graph
"""
from collections import namedtuple


# function to create the adjacency list representation of the graph
def create_adjacency_list(graph):
    # creating the dictionary to hold the node-edge relationships
    adjacency_dictionary = {node: [] for node in graph.nodes}

    # Making the adjacency list to establish the relationships using a for loop
    for edge in graph.edges:
        # Creating two variables to hold the edges
        edge_one, edge_two = edge[0], edge[1]

        # Adding each acquired node to the list of the necessary node
        if edge_two not in adjacency_dictionary[edge_one]:
            adjacency_dictionary[edge_one].append(edge_two)
    return adjacency_dictionary


# function to perform a depth first traversal through the graph
def depth_first_traversal(graph_adjacency_list, starting_node):
    # using a stack(list in python) for the implementation
    stack = [starting_node]

    # using a while loop to generate the result of the traversing
    while len(stack) > 0:
        # popping the last element of the stack and storing it as the current_node
        current_node = stack.pop()

        # printing the current_node to the console
        print(current_node)

        # using a for to aid in visiting all the neighbours of the current_node
        for neighbour_node in graph_adjacency_list[current_node]:
            # pushing the neighbours of the current_node into the stack
            stack.append(neighbour_node)


# Creating a graph template using a namedtuple
Graph = namedtuple('Graph', ['nodes', 'edges'])

# Creating a list of the nodes of the graph
graph_nodes = ['f', 'g', 'h', 'i', 'j', 'k']

# Creating a list of the edges of the graph
graph_edges = [('f', 'g'), ('f', 'i'), ('g', 'h'), ('i', 'k'), ('j', 'i'), ('i', 'g')]

# Creating a instance of the graph class
created_graph = Graph(graph_nodes, graph_edges)

# Printing the adjacency list of the created graph
print(create_adjacency_list(created_graph))

# Obtaining the results of the depth first traversal
depth_first_traversal(create_adjacency_list(created_graph), 'g')