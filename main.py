from random import randint


while True:
    rolled = []
    print("Welcome to the Dice Simulator")
    sides = int(input("Please choose how many sides:\nD"))
    number = int(input("How many dice would you like to roll?\n"))
    print("\nRolling " + str(number) + " dice with " + str(sides) + " sides...\n\n")

    for num in range(number):
        rolled.append(randint(1, sides))

    print(rolled)
    if input("Would you like to roll again? (Y/N) ").upper() == "N":
        print("Goodbye")
        break
