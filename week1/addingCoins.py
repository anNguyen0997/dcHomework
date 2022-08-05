# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin? 
# If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program. 

prompt = input('Do you want a coin? Type Yes / No : ')
coin = 0

if prompt.lower() == 'yes':
    print('Do you want another coin?')
    coin = coin + 1
    print('You have %d coins' % coin)

elif prompt.lower() == 'no':
    print('No more coin')
