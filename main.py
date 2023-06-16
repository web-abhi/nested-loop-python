print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))


if height >= 120:
    print("You're eligible for rollercoaster ride!")
    age = int(input("What is your age in years? "))
    if age >= 18:
        print("You have to pay $20.")
    else:
        print("You have to pay $7")
else:
    print("Sorry, you're under age for rollercoaster.")