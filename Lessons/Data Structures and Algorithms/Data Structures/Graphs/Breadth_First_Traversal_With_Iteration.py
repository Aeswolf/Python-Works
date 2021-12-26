"""
This is a program that traverses through a graph going through the breadth of each node first
This is achieved by using a queue to traverse through the graph
"""
from collections import namedtuple


# template for the queue to be used using a list
class Queue:
    # the init function to create an empty queue
    def __init__(self):
        # setting the queue to an empty list
        self.queue = []

    # the is_empty function to check if the queue is empty or not
    def is_empty(self):
        return len(self.queue) == 0

    # the size function to return the number of elements in the queue
    def size(self):
        return len(self.queue)

    # the enqueue function to add elements to the queue
    def enqueue(self, element):
        self.queue.append(element)

    # the dequeue function to remove elements from the front of the queue
    def dequeue(self):
        # setting the first element of the queue to the variable first_element
        first_element = self.queue[0]

        # shifting the elements in the queue using slicing
        self.queue = self.queue[1:]

        # returning the first element of the queue
        return first_element


# the create adjacency list function to create an adjacency list representation of the graph
def create_adjacency_list(graph):
    # the adjacency dictionary to show the relationship between the nodes
    adjacency_dictionary = {node: [] for node in graph.nodes}

    # establishing the relationship represented by the edges using a for loop
    for edge in graph.edges:
        # creating the necessary adjacency list
        adjacency_dictionary[edge[0]].append(edge[1])

    # returning the adjacency dictionary
    return adjacency_dictionary


# the breadth first traversal function to traverse through the nodes of the graph considering the breadth of
# each node first
def breadth_first_traversal(graph_adjacency_list, starting_node):
    # creating a queue and initializing it the starting node
    queue = Queue()
    queue.enqueue(starting_node)

    # using a while loop to traverse through the graph
    while not queue.is_empty():
        # removing the first element of the queue and setting it to the variable current_node
        current_node = queue.dequeue()

        # Printing the element removed from the queue
        print(current_node)

        # accessing the neighbours of the current node using a for loop
        for neighbour_node in graph_adjacency_list[current_node]:
            # adding the neighbour node to the queue
            queue.enqueue(neighbour_node)


# Using namedtuple to create a template for the Graph
Graph = namedtuple('Graph', ['nodes', 'edges'])

# the nodes of the directed graph
nodes_of_the_directed_graph = ['A', 'B', 'C', 'D', 'E', 'F']

# the connection(edges) between the various nodes of the directed graph
edges_of_the_directed_graph = [('B', 'A'), ('A', 'D'), ('B', 'C'), ('D', 'C'), ('C', 'F'), ('C', 'E')]

# creating an instance of the graph class
graph_instance = Graph(nodes_of_the_directed_graph, edges_of_the_directed_graph)

# Printing the adjacency list representation of the graph
print(create_adjacency_list(graph_instance))

# testing the traversal
breadth_first_traversal(create_adjacency_list(graph_instance), 'F')