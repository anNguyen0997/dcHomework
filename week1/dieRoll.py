import random

print("Let's roll a dice!")
die = input('How many sides should it have? (2-20): ')
die = int(die)

print("It's rolling... ")
print("It's a " + str(random.randint(1,die)))