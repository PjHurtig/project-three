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

    chosen_dice = random.randint(0, len(dices) - 1)
    chosen_dice_color = (dices[chosen_dice])

    return chosen_dice_color


chosen_dice_color = pick_dices()
print(chosen_dice_color)


def generate_sides():
    if chosen_dice_color == "yellow":
        return ['ybrains', 'ybrains', 'yfeet', 'yfeet', 'ybombs', 'ybombs']
    elif chosen_dice_color == "green":
        return ['gbrains', 'gbrains', 'gbrains', 'gfeet', 'geet', 'gbombs']
    else:
        return ['rbrains', 'rfeet', 'rfeet', 'rbombs', 'rbombs', 'rbombs']


dice_sides = generate_sides()


def picked_side():
    dice_side = random.randint(0, len(dice_sides) - 1)
    return dice_sides[dice_side]


side = picked_side()
print(side)


def roll_dice():
    dice1 = pick_dices()
    dice1_face = picked_side()

    print(dice1, dice1_face)


roll_dice()