# dictionary to store file paths and their respective sizes

testDic = {'first':'Hello World', 'key':{'one':'test', 'two':'test2'}, 'num':100, 'num':200, 'num':300, 'boo':True}

print(testDic)
testDic['first'] = 'New Value' # updates the value of 'first' to 'New Value'
val = testDic['first']  # retrieves the value of 'first'
val = testDic['num']  # retrieves the value of 'num'
val = testDic['key']['two']  # retrieves the value of 'two' from the nested dictionary

testDic['test'] = 1000  # adds a new key-value pair to the dictionary
testDic.pop('key')  # removes the key-value pair with the key 'test' and 'test2 from the dictionary
# testDic.clear()  # removes all key-value pairs from the dictionary

val = testDic.keys()  # retrieves all keys from the dictionary
val = testDic.values()  # retrieves all values from the dictionary

test2 = {
    'first' : 100,
    'second' : 'Values',
    'third' : True
}  # creates a new dictionary

print(test2)

print(testDic)
print(val)
print(testDic['test'])