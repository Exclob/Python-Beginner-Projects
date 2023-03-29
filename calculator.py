def calculator(a: int, b: int) -> float:
    print('Available operations: add, subtract, multiply, divide, power, modulus, floor division')
    operation = input('Enter an operation: ').strip().lower()
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b
    elif operation == 'power':
        return a ** b
    elif operation == 'modulus':
        return a % b
    elif operation == 'floor division':
        return a // b
    else:
        print('Please provide a valid operation.')
        return calculator(a, b)

print(calculator(5, 8))
