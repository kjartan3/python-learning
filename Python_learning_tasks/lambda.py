# lambda is a small anonymous function 
# that can take any number of arguments, but can only have one expression.

val = lambda a : a * 5
num1 = val(5)
print(num1)  # Output: 25


# Lambda function with multiple values/arguments

val1 = lambda a, b : a * b
num2 = val1(10, 20)
print(num2)  # Output: 200

print(val1(3, 9)) # Output: 27