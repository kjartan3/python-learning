boo = True
a, b = 500, 500

# print(a < b)

if boo:
    print('boo is True')
if a < b:
    a = 1000
    print(a)
    print('True')
elif a > b:  # else if a < b then print
    print('a is greater than b')
else:
    print('a and b must be equal')