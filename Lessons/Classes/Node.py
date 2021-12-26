class Node:
    """
    This is a blueprint for creating a Node to be used for singly linked list
    This class has two class variables namely data and the next variables.
    The data variable holds the content of the item to be stored and the next variable holds the address of the next
    node in the list
    """
    # Data variable
    data = None

    # The next variable
    next = None

    # The init method to permit the creation of an instance of the class
    def __init__(self, data):
        # Assigning the data passed for the instance of the class to the class variable
        self.data = data

    # The repr method to provide a better representation of the Node Object
    def ___repr__(self):
        return f"<class Node: Data -> {self.data} Next Reference -> {self.next}"


new_node = Node(200)
next_node = Node(-100)
new_node.next = next_node
print(new_node.___repr__())
print(new_node.next)