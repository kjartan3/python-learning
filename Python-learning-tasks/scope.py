# Scope is defined by where variables are declared.
# Global scope is defined outside of any function.
# Local scope is defined inside a function.

a = 'test'
b = 0

def fun1(val):
    # b = b + 1
    # a = 'hello'
    def fun2():
        global b # use global keyword to access global variable inside a local function
        nonlocal val # use nonlocal keyword to access nonlocal variable inside a local function
        b += 5
        val += 1000
        print(val)
    fun2()
    print(a)

fun1(100)
print(b)