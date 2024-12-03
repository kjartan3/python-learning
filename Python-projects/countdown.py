#  a countdown project that will count down from the input number/seconds

import time

def test():  # define a test function that will tests the countdown function works correctly
    val = 0
    while val < 10:
        val += 1
        time.sleep(1)
        print(val)

def countdown(t):  # defines a countdown function that will count down
    while t:
        minutes = t // 60 
        seconds = t % 60
        output = 'Your Time Left is {:02d}:{:02d}'.format(minutes, seconds)  # format enables you to structure the output correctly
        print(output)
        time.sleep(1)
        t -= 1
    print('Time is up!')
    start()

def start():  # a start function that will start a countdown project
    t = input('Enter the number of seconds: ')
    if t.isnumeric():
        countdown(int(t))
    else:
        print('Invalid input. Please enter a number of seconds')
        start()
start()

t = input('Enter a number of seconds to countdown: ')
if t.isnumeric():
    countdown(int(t))
else:
    print('Invalid input. Please enter a number of seconds')