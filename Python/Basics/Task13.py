print("Welcome to the RollerCoaster!!!")
height = int(input("What is your height in cm? "))
price = 0
if height > 120:
    print("You can ride! Yayyyyyyy")
    age = int(input("What's your age? "))
    if age < 12:
        if age < 5:
            print("You are too young to ride!!!!!")
        else:
            print("Your ticket price gotta be $5.")
            price = 5
    elif age <= 18:
        print("Your ticket price gotta be $7.")
        price = 7
    elif age >=45 and age <=55:
        print(f"Your ticket price gotta be ${price}.")
    else:
        print("Your ticket price gotta be $12.")
        price = 12
    wants_picture = input("Do you want a family picture bro? (Y/N) ")
    if wants_picture == "Y":
        print(f"You gotta pay $3 for a picture")
        price += 3
    print(f"Your total cost is equal to ${price}")
else:
    print("Sorry, you gotta grow taller bro!!!")
