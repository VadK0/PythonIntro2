import random

N = int(input("Enter a number: "))

n = 0
i = N
while i > 0:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    #print(x,y)
    #print(x**2 + y**2)
    if x**2 + y**2 < 1:
        n += 1

    i -= 1
#print('n=', n)
print('Pi = ', 4*n/N)