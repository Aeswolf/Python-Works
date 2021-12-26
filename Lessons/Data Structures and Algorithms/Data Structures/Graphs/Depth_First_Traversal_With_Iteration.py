"""
This program houses the depth first traversal implementation using iteration for both directed and undirected graphs
This program uses a stack for the traversal of the nodes
"""

from collections import namedtuple
global nodes_visited

# setting the nodes_visited to an empty set
nodes_visited = set()


# Function to determine if a path exist between two given nodes
def path_exist(graph_adjacency_list, starting_node, destination_node, visited_nodes):
    # Creating a stack and making the starting node it's first element
    stack = [starting_node]

    # using a while loop to traverse through the graph
    while len(stack) != 0:
        # Popping the last element of the stack to the variable current_node
        current_node = stack.pop()

        # Printing the path for visualization
        print(current_node, end=' => ')

        # Adding a popped node to the visited nodes
        visited_nodes.add(current_node)

        # checking if the current node is the destination node
        if current_node == destination_node:
            print("Comment : ", end='')
            return True

        # using a for loop to access the neighbour nodes of the current node should in case the current node is
        # not the destination node
        for neighbour_node in graph_adjacency_list[current_node]:
            # adding a neighbour node to the stack so far as the node has not been visited
            if neighbour_node not in visited_nodes:
                stack.append(neighbour_node)

    # returning false if no path exists
    print("Comment : ", end='')
    return False


# Function to traverse through the graph provided a starting node
def depth_first_traversal_with_iteration(graph_adjacency_list, starting_node, visited_nodes):
    # Creating a stack using a list with the starting node as it's element
    stack = [starting_node]

    # using a while loop for the traversal
    while len(stack) != 0:
        # Pop the last element of the stack to the variable current_node
        current_node = stack.pop()

        # Once a node has been popped, it implies it has been visited and hence put it in the visited nodes
        visited_nodes.add(current_node)

        # Print the current_node
        print(f"Current node -> {current_node}")

        # Accessing the neighbour nodes of the current node
        for neighbour_node in graph_adjacency_list[current_node]:
            # Push the neighbour node to the stack to be accessed later if it not been visited
            if neighbour_node not in visited_nodes:
                stack.append(neighbour_node)


# Function to develop an adjacency list of the graph
def create_adjacency_list(graph):
    # the adjacency dictionary variable to house the relationships
    adjacency_dictionary = {node: [] for node in graph.nodes}

    # a for loop to establish the relationships using the edges
    for edge in graph.edges:
        # appending the necessary nodes to obtain the adjacency list
        adjacency_dictionary[edge[0]].append(edge[1])

    # returning the adjacency dictionary
    return adjacency_dictionary


# Creating a template or blueprint for the graph class
Graph = namedtuple('Graph', ['nodes', 'edges'])

# list holding the nodes of a directed graph
nodes_of_a_directed_graph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

# list holding the connections(edges) between the various nodes of the directed graph
edges_of_a_directed_graph = [('E', 'A'), ('B', 'C'), ('A', 'D'), ('B', 'F'), ('C', 'F'), ('D', 'B'), ('D', 'H'),
                            ('E', 'G'), ('E', 'H'), ('A', 'B'), ('E', 'B'), ('F', 'E'), ('G', 'D'), ('H', 'F'),
                             ('H', 'G')]

# Creating an instance of the graph class
directed_cyclic_graph = Graph(nodes_of_a_directed_graph, edges_of_a_directed_graph)

# Printing the adjacency list representation of the graph
print(create_adjacency_list(directed_cyclic_graph))

#  Traversing through the graph using the depth first traversal
# depth_first_traversal_with_iteration(create_adjacency_list(directed_cyclic_graph), 'G', nodes_visited)

# checking if a path exist between certain nodes
print(path_exist(create_adjacency_list(directed_cyclic_graph), 'E', 'C', nodes_visited))
