import math

def pizzaPrice(size, price):
    s = math.pi * size/200 ** 2
    return s/price

size1 = int(input("Enter the size of pizza #1:"))
price1 = int(input("Enter the price of pizza #1:"))
size2 = int(input("Enter the size of pizza #2:"))
price2 = int(input("Enter the price of pizza #2:"))

value1 = pizzaPrice(size1, price1)
value2 = pizzaPrice(size2, price2)
print(value1, value2)

if value1 > value2:
    print("The 1st pizza value is greater")
elif value2 > value1:
    print("The 2nd pizza value is greater")
else:
    print("Both pizza values are equal")