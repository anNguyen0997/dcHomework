#Even Odd
try:
    number = int(input('Enter a number :'))

    if number % 2 == 0:
            print("It's Even!")
    elif number % 2 == 1:
            print("It's Odd!")
except:
    print('Enter a valid number!')