import sys
import random

def game():
    random_number = random.randint(1, 10)
    tries = 3
    
    while True:
        try:
            guess = int(input('Guess a number between 1-10: '))
            if guess < 1 or guess > 10:
                print('Please enter a number between 1-10.')
            else:
                if guess == random_number:
                    return "You guessed the correct number!" 
                elif tries > 1:
                    tries -= 1
                    print(f'Incorrect guess. You have {tries} tries left.')
                else:
                    return f'You ran out of tries. The correct number was {random_number}.'
        except ValueError:
            print('Please enter a number.')

print(game())