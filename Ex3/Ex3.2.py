x = input("Enter your cabin class: ")
if x == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif x == "A":
    print("A: above the car deck, equipped with a window.")
elif x == "B":
    print("B: windowless cabin above the car deck.")
elif x == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class")