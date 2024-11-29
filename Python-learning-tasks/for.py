testList = ['Laurence', 'John', 'World', 55, 100, True]

for i in testList:
    print(i)

myStr = 'Hello World!'
for l in myStr:  # we use for loop to iterate over each character in the string
    if l == 'l':
        continue # skips the rest of the loop and returns back to the for loop on the next iteration
    if l == 'x':
        break # stops the loop completely
    print(l)
else:
    print('Word done!')

testDic = {  # a dictionary
    'first': 'John',
    'last': 'Doe',
    'allowed': 'True'
}

for key in testDic: 
    print(key + ' : ' + testDic[key])

for val in testDic.values():  # prints all values in the dictionary
    print(val)

for val in testDic.keys():  # prints all keys in the dictionary
    print(val)

for key, val in testDic.items():  # prints both keys and values in the dictionary
    print(key, val)
