weight = float(input('What is your weight on Earth? '))
print ('1. Mercury \n2. Venus \n3. Mars\n4. Jupiter\n5. Saturn\n6. Uranus\n7. Neptune')
planet = int(input('Choose from the previous list a planet using number from 1 to 7: '))

if planet == 1 :
    weight = weight * 0.38
    print ('Your weight in Mercury will be', weight, 'kg.')
elif planet == 2 : 
    weight = weight * 0.91
    print ('Your weight in Venus will be', weight, 'kg.')
elif planet == 3 : 
    weight = weight * 0.38
    print ('Your weight in Mars will be', weight, 'kg.')
elif planet == 4 : 
    weight = weight * 2.35
    print ('Your weight in Jupiter will be', weight, 'kg.')
elif planet == 3 : 
    weight = weight * 1.07
    print ('Your weight in Saturn will be', weight, 'kg.')
elif planet == 3 : 
    weight = weight * 0.89
    print ('Your weight in Uranus will be', weight, 'kg.')
elif planet == 3 : 
    weight = weight * 1.14
    print ('Your weight in Neptune will be', weight, 'kg.')
else:
    print ('Invalid planet.')