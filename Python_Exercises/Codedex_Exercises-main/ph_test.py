"""
In chemistry, pH is a scale used to specify the acidity or basicity of a liquid.

Create a ph_levels.py program that checks whether a pH level is basic, acidic, or neutral.

First, create a ph variable and ask the user for a value between 0 and 14.

Write an if, elif, else statement that:

If ph is greater than 7, output "Basic".
If ph is less than 7, output "Acidic".
Else, output "Neutral".

"""
ph = float (input('What is your PH level'))

if ph > 7:
    print ('Your PH is basic')
elif ph < 7:
    print ('Your PH is acidic')
else: 
    print ('Your ph is neutral')