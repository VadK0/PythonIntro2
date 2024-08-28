def evenNumber(numbers):
    eNumbers = []
    for number in numbers:
        if number % 2 == 0:
            eNumbers.append(number)
    return eNumbers

list = [1,2,3,4,5,6,7,8,9,10]
print('Original List: ', list)
print('Even numbers list: ', evenNumber(list))