x = 0
while x >= 0 :
    x = float(input("Enter size in inches: "))
    if x >= 0:
        print("Size in centimeters: ", x*2.54)
    else:
        break