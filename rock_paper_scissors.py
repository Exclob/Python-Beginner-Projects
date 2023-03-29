import random

def playtime():
    while True:
         validInputs = ['rock','paper','scissors']
         user = str(input('Choose rock, paper or scissors: ').lower().strip())
         if user not in validInputs:
              print('Invalid Input')
              return
         bot = random.choice(validInputs)
         print('\n')
         print(f'You chose:     {user.capitalize()}')
         print(f'Bot chose:     {bot.capitalize()}')
         print('-----------------------')
         if user == bot:
              print('        Draw')
         elif (user == 'rock' and bot == 'scissors') or (user == 'scissors' and bot == 'paper') or (user == 'paper' and bot == 'rock'):
              print('   You won :)')
         else:
              print('  You lost :(')
         print('\n')
         play_again = str(input('Would you like to play again (y/n): ').strip())
         if play_again.lower() not in  ['yes','y']:
              break

playtime()
