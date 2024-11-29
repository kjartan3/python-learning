# sets are different from tuples and lists
#   in that they cannot contain duplicate elements
#   and they are unordered

testSet = {'John', 100, True, 100, 'Laurence'}

testSet.add('New') # adds 'David' to the set

testSet.remove(100) # removes the first occurrence of 100 from the set

testSet.pop() # removes the last element from the set

val = ("John" in testSet) # checks if 'John' is in the set

print(testSet)

print(val) # prints True if 'John' is in the set, False otherwise

# however, because the sets are unordered, sometimes it may print false.