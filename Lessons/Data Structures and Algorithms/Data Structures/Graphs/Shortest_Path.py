"""
This is a program that traverses through a graph going through the breadth of each node first
This is achieved by using a queue to traverse through the graph
"""
from collections import namedtuple
global nodes_visited

# setting the nodes_visited to an empty set
nodes_visited = set()


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
        adjacency_dictionary[edge[1]].append(edge[0])

    # returning the adjacency dictionary
    return adjacency_dictionary


# the breadth first traversal function to traverse through the nodes of the graph considering the breadth of
# each node first
def breadth_first_traversal(graph_adjacency_list, starting_node, destination_node):

    # creating a queue and initializing it with the starting node
    queue = Queue()
    queue.enqueue((starting_node, 0))

    # using a while loop to traverse through the graph
    while not queue.is_empty():
        # removing the first element of the queue and setting it to the variable current_node
        current_node, current_distance = queue.dequeue()

        print(f"({current_node}, {current_distance})")

        # Adding the current node to the visited nodes if not present
        nodes_visited.add(current_node)

        # checking if the current node matches the destination node
        if current_node == destination_node:
            return current_distance

        # accessing the neighbours of the current node using a for loop
        for neighbour_node in graph_adjacency_list[current_node]:
            # adding the neighbour node to the queue
            if neighbour_node not in nodes_visited:
                queue.enqueue((neighbour_node, current_distance + 1))

    return -1


# Using namedtuple to create a template for the Graph
Graph = namedtuple('Graph', ['nodes', 'edges'])

# the nodes of the directed graph
nodes_of_the_undirected_graph = ['o', 'p', 'v', 'w', 'x', 'y', 'z']

# the connection(edges) between the various nodes of the directed graph
edges_of_the_undirected_graph = [('w', 'x'), ('v', 'p'), ('p', 'o'), ('o', 'z'), ('w', 'v'), ('x', 'y'), ('y', 'z')]

# creating an instance of the graph class
graph_instance = Graph(nodes_of_the_undirected_graph, edges_of_the_undirected_graph)

# printing the adjacency list representation for the undirected graph
print(create_adjacency_list(graph_instance))

# displaying the shortest possible distance
print(breadth_first_traversal(create_adjacency_list(graph_instance), 'w', 'z'))