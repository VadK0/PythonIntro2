numbers = []

num = input("Enter number or quit by pressing Enter: ")
while num!="":
    numbers.append(int(num))
    num = input("Enter number or quit by pressing Enter: ")
    if num == "":
        break

numbers.sort(reverse=True)

for i in range(5):
    print(numbers[i])
