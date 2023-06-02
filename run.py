import random
from random import randint


def pick_dices():

    chosen_dice = random.randint(0, len(dices) - 1)
    chosen_dice_color = (dices[chosen_dice])
    return chosen_dice_color


def generate_sides(chosen_dice_color):
    if chosen_dice_color == "yellow":
        return [
            'treasure',
            'treasure',
            'empty',
            'empty',
            'trap',
            'trap'
        ]
    elif chosen_dice_color == "green":
        return [
            'treasure',
            'treasure',
            'empty',
            'empty',
            'treasure',
            'trap'
        ]
    else:
        return [
            'treasure',
            'trap',
            'empty',
            'empty',
            'trap',
            'trap'
        ]


def roll_dice(side):
    score = 0
    traps = 0
    if side == "treasure":
        print("you found a treasure of gold!\n")
        score += 1
    elif side == "empty":
        print("this chest is empty\n")
        score += 0
    elif side == "trap":
        print("Oh no! it was a trap\n")
        traps += 0

    return [score, traps]


def generate_dice(num_dice):
    dice = []
    generated = 0
    # add validation!
    while generated < num_dice:
        index = random.randint(0, len(dices) - 1)
        dice.append(dices[index])
        del dices[index]
        generated = generated + 1
    return dice


def roll_user_dices(user_dices):
    traps = 0
    score = 0
    for dice in user_dices:
        current_dice = generate_sides(dice)
        random_side = random.randint(0, 5)
        rolled_dice = roll_dice(current_dice[random_side])
        score += rolled_dice[0]
        traps += rolled_dice[1]
        print(f"Rolled {dice} dice.")
        print(f"Treasures Collected: {rolled_dice[0]} \
            Traps Triggered: {rolled_dice[1]}")
    return [score, traps]


def play_game():
    score = 0
    traps = 0
    roll = input("Do you want to make a roll?(y/n) \n")
    while roll == "y" and traps < 3:
        # while True:
        #     num_dice = input("how many dice? (1-3) \n")
        #     try:
        #         num_dice = int(num_dice)
        #         break
        #     except ValueError:
        #         print(f"Number of dice must be 1, 2 or 3 you put '{num_dice}'")
        num_dice = 2
        user_dices = generate_dice(num_dice)
        result = roll_user_dices(user_dices)
        score += result[0]
        traps += result[1]

        print(f"Total Treasures Collected: {score} \
           Total Traps Triggered: {traps}")
        roll = input("Roll again?(y/n) \n")


if __name__ == "__main__":

    dices = [
        "yellow",
        "yellow",
        "yellow",
        "green",
        "green",
        "green",
        "green",
        "green",
        "green",
        "red",
        "red",
        "red"
    ]

    print("Welcome to Adventure Dice")
    player = input("What is your name? \n")
    print(f"Hello {player} I hope you are ready to search for treasures!")
    play_game()
