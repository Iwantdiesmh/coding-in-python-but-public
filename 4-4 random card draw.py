import random
symbols = ['of Spades', 'of Hearts', 'of Diamonds', 'of Clubs']
p1value = random.randint(1,13)
p1sym = symbols[random.randint(0,3)]
p2value = random.randint(1,13)
p2sym = symbols[random.randint(0,3)]
if p1value == int(11):
    print('Player 1 has got the Jack', p1sym)
elif p1value == int(12):
    print('Player 1 has got the Queen', p1sym)
elif p1value == int(13):
    print('Player 1 has got the King', p1sym)
else:
    print('Player 1 has got the', p1value, p1sym)
    
if p2value == int(11):
    print('Player 2 has got the Jack', p2sym)
elif p2value == int(12):
    print('Player 2 has got the Queen', p2sym)
elif p2value == int(13):
    print('Player 2 has got the King', p2sym)
else:
    print('Player 2 has got the', p2value, p2sym)

if p1value > p2value:
    print('Player 1 has the higher card')
elif p2value > p1value:
    print('Player 2 has the higher card')
else:
    if p1sym == p2sym:
        print('We have a draw')
    elif p1sym == 'of Spades':
        print('Player 1 has the higher card')
    elif p2sym == 'of Spades':
        print('Player 2 has the higher card')
    elif p1sym == 'of Hearts':
        print('Player 1 has the higher card')
    elif p2sym == 'of Hearts':
        print('Player 2 has the higher card')
    elif p1sym == 'of Diamonds':
        print('Player 1 has the higher card')
    elif p2sym == 'of Diamonds':
        print('Player 2 has the higher card')
