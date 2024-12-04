import random

computerScore = 0
playerScore = 0
arr = ['Rock', 'Paper', 'Scissors']
inPlay = True

# x = 3
# while x > 0:
#     test = random.randint(min, max)
#     print(test)
#     x -= 1

def gamePlay():
    global inPlay
    global computerScore
    global playerScore
    while inPlay:
        player = input('Rock Paper or Scissors? ').capitalize()
        computer = random.choice(arr).capitalize()
        print(f'You selected: {player}')
        print('vs')
        print(f'Computer selected: {computer}')
        if player == computer:
            print('It\'s a tie!')
        elif player == 'Rock':
            if(computer == 'Paper'):
                print('You lose!')
                computerScore += 1
            else:
                print('You win!')
                playerScore += 1
        elif player == 'Paper':
            if(computer == 'Scissors'):
                print('You lose!')
                computerScore += 1
            else:
                print('You win!')
                playerScore += 1
        elif player == 'Scissors':
            if(computer == 'Rock'):
                print('You lose!')
                computerScore += 1
            else:
                print('You win!')
                playerScore += 1
        inPlay = input('Play again? (y/n): ')
        if inPlay == 'n' :
            break

gamePlay()
print('Game Over!')
print(f'You ({playerScore}) vs Computer ({computerScore})')