# To make use of json in my python program, i must first of all import the json module
import json

# A sample python dictionary
dictionary_person = {"name": "John", "age": 30, "city": "Cape Coast", "has_children": True,
                     "occupation": ["Software Engineer", "Data Scientist"]}

# Converting a dictionary to a json variable(Performing the serialization process)
"""
To convert any python data structure such as a dictionary to a json variable, the 
function dumps from the json module is used
"""

json_variable_person = json.dumps(dictionary_person, indent=4)
print(json_variable_person)

"""
To convert any python data structure such as  a dictionary to a json file or text, the 
function dump from the json module is used
"""

with open("json_file.json", "r+") as json_file:
    json.dump(dictionary_person, json_file, indent=4)

# Converting a json variable to a dictionary (Performing a deserialization process)
"""
To convert any python data structure such as a dictionary to a json variable, the 
function loads from the json module is used
"""

dictionary_person = json.loads(json_variable_person)
print(dictionary_person)

"""
To convert a json file or text to a dictionary, the 
function load from the json module is used
"""
with open("json_file.json") as json_file:
    dictionary_person = json.load(json_file)

print(dictionary_person)

# Converting a python object to a json variable, file or text
"""
Python Object is not JSON serializable and hence must first be encoded before it can 
be converted to a json variable, file or text
"""


# Creating a class called User
class User:
    # an init function to help create instances of the class
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Instance of the user class
user = User("Naomi", 39)


# the encoding function
def encode_user(obj):
    # checking if the argument being passed is an instance of the class user
    if isinstance(obj, User):
        # return a dictionary with the instance variables being the values of the dictionary
        return {"user_name": obj.name, "user_age": obj.age, obj.__class__.__name__: True}
    else:
        raise TypeError("Object passed as argument is not an instance of the User Class")


# Performing the conversion using the encoding function
json_user_variable = json.dumps(user, default=encode_user)
print(json_user_variable)

"""
In trying to encode a class to make it json serializable, a function named JSONEncoder can be used
When this method is imported, a class must be created for the encoding. The class must inherit
from the imported function and over the default method present in the dumps function.
In the overriding function, we first check if the object being passed is an instance of the class we are dealing
with and return a dictionary if true else invoke the default method of the JSONEncoder to deal with it
"""

from json import JSONEncoder


class UserEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {"user_name": obj.name, "user_age": obj.age, obj.__class__.__name__: True}
        return JSONEncoder.default(self, obj)


user_json_formatted_variable = UserEncoder().encode(user)
print("JSON format ------>", user_json_formatted_variable)
