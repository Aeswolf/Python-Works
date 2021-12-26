class Node:
    """
    The node class for creating the nodes of the doubly linked list. Each node consists of a
    node data, the reference to the next node in the list and the reference to the node before it in the list
    """
    # The node_data variable for storing the data of the node
    node_data = None

    # The next_node_reference variable for holding the address or reference of the next node
    next_node_reference = None

    # The previous_node_reference variable for holding the address or the reference of the previous node
    previous_node_reference = None

    # The init method for creating instances of the Node class
    def __init__(self, data):
        self.node_data = data

    # The repr method for providing a better string representation of the node
    def __repr__(self):
        return f"<class 'Node' : Data -> {self.node_data}, Previous Node -> {self.previous_node_reference}, Next Node -> {self.next_node_reference}>"


class DoublyLinkedList:
    """
    This is a blueprint for the doubly linked list
    """
    # The init method for creating instances of the doubly linked list
    def __init__(self):
        # Creating a head node of the doubly linked list and setting its value to None in order to create an empty
        # linked list
        self.head = None

    # The prepend method for adding data to the linked list
    def prepend(self, data):
        # Creating a new node for the data to be added
        new_node = Node(data)

        # Setting the current list head to the variable current_head_node
        current_head_node = self.head

        # Setting the new node's next node reference to the current head node
        new_node.next_node_reference = current_head_node

        # An if statement to link the current head node's previous reference to the new head
        if current_head_node is not None:
            current_head_node.previous_node_reference = new_node

        # Setting the new node as the head of the list
        self.head = new_node

    # Checking if the list is empty
    def is_empty(self):
        return self.head is None

    # The append method to aid add data at the end of the list
    def append(self, data):
        # Checking if the list is empty
        if self.head is None:
            self.prepend(data)
        else:
            # Creating a new node for the data to added
            new_node = Node(data)

            # Setting the head node of the list to a variable called current_node
            current_node = self.head

            # Using a while to traverse through the current list to identify the current tail node
            while current_node.next_node_reference is not None:
                # Setting the current node in the list to the next node in the list
                current_node = current_node.next_node_reference
            # setting the current node's next node reference  to the new node
            current_node.next_node_reference = new_node

            # setting the new node's next node reference to None
            new_node.next_node_reference = None

            # setting the new node's previous node reference to the current node
            new_node.previous_node_reference = current_node

    # The size method to return the number of nodes present in the list
    def size(self):
        # Variable count to keep track of the number of nodes in the list
        count = 0

        # setting the current head node of the list to the variable current_head
        current_head = self.head

        # while loop to traverse through the list to count each node in the list
        while current_head:
            # Incrementing the count variable
            count += 1
            # setting the current_head to the next node in the list
            current_head = current_head.next_node_reference
        return count

    # The search method for searching for a specific data within the linked list
    def search(self, data):
        # Setting the head node to a variable called current_node
        current_head = self.head

        # Variable search_content to house all the found nodes with the data passed
        search_content = []

        # Variable position to hold the position of the node while searching
        position = 0

        # search_content_positions to hold all the position of the found node
        search_content_positions = []

        # while loop to traverse through the list until the required node is found or not
        while current_head:
            # Incrementing the position variable
            position += 1
            # if statement to check if the required node has been located
            if current_head.node_data == data:
                search_content.append(current_head)
                search_content_positions.append(position)

            # setting the current node to the next node in the list
            current_head = current_head.next_node_reference
        if len(search_content) == 0:
            return None

        # list variable to hold all the paired results
        resulting_list = []

        for index in zip(search_content_positions, search_content):
            resulting_list.append(index)
        return resulting_list

    # Checking if the index for an insertion is valid or invalid
    def valid_index(self, index):
        return 0 <= index <= self.size() + 1

    # The insert method for inserting a node at any given point in the list
    def insert(self, index, data):

        # Checking the validity of the index passed
        if self.valid_index(index):
            # node_site_located variable to help identify the exact position where the node must be inserted
            node_site_locator = index
        else:
            raise Exception(f"Index {index} is out of bounds")

        # Making an insertion at the head of the list if the index is zero
        if index == 0:
            self.prepend(data)
        # Making an insertion at the tail of the list if the index is size() + 1
        elif index == self.size() + 1:
            self.append(data)

        else:
            # Creating a new node for the data to be added
            new_node = Node(data)

            # setting the current head node to the variable current_node
            current_node = self.head

            # while loop to  traverse through the list to identify the site where the node must be added
            while node_site_locator > 1:

                # Decreasing the node_site_locator value until reaching a node before the site of insertion
                node_site_locator -= 1

                # setting the current head node variable to the next node in the list
                current_node = current_node.next_node_reference

            # setting the new node's previous node reference to the current node reached
            new_node.previous_node_reference = current_node

            # setting the new node's next node reference to the next node reference of the current node reached
            new_node.next_node_reference = current_node.next_node_reference

            # setting the current node's next node reference to point to the new node
            current_node.next_node_reference = new_node

            # setting the current node's next node reference's previous node reference to the new node
            current_node.next_node_reference.previous_node_reference = new_node

    # The remove method for deleting nodes from the list
    def remove(self, data):
        # checking if the list is empty
        if self.is_empty():
            raise Exception("The list is empty")

        # checking if the data being removed is present in the list
        elif self.search(data) is None:
            raise Exception(f"{data} is not present in the list {self.__repr__()}")

        # handling the removal of the data when present
        else:
            # setting the current head node to the variable current_head
            current_head = self.head

            # while loop to traverse through the list to identify the node to be removed
            while current_head.next_node_reference.node_data != data:
                # setting the current node to the current_head variable
                current_head = current_head.next_node_reference

    # The repr method to provide a better string representation of the doubly linked list class
    def __repr__(self):
        # Setting the current head node to a variable called current_node
        current_node = self.head
        # A variable nodes to hold all the nodes in the list
        nodes = []

        # node_position variable to indicate each node position
        node_position = 0

        # While loop to traverse through the list
        while current_node:
            # Incrementing the node_position
            node_position += 1

            # Checking if the current node of the list is the head node

            if current_node is self.head:
                nodes.append(f"[Head node (Node {node_position}) : {current_node.node_data}]")

            # Checking if the current node of the list is the tail node
            elif current_node.next_node_reference is None:
                nodes.append(f"[Tail node(Node {node_position}) : {current_node.node_data}]")

            # else if the node is just a node in the list
            else:
                nodes.append(f"[Node {node_position} : {current_node.node_data}]")

            # Setting the current node to the next node in the list
            current_node = current_node.next_node_reference
        return " <=> ".join(nodes)


N = Node(500)
print(N)
N.next_node_reference = Node(300)
N.previous_node_reference = Node(900)
print(N)
print(".....................................................")
new_list = DoublyLinkedList()
print(new_list)
new_list.prepend(40)
print(new_list)
new_list.prepend(50)
print(new_list)
new_list.append(20)
new_list.insert(4, 35)
print(new_list.__repr__())



































































































































































































































































































































































































































































































