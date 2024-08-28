import random

num = int(input("Enter a number: "))

def roll(n):
    return random.randint(1,n)

dice = 0
while dice != num:
    dice = roll(num)
    print(dice)