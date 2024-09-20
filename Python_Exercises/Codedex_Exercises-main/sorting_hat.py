"""

The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

🦁 Gryffindor
🦅 Ravenclaw
🦡 Hufflepuff
🐍 Slytherin
Write a program that asks the user some questions with the int() and input() functions:

Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk

If answer is equal to 1, Gryffindor and Ravenclaw both get a +1.
Else if answer is equal to 2, Hufflepuff and Slytherin both get a +1.
Else, output the message "Wrong input."
Q2) When I’m dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold

If the answer is 1, Hufflepuff +2.
Else if answer is 2, Slytherin +2.
Else if answer is 3, Ravenclaw +2.
Else if answer is 4, Gryffindor +2.
Else, output the message "Wrong input."
Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum

If the answer is 1, Slytherin +4.
Else if the answer is 2, Hufflepuff +4.
Else if the answer is 3, Ravenclaw +4.
Else if the answer is 4, Gryffindor +4.
Else, output "Wrong input."
Lastly, print out the house with the most points!

"""
print ("Answer these questions to find out which house of magic do you belong to.")
print ("Q1) Do you like Dawn or Dusk?")
print ("1) Dawn")
print ("2) Dusk")

gryffindor_score = 0
ravenclaw_score = 0
hufflepuff_score = 0
slytherin_score = 0

q1 = int (input("Answer the question with 1 or 2: "))

if q1 == 1 :
    gryffindor_score += 1
    ravenclaw_score += 1
elif q1 == 2 :
    hufflepuff_score += 1
    slytherin_score += 1
else:
    print ("Wrong input.")

print("Q2) When I’m dead, I want people to remember me as:")
print ("1) The Good")
print ("2) The Great")
print ("3) The Wise")
print ("4) The Bold")

q2 = int (input("Answer the question with 1 to 4: "))

if q2 == 1 :
    hufflepuff_score += 2
elif q2 == 2 :
    slytherin_score += 2
elif q2 == 3 :
    ravenclaw_score += 2
elif q2 == 4 :
    gryffindor_score += 2
else:
    print ("Wrong input.")

print ("Q3) Which kind of instrument most pleases your ear?")
print ("1) The violin")
print ("2) The trumpet")
print ("3) The piano")
print ("4) The drum")

q3 = int (input("Answer the question with 1 to 4: "))

if q3 == 1 :
    slytherin_score += 4
elif q3 == 2 :
    hufflepuff_score += 4
elif q3 == 3 :
    ravenclaw_score += 4
elif q3 == 4 :
    gryffindor_score += 4
else:
    print ("Wrong input.")

max_score = max (gryffindor_score, hufflepuff_score, slytherin_score, ravenclaw_score)

if slytherin_score == max_score:
    print (" You are 🐍 Slytherin")
elif hufflepuff_score == max_score:
    print (" You are 🦡 Hufflepuff")
elif ravenclaw_score == max_score:
    print (" You are 🦅 Ravenclaw")
elif gryffindor_score == max_score:
    print (" You are 🦁 Gryffindor")
