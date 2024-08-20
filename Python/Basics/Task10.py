# Write a program that uses if-else to check if a random number between 1 and 100 is even or odd.
import random

num = random.randint(1, 100) # We can also do a print(num) here to check the number as well
if num % 2 == 0:
    print("This is an Even Number")
else:
    print("This is an Odd Number")
