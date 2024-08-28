username = 'python'
password = 'rules'
i = 1

while i <= 5:
    username1 = input('Username: ')
    password1 = input('Password: ')
    if username1 == username and password1 == password:
        print('Welcome')
        break
    print('Wrong username or password')
    i += 1
else:
    print('Access denied')
