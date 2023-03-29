import random

def dice_roll():
    while True:
        roll = input('Would you like to roll the dice(y/n): ').strip().lower()
        if roll == 'yes' or roll == 'y':
            print(f'Dice Number: {random.randint(1,6)}')
        elif roll == 'no' or roll == 'n':
            break
        else:
            print('Invalid input, please enter "y" or "n"')
            continue
      
        roll_again = input('Would you like to roll again (y/n): ').strip().lower()
        if roll_again == 'yes' or roll_again == 'y':
            print(f'Dice Number: {random.randint(1,6)}')
        elif roll_again == 'no' or roll_again == 'n':
            break
        else:
            print('Invalid input, please enter "y" or "n"')
            continue

dice_roll()
