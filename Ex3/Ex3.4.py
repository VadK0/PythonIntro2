year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 == 0:
    print("The year is leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("The year is leap year")
else:
    print("The year is not leap year")

