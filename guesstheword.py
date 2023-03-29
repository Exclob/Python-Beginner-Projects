import random

def guessword(cap:int):
    words = ['this','and','which','can','well','be']
    random_word = random.choice(words)

    for _ in range(cap):
        guess = str(input('Guess the word: '))
        if random_word == guess:
            print('You guessed correctly!')
            break
        else:
            print('You guessed incorrectly!')


guessword(3)

