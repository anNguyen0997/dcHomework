# Take input from the user and find out if that number is prime or not.

userIn = int(input('ENTER A PRINE NUMBER : '))

isPrime = True
if userIn > 1:

    for num in range(2, userIn):
        if userIn % 2 == 0:
            isPrime = False
            print('NOT A PRIME NUMBER')
            break

if isPrime:
    print('PRIME NUMBER')
else:
    print('NOT A PRIME NUMBER')