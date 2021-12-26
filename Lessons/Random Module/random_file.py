# this file is used to study the random module
# To use the random module, the module must first be imported
import random
"""
The random module generates random values. These values are not genuine random values 
since a value has the capability of being repeated. As such, these values are called pseudorandom
values. 
"""

# the random method of the module produces pseudorandom float
random_variable = random.random()
print("Random() value ---->", random_variable)

# the uniform method of the module produces a pseudorandom float within a specified range
# the method requires the user to specify the range within which the values must be generated
# The upper bound of the range is included in the values to be generated
uniform_variable = random.uniform(2, 6)
print("Uniform(a, b) value ---->", uniform_variable)


# the randInt method of the module generates integer based values within a specified range
# the method requires the user to specify the range within which the values must be generated
# With the randInt method, both a and b in the argument(a, b) are included in the range
randInt_variable = random.randint(2, 6)
print("RandInt(a, b) value ---->", randInt_variable)

 
# the randrange method of the module generates an integer based values within a specified range
# the method requires the user to specify the range within which the values must be generated
# The upper bound is not included in the range of values to be generated
randrange_variable = random.randrange(1, 10, 3)
print("RandRange(a, b) value ---->", randrange_variable)


# the normalvariate method of the module generates a floating point value for a normal distribution in statistics
# the method requires the user to pass the mean of the population(mu) and the standard deviation of the population as
# arguments.
normal_variate_variable = random.normalvariate(4.5, 10)
print("Normalvariate(a, b) value ----> ", normal_variate_variable)


# the choice method of the module helps to generate a random choice from a collection of items
choice_list = ["home", 1, 5, "bye"]
selected_choice = random.choice(choice_list)
print("Choice value ----> ", selected_choice)


# the sample method of the module helps to select a random sub-collection from a main collection
# In this method, the collection and the length of the sub-collection must be specified
# all the selection made by this method are unique and no one selected item is repeated
sub_collection = random.sample(choice_list, 3)
print("Sample value ----> ", sub_collection)


# the choices method of the module helps to select a random sub-collection from a main collection
# In this method, the collection and the length of the sub-collection must be specified
# all the selection made by this method are not unique and can be repeated
# the length of the collection is assigned to keyword argument represented as k
sub_collection_for_choices = random.choices(choice_list, k=3)
print("Choices value ---->  ", sub_collection_for_choices)


# the shuffle method of the module helps to randomly rearrange the elements of a list
random.shuffle(choice_list)
print("Shuffled value ----> ", choice_list)

# the seed method in the module helps to reproduce results for the other methods
random.seed(1)
print(random.randint(1, 10))
print(random.random())

random.seed(1)
print(random.randint(1, 10))
print(random.random())

# the random module is not adviceable for generating randoms values to be used for security. The secrets module is
# preferred