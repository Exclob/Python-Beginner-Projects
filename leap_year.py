def leap(year:int)->None:
    if (isinstance(year,int)):
        if year % 4 == 0:
            print('This is a leap year!')
        else:
            print('This is not a leap year!')
    else:
        print('The expected value is suppose to be a year (int)')

leap(2008)