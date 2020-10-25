import random
tries = 0
while tries < 1:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        print('Heads')
    if coin == 2:
        print ('Tails')
