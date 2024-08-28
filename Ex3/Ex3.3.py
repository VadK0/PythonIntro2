gen = input("Enter your gender: ")
hemo = float(input("Enter your hemoglobin value: "))
if gen == "male":
    if hemo < 134:
        print("Your hemoglobin is too low.")
    elif hemo <= 167:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is too high.")
elif gen == "female":
    if hemo < 117:
        print("Your hemoglobin is too low.")
    elif hemo <= 155:
        print("Your hemoglobin is normal.")
    else:
        print("Your hemoglobin is too high.")
else:
    print("Incorrect gender entered.")