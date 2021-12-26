"""
This program traverse through the graph and determines which traversal has the greater number of components(nodes)
This program uses the depth first traversal for the traversing
"""
from collections import namedtuple
global nodes_visited

# setting the nodes_visited variable to an empty set
nodes_visited = set()


# largest_component function to return the greatest number of nodes involved in a certain traversal
def largest_component_in_graph(graph):
    # largest component counter
    largest_component = 0
    # considering the nodes of the graph
    for node in graph.nodes:
        number_of_nodes_in_graph_component = depth_first_traversal_with_recursion(create_adjacency_list(graph),node, nodes_visited)
        if largest_component < number_of_nodes_in_graph_component:
            largest_component = number_of_nodes_in_graph_component
    return largest_component


# the depth_first_traversal_with_recursion to traverse through the nodes of a graph
def depth_first_traversal_with_recursion(adjacency_list, starting_node, visited_nodes):

    # if the node being considered is already visited, then skip it
    if starting_node in visited_nodes:
        return 0

    # else add it to the visited nodes and consider it neighbours
    visited_nodes.add(starting_node)

    # incrementing the node_counter by one
    nodes_counter = 1

    for neighbour_node in adjacency_list[starting_node]:
        nodes_counter += depth_first_traversal_with_recursion(adjacency_list, neighbour_node, visited_nodes)

    return nodes_counter


# a create_adjacency_list to provide an adjacency list representation of the graph
def create_adjacency_list(graph):
    # the adjacency_dictionary to hold the relationships between the nodes of the graph
    adjacency_dictionary = {node: [] for node in graph.nodes}

    # establishing the relationships between the nodes using the edges and a for loop
    for edge in graph.edges:
        adjacency_dictionary[edge[0]].append(edge[1])
        adjacency_dictionary[edge[1]].append(edge[0])
    return adjacency_dictionary


# creating the template for the graph
Graph = namedtuple('Graph', ['nodes', 'edges'])

# a list to hold the nodes of the graph
nodes_of_graph = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# a list to hold all the connections (edges) between the nodes
edges_of_graph = [(0, 1), (0, 8), (0, 5), (5, 8), (2, 3), (3, 4), (2, 4), (2, 6), (3, 7)]

# creating an instance of the graph class
graph_instance = Graph(nodes_of_graph, edges_of_graph)

# printing the adjacency list for the graph
print(create_adjacency_list(graph_instance))

# print(depth_first_traversal_with_recursion(create_adjacency_list(graph_instance), 0, nodes_visited))
print(largest_component_in_graph(graph_instance))