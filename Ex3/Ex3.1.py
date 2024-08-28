len = float(input("Enter the length of the zander: "))
if len >= 42:
    print("All good. Congrats")
else:
    print("This one is too small. Please release it back.")
    print("It's ", 42-len, " centimeters shorter.")