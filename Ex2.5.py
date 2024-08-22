tal = float(input("Enter talents: \n"))
p = float(input("\nEnter pounds: \n"))
l = float(input("\nEnter lots: \n"))

result = ((tal*20+p)*32+l)*13.3
result1 = result // 1000
result2 = result % 1000
print("The weight in modern units:\n",int(result1)," kilograms and ",round(result2,2)," grams.")