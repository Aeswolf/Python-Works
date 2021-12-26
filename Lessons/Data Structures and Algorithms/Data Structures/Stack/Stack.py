"""
This is a file that implements that the stack data structure.
The stack data structure is a data structure that stores data according to the LIFO principle.
Operations performed by the stack data structure:
- Pop -> returns the last element of the stack and deletes it from the stack
- Push -> adds an element to the stack
- is_empty -> monitors the emptiness of the stack
- Peek -> returns the element at the top of the stack without removing it from the stack
"""


# creating the blueprint for the stack data structure
class Stack:
    # The init method for creating an instance of the stack
    def __init__(self):
        # initializing an empty list
        self.stack = []
        # a variable called top to handling the number of elements present in the list
        self.top = len(self.stack)

    # the is_empty method for checking if the stack has no member
    def is_empty(self):
        return self.top == 0

    # the size method for returning the total number of elements in the stack
    def size(self):
        return self.top

    # the push method for adding elements unto the stack
    def push(self, data):
        self.stack.append(data)
        self.top += 1

    # the peek method for returning the last element in the stack without removing it from the stack
    def peek(self):
        return self.stack[self.top - 1]

    # the pop method for returning the last element in the stack and removing the element from the stack
    def pop(self):
        # setting the last element in the list to the variable last_element
        last_element = self.stack[self.top - 1]

        # decreasing the value of the self.top variable
        self.top -= 1

        # removing the last element from the stack
        self.stack = self.stack[:self.top]

        return last_element


stack = Stack()
print("Empty stack = ", stack.stack)
print("Number of items in the stack :", stack.top)
print("The stack is empty :", stack.is_empty())
stack.push(30)
stack.push(31)
stack.push(32)
stack.push(33)
stack.push(200)
stack.push(210)
stack.push(150)
print("The number of elements in the current stack :", stack.size())
print("The current stack :", stack.stack)
print("Value obtained upon peeking at the stack :", stack.peek())
print("Current stack :", stack.stack)
print("Value obtained upon popping the stack :", stack.pop())
print("Current stack :", stack.stack)
print("Value obtained upon popping the stack :", stack.pop())
print("Current stack :", stack.stack)