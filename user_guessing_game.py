import random

def guessing(x:int)->int:
    while True:
         bot =  random.randint(1,x)
         user = int(input(f'Guess a number from 1 to {x}: ').strip())
         if user == bot:
             print('You won')
             break
         else:
             try_again = str(input('Try again(y/n): '))
             if try_again.lower() not in ['y','yes']:
                 break

guessing(5)

