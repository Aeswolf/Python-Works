"""
Provides a blueprint for creating queues
A queue is a data structure that working on the principle FIFO(first_in_first_out)
A queue permits the following operation => enqueue -> for adding an item at the back of the queue and dequeue -> for
removing an element at the front of the queue
This file implements a queue using the array(list) data structure
"""


# Creating the class that will provide the blueprint for creating queues
class Queue:
    """
    Provides the required blueprint or contract or template for creating and manipulating queues
    """

    # The init method for creating instances of the queue class
    def __init__(self):
        # Creating an empty list whenever a new a queue is created
        self.queue = []

    # The is_empty method to ensure that the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # The size method for returning the number of items in the queue
    def size(self):
        return len(self.queue)

    # The enqueue method to permit the addition of an item to the back of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # The dequeue method for removing an item from the front of the queue
    def dequeue(self):
        # Checking if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            first_item = self.queue[0]
            # slice for removing the first item from the queue
            self.queue = self.queue[1:]
            return first_item


# Creating an instance of the Queue class
queue = Queue()
print(queue.is_empty())
queue.enqueue(200)
queue.enqueue(201)
queue.enqueue(203)
queue.enqueue(204)
queue.enqueue(205)
queue.enqueue(206)
print(queue.is_empty())
print(queue.queue)
print(queue.dequeue())
print(queue.queue)
print(queue.dequeue())
print(queue.queue)
