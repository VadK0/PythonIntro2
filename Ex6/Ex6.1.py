import random

def roll():
    return random.randint(1,6)

dice = 0
while dice != 6:
    dice = roll()
    print(dice)