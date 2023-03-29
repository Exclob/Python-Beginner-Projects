def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        print(a)
        a, b = b, a+b

fibonacci(100)