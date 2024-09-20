'''
The Magic 8 Ball is a popular office toy and children's toy invented in the 1940s for fortune-telling and advice seeking. 🎱

It's an oversized 8 ball with some of the following answers:

Yes - definitely.
It is decidedly so.
Without a doubt.
Reply hazy, try again.
Ask again later.
Better not tell you now.
My sources say no.
Outlook not so good.
Very doubtful.
Create a magic8.py program that can respond to any Yes or No questions with a different answer each time it executes.

'''

import random
x = random.randint (1,9)

question = input ('Ask your questión to the magic 8 ball: ')

if x == 1:
    print ('Yes - definitely.')
elif x == 2:
    print ('It is decidely so.')
elif x == 3:
    print ('Without a doubt.')
elif x == 4:
    print ('Reply hazy, try again.')
elif x == 5:
    print ('Ask again later.')
elif x == 6:
    print ('Better not tell you now.')
elif x == 7:
    print ('My sources say no.')
elif x == 8:
    print ('Outlook not so good.')
elif x == 9:
    print ('Very doubtful.')