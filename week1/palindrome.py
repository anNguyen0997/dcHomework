# Create an app which detects if the input word is a palindrome or not.

userIn = input('Enter a palindrome string : ')

reversedIn = (userIn[::-1])
if userIn == reversedIn:
    print('PALINDROME')
else:
    print('NOT PALINDROME')
    