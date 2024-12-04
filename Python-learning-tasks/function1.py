def fun1(val):
    print(val * val)
    # print('Hello')

# fun1(1)
# fun1(3)
# fun1(5)

def fun2(first, second):
    print("Greetings, " + first + ' ' + second)

# fun2('Jamie', 'Foxx')


def fun3(val1, val2): # Function with return statement
    total = val1 + val2
    print(str(val1) + ' + ' + str(val2) + ' = ' + str(total))  # printing in string format
    return total

num1 = fun3(6, 7)
num2 = fun3(62, 714)
print('Number 1 is:', num1, ' & ', 'Number 2 is:', num2)
