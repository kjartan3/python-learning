# difference between a tuple and a list is that you canny change elements of a tuple once it's created

testTuple = ('Hello', 'Laurence', 'John', 100, True)

val = len(testTuple)

print(testTuple)

# testTuple[2] = 'David'  <-- this will not work because tuples are immutable

val = testTuple[2]
print(val)