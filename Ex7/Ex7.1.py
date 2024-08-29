
seasons = ("spring", "summer", "autumn", "winter")

num = int(input("Enter number of month: "))

if 3 <= num <= 5:
    print(seasons[0])
elif 6 <= num <= 8:
    print(seasons[1])
elif 9 <= num <= 11:
    print(seasons[2])
elif num == 12 or num == 1 or num == 2:
    print(seasons[3])
else:
    print('Not correct number of month')
'''season = num // 3 - 1

print(seasons[season-1])'''