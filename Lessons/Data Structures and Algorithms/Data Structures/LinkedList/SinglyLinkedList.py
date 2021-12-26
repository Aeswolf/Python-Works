"""
This is an implementation of a singly linked list
This is a type of the LinkedList data structure in which the nodes point only to the reference of the node ahead of them
in the list.
Each node has only two attributes -> Data attribute(for holding the content of the item to be stored) and
next_node(to hold the reference of the next node in the list.
"""


# Blueprint for the Node class
class Node:

    # The data attribute of the class
    data_attribute = None

    # The next_node attribute to hold the reference of the next node in the list
    next_node = None

    # The init method of the class to allow for instance creation
    def __init__(self, data):
        self.data_attribute = data

    # The repr method to provide a better string representation of the Node class
    def __repr__(self):
        return f"<class \'Node\' : Data -> {self.data_attribute}, Next Node -> {self.next_node.__repr__()}>"


# Blueprint for the Singly Linked List
class SinglyLinkedList:
    # The init method of the class to allow for instance creation
    def __init__(self):
        # The head variable to hold the head node of the list.
        # The head variable is set to none to ensure every created instance is an empty list
        self.head = None

    # The is_empty method to determine whether or not a given list is empty
    def is_empty(self):
        # A list is empty if it's head node is None
        return self.head is None

    # The size method to determine the number of nodes present in the list
    def size(self):
        # Setting the head node to a variable called current_node to aid in the traversing of the list
        current_node = self.head

        # A count variable to hold the number of nodes in the list
        count = 0

        # A while loop to traverse through the list and count each present node
        while current_node:
            # Increase the value of the count variable by 1
            count += 1

            # set the current node to the next node in the list
            current_node = current_node.next_node

        return count

    # The prepend method for adding new nodes to the head of the list
    def prepend(self, data):
        # Creating a node for the data to be added to the list
        new_node = Node(data)

        # Setting the next_node attribute of the new node to the current head node
        new_node.next_node = self.head

        # Making the new node the head of the list
        self.head = new_node

    # The append method to add an item to the tail of the list
    def append(self, data):

        # Setting the current head node to current_node in order to permit the traversing from the head node
        current_node = self.head

        # boolean variable to use as condition for while loop
        loop_condition = True

        # Creating a new node for the data to be added to the list
        new_node = Node(data)

        # while loop for traversing through the list
        while loop_condition:
            # checking if the current node point to None(signifying a tail node)
            if current_node.next_node is None:
                # setting the loop condition to false in order to break the loop
                loop_condition = False

                # setting the current node's next node to the new data
                current_node.next_node = new_node

                # setting the new node's next node to None(Making it the last item in the list)
                new_node.next_node = None

            # setting the current_node to the next node in the list
            current_node = current_node.next_node

    # the insert method to add an item at any position in the list
    def insert(self, data, index):
        # Making an insertion at the head of the list
        if index == 0:
            self.prepend(data)

        # Making an insertion at any other position in the list
        else:
            # Creating a new node for the data to be added
            new_node = Node(data)

            # Assigning the current node in focus to the current_node variable
            current_node = self.head

            # Creating a variable called previous_node to hold the previous node of the new_node
            previous_node = None

            # Creating a variable to hold the location where the new_node must be inserted
            node_location = index

            # While loop to help locate the site of insertion of the node
            while node_location > 1:
                # Decreasing the node_location by one
                node_location -= 1

                # setting the current node to the next_node in the list
                current_node = current_node.next_node

            # Setting the current node to the previous_node variable
            previous_node = current_node

            # Setting the next node of the current node to the variable next_node
            next_node = current_node.next_node

            # Setting the next node of the previous node to the new node to be added
            previous_node.next_node = new_node

            # Setting the next node of the new node to the next node
            new_node.next_node = next_node

    # The search to identify the presence or absence an item in the list
    def search(self, data):
        # Setting the current node to the variable current_node
        current_node = self.head

        # Creating  a count variable to help tell the location of the node
        count = 0

        # while loop to traverse through the list in search for the item
        while current_node:
            # Incrementing the count variable by one
            count += 1
            # Checking if the current node's item equals the item being searched for
            if current_node.data_attribute == data:
                return f"Node with data {current_node.data_attribute} is occupying Node {count} in the list"

            # setting the current_node to the next node in the list
            current_node = current_node.next_node

        return None

    # The remove method to delete an item from the list
    def remove(self, data):
        # Checking if the list is empty
        if self.is_empty():
            raise Exception("The list is an empty")

        # checking if the data being removed is present in the list
        elif self.search(data) is None:
            raise Exception(f"Node with data {data} is absent in the list")

        # else if the node with the data is present
        else:
            # Creating a boolean variable to help deal with the node to be removed
            node_located = False

            # Creating a previous_node to hold the node that will be visited before the node to removed
            previous_node = None

            # Setting the current node to the current_node
            current_node = self.head

            # while loop to help traverse through the list
            while current_node and not node_located:
                # Checking if the node to be removed is the head node of the list
                if current_node.data_attribute == data and current_node is self.head:

                    # setting the head node to the next node in the list
                    self.head = current_node.next_node

                    # setting the node located variable to true to break the loop
                    node_located = True

                # checking if the current node contains the data to be removed and is not the head
                elif current_node.data_attribute == data:
                    # setting the node located to be true to break the node
                    node_located = True

                    # setting the next node of the previous node to the next node of the current node
                    previous_node.next_node = current_node.next_node

                # else if the node with the data is not found
                else:
                    # Setting the previous node to the current node
                    previous_node = current_node

                    # Setting the current node to the next node in the list
                    current_node = current_node.next_node

        return f"Node removed => {current_node}"

    # the repr method to provide a better string representation of the singly linked list class
    def __repr__(self):
        # setting the node in focus to the current_node variable
        current_node = self.head

        # a nodes variable to hold all the nodes in the list
        nodes = []

        # node position index
        node_position = 0

        # a while loop to traverse through the list
        while current_node:
            # Incrementing the node position
            node_position += 1
            # Checking if the node in focus is the head node
            if current_node is self.head:
                nodes.append(f"[Head node (Node {node_position}): {current_node.data_attribute}]")

            # Checking if the node in focus is the tail node
            elif current_node.next_node is None:
                nodes.append(f"[Tail node (Node {node_position}): {current_node.data_attribute}]")

            else:
                nodes.append(f"[Node {node_position} : {current_node.data_attribute}]")

            # setting the current node to the next node in the list
            current_node = current_node.next_node
        return " => ".join(nodes)


new_list = SinglyLinkedList()
new_list.prepend(20)
new_list.prepend(80)
new_list.prepend(50)
new_list.append(60)
new_list.append(-90)
new_list.append(10)
print(new_list.__repr__())
new_list.insert(-200, 3)
print(new_list.__repr__())
print(new_list.remove(20))
print(new_list.search(50))
print(new_list.__repr__())
new_list.insert(5000, 5)
print(new_list.__repr__())