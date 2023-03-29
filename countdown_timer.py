import time

def countdown(t:int)->int:
    while t:
        minutes,seconds = divmod(t,60)
        print(f'{minutes:02d}:{seconds:02d}', end = '\r')
        time.sleep(1)
        t -= 1
        if t == 0:
            print('Timer Over!')
            break

countdown(10)

