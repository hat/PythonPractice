__author__ = 'taztony2010'

import random, logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
guess = ''

while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 0:
    toss = 'tails'
elif toss == 1:
    toss = 'heads'
else:
    logging.CRITICAL('Toss is not between 0, 1')

logging.debug('guess is ' + str(guess) + ', toss is ' + str(toss))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')