import random

player_score = 0
cpu_score = 0 

print ("The rules are:")
print ("Rock beats scissors.")
print ("Scissors beat paper.")
print ("Paper beats Rock \n")


print ("Choose from 1 to 3 one of the following options:")
print ("1. Choose Rock.")
print ("2. Choose Paper.")
print ("3. Choose Scissors. \n")

player = int(input ("Make your choice: "))
cpu = random.randint (1,3)

if player == 1 and cpu == 2:
    print ("You chose rock.")
    print ("CPU chose paper.")
    print ("Computer wins!")
elif player == 2 and cpu == 3:
    print ("You chose paper.")
    print ("CPU chose scissors.")
    print ("Computer wins!")
elif player == 3 and cpu == 1:
    print ("You chose scissors.")
    print ("CPU chose rock.")
    print ("Computer wins!")
elif player == 1 and cpu == 3:
    print ("You chose rock.")
    print ("CPU chose scissors.")
    print ("Player wins!")
elif player == 3 and cpu == 2:
    print ("You chose scissors.")
    print ("CPU chose paper.")
    print ("Player wins!")
elif player == 2 and cpu == 1:
    print ("You chose paper.")
    print ("CPU chose rock.")
    print ("Player wins!")
else:
    print ("It´s a tie.")