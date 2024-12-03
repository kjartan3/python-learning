# A random dice game using random module and if statements to determine output.

import random # using random module

min = 1
max = 10

computerScore = 0
playerScore = 0
inPlay = True

x = 20
while x < 10:  
    test = random.randint(min, max)  # allowing random number generation
    print(test)
    x += 1  # increment counter
def gamePlay():
    global inPlay
    global computerScore
    global playerScore
    while inPlay:
        player = random.randint(min, max)
        computer = random.randint(min, max)
        print(f'You got {player} vs {computer}')
        if(player == computer):
            print('It\'s a tie!')
        elif(player > computer):
            print('You win!')
            playerScore += 1
        elif(player < computer):
            print('Computer wins!')
            computerScore += 1
        inPlay = input('Roll again? (y/n): ')
        if inPlay == 'n' :
            break

gamePlay()
print('Game Over')
print(f'Computer Score: {computerScore } vs Player Score: {playerScore }')