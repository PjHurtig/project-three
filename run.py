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


chosen_dice_color = pick_dices()
print(chosen_dice_color)


def generate_sides():
    if chosen_dice_color == "yellow":
        return ['brains', 'brains', 'feet', 'feet', 'bombs', 'bombs']
    elif chosen_dice_color == "green":
        return ['brains', 'brains', 'brains', 'feet', 'feet', 'bombs']
    else:
        return ['brains', 'feet', 'feet', 'bombs', 'bombs', 'bombs']


generate_sides()