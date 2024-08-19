# Create a program that checks if a number is positive or negative using if-else.

num = float(input("Enter a number to check if positive or negative?")) # using float instead of int to avoid ValueError
if num > 0:
    print("Number is Positive")
elif num ==0:
    print("Entered number is Zero")
else: print("Number is negative")
