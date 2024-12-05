num = 10
limit = 5
count = 0
playGame = False
guess = 0
while guess != num:
    print('You have', limit - count, 'attempts left.')
    guessFirst = input('Enter a number between 1 - 10: ')
    if(guessFirst.isnumeric()):
        guess = int(guessFirst)
        if guess == num:
            playGame = True
        if(guess < num):
            print('Too low! Try again.')
        if(guess > num):
            print('Too high! Try again.')
    count += 1
    if(limit - count == 0):
        break
else:
    playGame = True

if(playGame):    
    print('-- Congratulations! -- You Got It! ' + '\U0001F973' * 3)

else:
    print('You have run out of attempts. The number was', num)