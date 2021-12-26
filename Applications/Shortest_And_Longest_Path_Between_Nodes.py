"""
This program is to determine the shortest and longest possible path that exist between two nodes in a directed cyclic
graph considering the nodes
To determine the shortest possible path between the nodes of the graph, a breadth first traversal will be employed using
queues
To determine the longest possible path between the nodes of the graph, a depth first traversal will be employed using a
stack
The iterative will be used to traverse through the nodes instead of the recursive method
"""

# importing the namedtuple and deque packages
from collections import namedtuple, deque

# Creating a global variable nodes_visited to help prevents infinite loop in the traversal
nodes_visited = set()


# function to return the adjacency list representation of a given graph
def adjacency_list_representation(graph):
    """
    :param graph:
    :return: a dictionary that shows the connected nodes of the graph
    """
    # the adjacency_dictionary variable to hold all the relationships of the nodes
    # A dictionary comprehension is used to provide a key and value pair for the dictionary
    # for each node present in the graph, an empty list is provided which later will house all the nodes
    # the node is connected to
    adjacency_dictionary = {node: [] for node in graph.nodes}

    # adding the connected nodes to the respective node according the edges
    for edge in graph.edges:
        adjacency_dictionary[edge[0]].append(edge[1])

    return adjacency_dictionary


# function to determine the longest path between two given nodes
def longest_path_between_nodes(graph_adjacency_list, starting_node, destination_node, visited_nodes):
    """
    :param graph_adjacency_list:
    :param starting_node:
    :param destination_node:
    :param visited_nodes: prevents cyclic traversals
    :return: the longest distance between the starting node and the destination node
    """
    # Emptying the visited nodes if it has values
    visited_nodes.clear()

    # Creating a stack to store the nodes involved in the traversal and initializing it with a tuple containing the
    # starting node and the distance covered
    stack = [(starting_node, 1)]

    # while loop for the traversal through the nodes
    while len(stack) != 0:

        # Popping the last element of the stack and unpacking the contents to the variables current_node
        # and distance_covered
        current_node, distance_covered = stack.pop()

        print(f"{current_node}", end=' ')
        # Checking if the current_node is the destination node and returning the distance covered so far
        if current_node == destination_node:
            return distance_covered

        # if not add the current node to the visited_node and check for it's neighbours
        visited_nodes.add(current_node)

        # Accessing the neighbours of the current node using a for loop
        for neighbour_node in graph_adjacency_list[current_node]:
            # Ensuring that the neighbour node has not been visited thereby preventing cyclic traversals
            # Hence adding the neighbour node to the stack t be traversed
            stack.append((neighbour_node, distance_covered + 1))

    # returning -1 in the case a path is not found
    return -1


# function to determine the shortest path between two given nodes
def shortest_path_between_nodes(graph_adjacency_list, starting_node, destination_node, visited_nodes):
    """
    :param graph_adjacency_list:
    :param starting_node:
    :param destination_node:
    :param visited_nodes: prevents the cyclic traversal
    :return: the shortest possible distance that exist between the starting node and the destination node
    """

    # Emptying the visited nodes before usage if values exist in it
    visited_nodes.clear()

    # creating a queue to hold the nodes for the breadth first traversal
    queue = deque()

    # Initializing the queue with a tuple pair of the starting node and the distance covered
    # Since the distance being calculated for depends on the nodes present, the starting node attains a distance of 1
    queue.append((starting_node, 1))

    # using a while loop to traverse through the nodes
    while len(queue) != 0:
        # Remove the node-distance from the queue and unpack it to the variables current_node and distance_covered
        current_node, distance_covered = queue.popleft()

        print(current_node, end=' ')

        # Checking if the current_node is the destination node and hence returning the distance upon reaching it
        if current_node == destination_node:
            return distance_covered

        # If not, add the node to the visited nodes and check if any of it's neighbours is the destination node
        visited_nodes.add(current_node)

        # Using a for loop to access the neighbours of the current node
        for neighbour_node in graph_adjacency_list[current_node]:
            # Adding only unvisited neighbour nodes to the queue
            if neighbour_node not in visited_nodes:
                queue.append((neighbour_node, distance_covered + 1))

    # returning -1 if node path exist
    return -1


# creating a graph template using the namedtuple
Graph = namedtuple('Graph', ['nodes', 'edges'])

# a list housing all the nodes of the graph
nodes_of_graph = [0, 1, 2, 3, 4, 5, 6]

# a list housing all the edges(connection between the nodes) of the graph
edges_of_graph = [(0, 2), (0, 1), (2, 1), (1, 3), (3, 2), (2, 5), (5, 3), (5, 4), (4, 2), (4, 6), (5, 6)]

# creating an instance of the graph class
graph_instance = Graph(nodes_of_graph, edges_of_graph)

# Printing the adjacency list representation for the graph
print(adjacency_list_representation(graph_instance))

# Accepting input from the user
s_node = int(input("Enter the starting node for the path trace : "))
d_node = int(input("Enter the destination node for the path trace : "))

# Printing the shortest possible path between nodes entered by the user
print(f"\nShortest path between {s_node} and {d_node} has {shortest_path_between_nodes(adjacency_list_representation(graph_instance), s_node, d_node, nodes_visited)} nodes")

print()

# printing the longest possible path between the nodes entered by the user
print(f"\nLongest path between {s_node} and {d_node} has {longest_path_between_nodes(adjacency_list_representation(graph_instance), s_node, d_node, nodes_visited)} nodes")