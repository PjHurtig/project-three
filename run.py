import random
from random import randint


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


def pick_dices():

    chosen_dice = random.randint(0, len(dices) - 1)
    chosen_dice_color = (dices[chosen_dice])

    return chosen_dice_color


def generate_sides():
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


def picked_side():
    dice_side = random.randint(0, len(dice_sides) - 1)
    return dice_sides[dice_side]


def roll_dice(num):
    score = 0
    traps = 0
    for x in range(num):
        side = picked_side()
        if side == "treasure":
            print("you found a treasure of gold!\n")
            score += 1
        elif side == "empty":
            print("this chest is empty\n")
        elif side == "trap":
            print("Oh no! it was a trap\n")
            traps += 1

    return [score, traps]


def play_game():
    score = 0
    traps = 0
    roll = input("Do you want to make a roll?(y/n) \n")
    while roll == "y" and traps < 4:
        num_dice = input("how many dice? \n")
        dice_result = roll_dice(int(num_dice))
        score += dice_result[0]
        traps += dice_result[1]

        print(f"Treasures Collected: {score} \
            Traps Triggered: {traps}")
        roll = input("Roll again?(y/n) \n")


if __name__ == "__main__":

    chosen_dice_color = pick_dices()
    dice_sides = generate_sides()
    print("Welcome to Adventure Dice")
    player = input("What is your name? \n")
    print(f"Hello {player} I hope you are ready to search for treasures!")
    play_game()
