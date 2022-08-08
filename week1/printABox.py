# Print a Box
# Given a height and width, input by the user, 
# print a box consisting of * characters as its border.

widthIn = int(input('Enter a WIDTH : '))
heightIn = int(input('Enter a HEIGHT : '))

def num(widthIn, heightIn):

    for row in range(1, widthIn + 1):
        for col in range(1, heightIn + 1):

            if (row == 1 or row == widthIn):
                print('*', end = ' ')
            elif (col == 1 or col == heightIn):
                print('*', end = ' ')    
            else:
                print(' ', end =' ')
        print()

num(widthIn, heightIn)