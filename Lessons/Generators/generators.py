from sys import getsizeof
"""
Generators are functions that return an object that can be iterated over
The values for the object which can be iterated over are done so one after the other only when asked for
Generators are created just like normal functions with a keyword yield in their definition
The yield keyword pushes it's accompanying value when a call is made to the generator and then stops if the call was
with the keyword function next(generator). It then continues from the value where it stopped when a second call is made
for the generator.
Generators are memory-efficient and hence helps to save memory
Generators always raise a StopIteration when it does not encounter a yield keyword

"""


# Creating a generator function
def generator():
    yield [1, 2, 3]
    yield "Hello generator world"
    yield {"key_1": "Wow", "key_2": "Happy"}


# Calling the generator
sample_generator = generator()
print(next(sample_generator))
print(next(sample_generator))


# Implementing the fibonacci series using a generator
def fibonacci_generator(limit):
    first_term, second_term = 0, 1
    while first_term <= limit:
        yield first_term
        first_term, second_term = second_term, first_term + second_term


# calling the fibonacci generator
for index in fibonacci_generator(30000):
    print(index)

print("........................................................................")
# Estimating the memory space occupied by the Fibonacci series generator for a very large input
print(getsizeof(fibonacci_generator(7800000000000000000000000000000089000890)))

# A short syntax for creating a generator is using the procedure for list comprehension but using braces rather than
# square brackets
new_generator = (number for number in range(21, 20000) if number in fibonacci_generator(50000000))
print(list(new_generator))