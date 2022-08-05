# Print a Box
# Given a height and width, input by the user, 
# print a box consisting of * characters as its border.

widthIn = int(input('Enter a WIDTH : '))
heightIn = int(input('Enter a HEIGHT : '))

def num(widthIn, heightIn):
    # print('*' * widthIn)
    for i in range(1, widthIn + 1):
        for x in range(1, heightIn + 1):
            if (i == 1 or i == widthIn or x == 1 or x == heightIn):

                print('*', end = '')
            else:
                print(' ', end ='')
        print()

num(widthIn, heightIn)