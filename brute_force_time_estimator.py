import math 
length = int(input("Enter the length of the password:"))
character_set_size = int(input("Enter the size of the character set (eg. 26 for lowercase) : "))
combinations = character_set_size **length
guesses_per_sec = 1000000000
seconds = combinations / guesses_per_sec 
minutes = seconds /60
hours = minutes /60
days = hours /24
print('\nTotal combinations:', combinations )
print("Brute force time:")
print(      'Seconds:', round(seconds, 2))
print(      'Minutes:', round(minutes, 2))
print('     Hours:', round(hours, 2))
print(      'Days:', round(days, 2))
if seconds <60:
    print("verdict: instantly-completely insecure!")
elif days < 1:
    print("verdict: crackable within hours, not secure")
elif days < 365 and days > 186:
    print("verdict: crackable within a year")
else:
    print("verdict: very strong - computationally infeasible to brute force")

