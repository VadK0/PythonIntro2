airports = {}

while True:
    answer1 = input('1.New airport\n2.Existing airport\n3.Exit\nEnter a number:')
    if answer1 == '3':
        print('Program stopped')
        break
    elif answer1 == '1':
        icao = input('Enter ICAO code of the airport:')
        airportName = input('Enter name of the airport:')
        airports[icao] = airportName
    elif answer1 == '2':
        icao = input('Enter ICAO code of the airport:')
        print('Airport name for ', icao, ' is ', airports[icao])
    else:
        print('Invalid input')
