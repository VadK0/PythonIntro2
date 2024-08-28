import random

x = random.randint(1,10)

y = 11
while y != x:
    y = int(input('Enter a number: '))
    if x == y:
        print('Correct!')
    elif x > y:
        print('Too low!')
    elif x < y:
        print('Too high!')
