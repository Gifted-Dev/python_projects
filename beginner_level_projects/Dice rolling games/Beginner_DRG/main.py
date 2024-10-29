import random
# Game starts... While True i.e. game is running
    # generate a tuple of random generated number
    # Ask for player input (roll dice or not)
    # if player is yes
    # print number
    # if player player asks no
    # Break away from the game

while True:
    dice_roll = (random.randint(1, 6), random.randint(1, 6))
    player_choice = input("Roll the dice? (y/n): ").lower()
    if player_choice == 'y':
        print(dice_roll)
    elif player_choice == 'n':
        print("Thanks for playing")
        break
    else:
        print("invalid choice")

