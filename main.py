from random import randint

logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
number = randint(1, 100)

print('Welcome to the Number Guessing Game!\nI´m thinking of a number between 1 and 100.')
difficulty = input('Choose a difficulty. Type "easy" or "hard": ')

if difficulty == 'easy':
    chances = 10
    print('Yoy have 10 attempts remaining')
else:
    chances = 5
    print('You have 5 attempts remaining')

def checking(chances, guess, number):
    if guess != number:
        if guess > number:
            print('Too high\nGuess again')
            
        elif guess < number:
            print('Too low\nGuess again')
            

    else:
        print(f'You got it! The answer is {number}')
        


jogando = True

while jogando:
    guess = int(input('Make a guess: '))

    if guess != number:
        chances -=1
    else:
        jogando = False
        
    checking(chances, guess, number)
    print(f'You have {chances} attempts remaining')
    


