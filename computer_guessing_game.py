import random

def guessing(x: int) -> None:
    answer = None
    low, high = 1, x
    while answer != 'C' and low <= high:
        user = random.randint(low, high)
        answer = input(f"Is {user} (C)orrect, (L)ower, or (H)igher? ").strip().upper()
        if answer == 'C':
            print(f"The computer guessed it! The answer was {user}. You lose!")
        elif answer == 'L':
            high = user - 1
        elif answer == 'H':
            low = user + 1
        else:
            print("Invalid input, please enter 'C', 'L', or 'H'.")
    
guessing(100)
