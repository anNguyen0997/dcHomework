# Tip Calculator

# Prompt the user for two things:
# The total bill amount
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount). The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%


try:
    bill = float(input('Enter bill amount : '))
except: 
    print('PLEASE ENTER A VALID NUMBER')

service = input('Enter service level (bad:10%, fair:15%, good:20% : ')
if service == 'bad':
        tip = .10 * bill
elif service == 'fair':
        tip = .15 * bill
elif service == 'good':
        tip = .20 * bill
else:
        print('PLEASE ENTER GOOD, BAD, OR FAIR')

totalBill = tip + bill



print('Tip Amount: %2f' % tip)
print('Total Amount: %2f' % totalBill)