month = input ('Tell me wwhat month you are in and I´ll tell you waht season it belongs to: ')
month = month.lower()

if month == 'january' or month == 'february' or month == 'march':
    print (f'{month} is Winter')
elif month == 'april' or month == 'may' or month == 'june':
    print (f'{month} is Spring')
elif month == 'july' or month == 'august' or month == 'september':
    print (f'{month} is Summer')
elif month == 'october' or month == 'november' or month == 'december':
    print (f'{month} is Autumn')
else:
    print ('Invalid')