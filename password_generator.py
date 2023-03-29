import random

def pwdpgenerator(length:int,amount:int = 1)-> str:
    charactersLower = 'abcdefghijklmnopqrstuvwxyz'
    charactersUpper = charactersLower.upper()
    symbols = '!@#$%^&*()_-+={}[]|.,><'
    digits = '1234567890'

    totalCharacters = charactersLower + charactersUpper + symbols + digits

    for _ in range(amount):
        password = ''.join(random.choice(totalCharacters) for _ in range(length))
        print(password)

pwdpgenerator(8,3)