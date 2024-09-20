import random

guess = 0 
tries = 0

x = random.randint (0,21)

while guess != x and tries < 5: # Mientras el bucle sea True
    guess = int(input('Guess the number from 1 to 20: '))
    if guess > x:
        tries += 1
        print ('Sorry, ',guess,' is too high.')
    elif guess < x:
        tries += 1
        print ('Sorry, ',guess,' is too low.')
    
# Si se acierta el numero el bucle pasa a ser False, 
# pasa a la siguiente instrucción:

if tries > 5:
    print ('Sorry you have ran out of luck.')
else:
    print ('Wow, ',guess, "you´ve guessed it!")