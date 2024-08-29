names = set()

while True:
    name = input("Enter a name or press Enter to finish: ")
    if name == '':
        print('Program stopped')
        break
    else:
        if name in names:
            print('Existing name')
        else:
            print('New name')
        names.add(name)

print(names)