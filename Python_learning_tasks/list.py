testList = [50, 100, 'Laurence', 'Hello', 50, 100, True]

a, b, c, d, e, f, g = testList

testList.insert(2, 'Python') # inserts 'Python' at index 2

testList.append('End') # adds 'End' to the end of the list

testList.remove(50) # removes the first occurrence of 50 from the list

testList.pop() # removes the last element from the list

# OR

testList[-1] = 'New End' # replaces the last element with 'New End'

print(testList)
print(testList[2])
print(c)
print(len(testList)) # prints the length of the list
print(testList[-2]) # when the number is negative, it starts counting from the end
print(testList[1:4]) # prints a sublist from index 1 to 3
print(testList[:3]) # prints a sublist from the beginning to index 2
print(testList.index('Python')) # prints the index of the first occurrence of 'Python'

val = ('Python' in testList) # checks if 'Python' is in the list

print(val) # prints True if 'Python' is in the list, False otherwise

testList.sort() # sorts the list in ascending order

testList.reverse() # reverses the order of the list