print ('BANK OF CODEDEX')

correct_password = '1234'
password = input ('Please enter you password: ')
while password != correct_password:
    password = input ('Wrong password. Please enter you password: ')

if password == correct_password:
    print ('Login succesfull.')