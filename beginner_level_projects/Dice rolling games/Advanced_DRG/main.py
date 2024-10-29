# Modify the dice rolling game beginner so the user can 
# specify how many dice they want to roll

# Add a feature that keeps track of how many times the user has rolled the dice
# during the session. This will require a counter that increments each time the
# dice are rolled. 

# Game start (While Loop)
    # Ask the user "Roll the dice"
    # if the user replies 'Y', the game begins
    # Ask: How many dice do you want to roll
        # Save the number of dice
        # loop through the dice number and create dice variable in a list
    # generate random numbers for each dice
    # print the dice numbers
    # Count: the number of times user roll a dice
    # if user replies 'N', the game breaks
    # Else invalid choice

import random

while True:
    count = 0
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == 'y':
        dice_no = int(input("How many dice do you want to roll? enter numbers only "))
        dice_numbers = []
        for i in range(dice_no):
            dice_numbers.append(random.randint(1,6))
        print(dice_numbers)
        count += 1
    elif choice == 'n':
        if count > 0:
            print(f"You played the game {count} time{'s' if count != 1 else ''}" )
        print("Thanks for playing")
        break
    else:
        print("Invalid choice")