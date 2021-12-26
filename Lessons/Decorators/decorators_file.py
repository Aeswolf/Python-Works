"""
This is a file that helps understand decorators
A decorator is a function that takes another function as argument, modifies the function
by adding an extra functionality to the function without explicitly changing the argument
function itself.
Within every decorator function is a wrapper function in which the augmented function is called
and the extra functionality is provided.
"""


# Creating a decorator for a function with no arguments
def decorator(func):
    # Creating the wrapper function
    def wrapper():
        print("Extra functionality")
        # calling the function
        func()

    # returning the wrapper function to ensure the execution of the function
    return wrapper


# Creating the actual function to be affected by the decorator
@decorator  # the decorator function is called with a preceding @ sign on top of the actual function
def actual_function():
    print("Content of the actual function")


# making a function call
actual_function()


# Creating a decorator for a function with an argument
# for such decorators, the wrapper function and the function call in the wrapper class must have *args and **kwargs
# to compensate for the argument of the actual class
def decorator_for_functions_with_argument(func):
    # Defining the wrapper function for the decorator
    def wrapper(*args, **kwargs):
        print("Extra functionality for the function with argument(s)")
        # calling the function in the wrapper class. For such functions, a return statement is accompanies the wrapper
        # to return the function
        return func(*args, **kwargs)
    # returning the wrapper function to ensure the execution of the function
    return wrapper


# Creating the actual function
@decorator_for_functions_with_argument
def second_actual_function(argument):
    print(f"This is the function with the argument {argument}")


# Calling the second actual function
second_actual_function("second function")


# Multiple decorators can be declared for a second function. For such a situation, the decorators are stacked up,
# on top of each other. The first decorator is applied before the second and so forth
# if the function for which the multiple decorators are being declared for possess an argument, then wrapper  functions
# in all decorators must have the *args and **kwargs arguments to compensate for function's argument
# Classes can also be used as decorators. To do so, the __call__(self) must be called within the class to make implement
# the decorator behavior
