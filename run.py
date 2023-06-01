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


chosen_dice_color = pick_dices()
print(chosen_dice_color)


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


dice_sides = generate_sides()


def picked_side():
    dice_side = random.randint(0, len(dice_sides) - 1)
    return dice_sides[dice_side]


side = picked_side()
print(side)


def roll_dice():
    score = 0
    traps = 0
    if side == "treasure":
        print("you found a treasure of gold!")
        score += 1
    elif side == "empty":
        print("this chest is empty")
    else:
        print("Oh no! it was a trap")
        traps += 1
    print(f"Treasures Collected: {score}")
    print(f"Traps Triggered: {traps}")


# roll_dice()


def play_game():
    roll = input("roll?(y/n) \n")
    if roll == "y":
        roll_dice()
    elif roll == "n":
        print("game over")


play_game()
