val = input('Enter a number from 1-9: ')
boo = val.isnumeric()
print(boo)
message = "Sorry, invalid input"
if(boo):
    num = int(val)
    if(1 <= num <= 9):
        print(type(num))    
        message = 'Great! You entered: ' + val
print(message)