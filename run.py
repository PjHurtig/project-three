import random

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

    chosen_dice = random.randint(0, len(dices))
    chosen_dice_color = (dices[chosen_dice])

    return chosen_dice_color


