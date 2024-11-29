# Data types in python are:
# 1. Integers (int)
# 2. Integers (float)
# 3. Strings (str)
# 4. Booleans (bool)
# 5. Lists (list)
# 6. Tuples (tuple)
# 7. Sets (set)
# 8. Dictionaries (dict)

a = True
print(type(a))  # Output: bool

b = 10
print(type(b))  # Output: int

c = 10.5
print(type(c))  # Output: float

d = 'Hello, world!'
print(type(d))  # Output: str

e = ['John', 'Mary', 'David']
print(type(e))  # Output: list

f = (1, 2, 3, 4, 5)
print(type(f))  # Output: tuple

g = {1, 2, 3, 4, 5}
print(type(g))  # Output: set


# Accessing elements in a list - you can add to a list
testList = [50, "100", True, 3.14, ['apple', 'banana']]
print(testList[1])  # Output: [50, '100', True, 3.14, ['apple', 'banana']]

print(len(testList))  # Output the length of the list: 5

print(type(testList))  # Output the type of datatype/s: list


# # Accessing elements in a tuple - you cannot add to a tuple
testTuple = (50, "100", True, 3.14, ['apple', 'banana'])
print(testTuple[1])  # Output: '100'

print(len(testTuple))  # Output the length of the tuple: 5

print(type(testTuple))  # Output the type of datatype/s: tuple


# Accessing elements in a set - you cannot add to a set and removes duplicates
testSet = {50, "100", True, 50, 'apple', 100, 100}
print(testSet)  # Output: {True, 3.14, 50, '100', ['apple', 'banana']}

print(len(testSet))  # Output the length of the set: 5

print(type(testSet))  # Output the type of datatype/s: set


# Accessing elements in a dictionary - they have a defined order and no duplicates allowed
testDict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(testDict['name'])  # Output: John

print(len(testDict))  # Output the length of the dictionary: 3

print(type(testDict))  # Output the type of datatype/s: dict

