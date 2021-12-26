from collections import namedtuple, deque

visited_nodes = set()


def adjacency_list_representation(graph_instance):
    adjacency_list = {node: [] for node in graph_instance.nodes}

    for edge in graph_instance.edges:
        adjacency_list[edge[0]].append(edge[1])

    return adjacency_list


def depth_first_traversal(adjacency_dict, starting_node, destination_node, nodes_visited):
    stack = [starting_node]
    while len(stack) != 0:
        current_node = stack.pop()

        if current_node == destination_node:
            return True

        nodes_visited.add(current_node)

        for neighbour_node in adjacency_dict[current_node]:
            
            stack.append(neighbour_node)

    return False


Graph = namedtuple("Graph", ["nodes", "edges"])

nodes_of_graph = ["A", "B", "C", "D"]

edges_of_graph = [("A", "B"), ("A", "C"), ("C", "B"), ("C", "D"), ("B", "D"), ("D", "A")]

graph = Graph(nodes_of_graph, edges_of_graph)

print(depth_first_traversal(adjacency_list_representation(graph), "A", "B"))