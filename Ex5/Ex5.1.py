import random

n = int(input("Enter number of rolls: "))

sum = 0
for i in range(1, n+1):
    sum += random.randint(1,6)

print('Final sum: ', sum)