"""
In order to create a linked list data structure, a node class must first be created
The node class possesses only two class variables namely the data and next_node
The data variable stores the content of the item to stored and the next_node variable stores the reference of the next
item in the list
The data variable and the next_node variable are initially declared none.
An init method is provided for the node class to enable the creation of instances of the node class
"""


# Creating the class for the node
class Node:
    # Creating the data and next_node variables
    data = None
    next_node = None

    # The init method to provide the class an ability for instance creation
    def __init__(self, data):
        self.data = data

    # The repr method to provide a proper string representation of the node
    def __repr__(self):
        return f"<class Node : Data -> {self.data}>"


    """
    Creating the actual linked list with methods such as init, repr, is_empty, prepend, append, size, search
    The linked list is a singly linked list class with only one class variable known as the head of the list
    """


class LinkedList:

    # The init method for creating an instance of the class
    def __init__(self):
        self.head = None

    # The is_empty method for checking if the list has no content
    def is_empty(self):
        return self.head is None

    # The size method to determine the number of items in the list
    def size(self):
        # Creating a current_node variable to hold the current node present in the list
        current_node = self.head

        # Creating a variable count to hold the number of items(nodes) in the list
        count = 0

        # While loop to traverse through the linked list
        while current_node:
            count += 1
            current_node = current_node.next_node
        return count

    # The prepend method for adding items at the beginning of the list
    def prepend(self, data):
        # Creating a new node variable for the introduced data
        new_node = Node(data)

        # Making the new node point to the original head of the list
        new_node.next_node = self.head

        # Setting the new node to be the head of the list
        self.head = new_node

    # The search method to locate a specific item within the list
    def search(self, item):
        # Starting the search from the head node of the list
        current_head_node = self.head

        # while loop to search through the list
        while current_head_node:
            if current_head_node.data == item:
                return current_head_node
            current_head_node = current_head_node.next_node
        return None

    # The insert method to add a new item at any position in the list
    def insert(self, index, data):
        # checking if index equals zero so as to prepend the data to the list
        if index == 0:
            self.prepend(data)

        elif index > 0:
            # Creating a node to the data to be added to the list
            new_node_to_be_added = Node(data)

            # creating a node_site variable to help locate the exact position in the list where the new node must be
            # added
            node_site = index

            # In order to traverse starting from the head, setting self.head to a variable called current_node
            current_node = self.head

            #  while loop to traverse through the nodes in the list until we locate the site where the new_node must be
            # added. The traversal must end at a node prior to the site where the node must be added. This is to help
            # connect that node to the new node
            while node_site > 1:
                # setting the current_node to the next node in the list enabling the movement of one node to another
                current_node = current_node.next_node

                # Decreasing the node_site value to help reach the node prior to the site of insertion of the new node
                node_site -= 1

            # Setting the current_node reached to a variable called previous_node
            previous_node = current_node

            # Setting the node to which the current_node points to a variable called next_node
            next_node = current_node.next_node

            # Connecting the previous_node to the reference of the new_node_to_be_added
            previous_node.next_node = new_node_to_be_added

            # Connecting the new_node_to_be_added to the reference of the node that would ahead of it(the next_node)
            new_node_to_be_added.next_node = next_node

    # The remove method to delete the items from the list
    def remove(self, item):
        if self.head is None:
            raise Exception(f"The list is an empty")

        elif self.search(item) is None:
            raise Exception(f"{item} is not present in the list")

        else:
            current = self.head
            previous_node = None
            located = False

            while current and not located:
                if current.data == item and current is self.head:
                    located = True
                    self.head = current.next_node

                elif current.data == item:
                    located = True
                    previous_node.next_node = current.next_node
                else:
                    previous_node = current
                    current = current.next_node
            return current

    # The repr method to provide the string representation of the LinkedList class
    def __repr__(self):
        current_node = self.head

        list_of_nodes = []

        while current_node:
            if current_node is self.head:
                list_of_nodes.append(f"[Head : {current_node.data}]")
            elif current_node.next_node is None:
                list_of_nodes.append(f"[Tail : {current_node.data}]")
            else:
                list_of_nodes.append(f"[{current_node.data}]")
            current_node = current_node.next_node
        return ' => '.join(list_of_nodes)


linked_list_instance = LinkedList()
linked_list_instance.prepend(20)
linked_list_instance.prepend(100)
linked_list_instance.prepend(300)
linked_list_instance.prepend(-123)
linked_list_instance.prepend(287)
print(linked_list_instance.__repr__())
print(linked_list_instance.remove(300))
print(linked_list_instance.__repr__())

list_ = LinkedList()
list_.prepend(300)