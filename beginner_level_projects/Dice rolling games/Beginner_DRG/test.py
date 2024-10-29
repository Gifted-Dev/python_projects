import random
# Game starts... While Game = True
    # generate a tuple of random generated number
    # Ask for player input (roll dice or not)
    # if player is yes
    # print number
    # if player player asks no
    # Game = False

game = True

while game:
    dice_roll = (random.randint(1, 6), random.randint(1, 6))
    player = input("Roll the dice? (y/n): ").lower()
    if player != "y" and player != "n":
        print("Invalid choice!")
    elif player == 'y':
        print(dice_roll)
    elif player == 'n':
        print("Thanks for playing")
        game = False

