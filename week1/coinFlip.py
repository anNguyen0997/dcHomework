#COIN FLIP
#random module to create random inputs
import random

coin = ['Heads', 'Tails']
coinToss = random.choice(coin)

if coinToss == 'Heads':
    print('You flipped a coin!')
    print('It is heads!')
else :
    print('You flipped a coin!')
    print('It is tails!')

