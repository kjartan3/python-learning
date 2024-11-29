val = 0  # initialize a variable

while val <= 10:  # a while loop that runs 10 times
    print(val)
    val += 1
    if val == 2:  # conditional statement to continue the loop
        continue  # skips the rest of the loops and returns back to while loop again on the 3rd iteration
    print('.')
    if val == 15:  # conditional statement to break the loop
        break  # stops the loop completely
else:
    print('val is no longer less than 11')  # this block will be executed if the loop finishes without being interrupted by a break statement
    
    