def conv(gall):
    return gall * 3.785


gallons = 0

while gallons >= 0:
    gallons = float(input("Enter a gallons: "))
    if gallons >= 0:
        print(conv(gallons))
    else:
        print('Program finished.')
