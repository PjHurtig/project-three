import random
import time
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
        score += 1
    elif side == "empty":
        score += 0
    elif side == "trap":
        traps += 1

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
    print(f"You got: {user_dices}\n")
    for dice in user_dices:
        time.sleep(1)
        current_dice = generate_sides(dice)
        print(f"Rolling {dice} dice...")
        random_side = random.randint(0, 5)
        rolled_dice = roll_dice(current_dice[random_side])
        score += rolled_dice[0]
        traps += rolled_dice[1]
        time.sleep(1)
        if current_dice[random_side] == "trap":
            print("Oh no! It was a trap\n")
        elif current_dice[random_side] == "treasure":
            print("You found a treasure of gold!\n")
        elif current_dice[random_side] == "empty":
            print("This chest is empty\n")
    return [score, traps]


def play_game():
    score = 0
    traps = 0
    roll = input("You have entered the tomb and in front of you are two "
                 "chests do you want to open them (y/n) \n")
    if roll == "n":
        print(f"Hmmm, that was disapointing... "
              f"Thanks for having a look {player}")
    while roll == "y" and traps < 3:
        num_dice = 2
        user_dices = generate_dice(num_dice)
        result = roll_user_dices(user_dices)
        score += result[0]
        traps += result[1]
        print(f"Dice Left: {dices}")
        print(f"Total Treasures Collected: {score} \
        Total Traps Triggered: {traps}")
        roll = input("Do you dare to continue further?(y/n) \n")
        if roll == "n":
            print(f"\nWise or foolish, who knows. You leave in one piece with"
                  f" {score} treasure \nWell done {player}!")


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

    print("Welcome to Treasure Dice! \n")
    time.sleep(0.5)
    print("Explore the old tomb and roll dice to go further in at every"
          " treasure room. There are 12 dice, and at each room you must roll 2"
          " to continue. Or stop and cash out. Green dice have few traps "
          "and lots of treasures but the red are the opposite! Yellow  "
          "dice are balanced between the two.")
    time.sleep(0.5)
    print("If you trigger 3 traps the game is over! So be careful... \n")
    time.sleep(0.5)
    player = input("What is your name, brave adventurer? \n")
    print(f"Greetings {player}! Get ready to search for treasures!\n")
    play_game()
