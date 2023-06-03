# Treasure Dice

### This is a terminal dice game loosely based on the Steve Jackson Games dice-game "Zombie Dice".

[Steve Jackson Games](http://www.sjgames.com/dice/zombiedice/)

the goal of the game is to roll dice that represents treasures that the adventurer finds the deeper they go into the tomb. at each round the adventurer can either roll 2 dice to open the chests or end their turn and get the points they have collected so far, but if 3 traps are triggered the game is over and all loot is lost!

[live project here](https://treasure-dice.herokuapp.com/)

![flowchart](https://i.imgur.com/eXrEECr.png)

![flowchart](https://i.imgur.com/SDLr3up.png)

## User Experience - UX

---

## User Stories

- As a user I want to understand the purpose and rules of the game
- As a user I want to enter my name.
- As a user I want to roll dice to see if i collect treasures or trigger traps
- As a user I want to see my score and how many traps i have triggered so far
- As a user I want to be able to end my adventure and get my score or keep going


## Design

The game loosely based on the analog dice-game ["Zombie Dice"](http://www.sjgames.com/dice/zombiedice/) and turned into this single player "push-your-luck" terminal game with a new theme and a few different rules.

---

### Flowshart

![flowchart](https://i.imgur.com/2v5cJaN.png)

## Features

---

### Welcome message and rules

This i what is first shown upon running the program. A simple explanation of the rules with a little bit of thematic flavour.

![flowchart](https://i.imgur.com/DfzGvow.png)

### Enter Name

After reading the introductory message the user is prompted to enter their name which is then used to refer to the player throughout the game.

![flowchart](https://i.imgur.com/t7q5k7h.png)

### Timing

The time.sleep has been used to add suspense between rolls and to separate the executed functions with delay for readability and a better user experience.

### Start rolling for treasure

The first time the user rolls there is a text telling them that they have entered the tomb and the user gets to choose to start opening chests (by rolling dice) or not.

![flowchart](https://i.imgur.com/MZ1BV32.png)

### Dice left

Every time the user rolls, the dice that are left and what colour they are is printed so that the user can make a decision if the risk is worth it to continue. Remember, the different coloured dice have different risk and reward!

![flowchart](https://i.imgur.com/G31Y0Yt.png)

### Total treasures and traps triggered


Every time the user rolls, the total traps triggered and total treasures collected is printed so that the user is always up to date with the score and risk of rolling again.

![flowchart](https://i.imgur.com/zdseOQf.png)

### Too many traps triggered

If the user chose to push their luck a little too far and triggered 3 or more traps, then the game is over and the user gets an end game message.

![flowchart](https://i.imgur.com/MvyJEAc.png)

### End game with collected treasures

If the user does not push their luck beyond the limit and wants to end with the treasure collected theu get a message with the final score. But could they have gotten more? 

![flowchart](https://i.imgur.com/q0PwWwW.png)

### No dice left

If the player survives through all the six rooms the game gives this end message that tells the player that they completed the tomb and gives the final score. 

![flowchart](https://i.imgur.com/b7xQdAT.png)

### Did not play

If the player for some reason goes to the trouble of entering their name and then does not want to play, they can choose "n" at the very first dice roll prompt to get this message:

![flowchart](https://i.imgur.com/b9vQW16.png)


## Rules of the game

---

### Dice

There are 12 dice each with six sides in the game. Each dice have a color that represents the number of traps, treasures and empty the user can get by rolling them.

- Green Dice: This is the most favourable dice, 3 treasures, 2 empty and only 1 trap.

- Yellow Dice: This is the middle-of-the-line dice, 2 treasures, 2 empty and 2 traps.

- Red Dice: The most dangerous dice, 3 traps, 2 empty and only 1 treasure.

### Traps

When a trap is rolled, the "total traps counter" adds 1 and if the user gets 3 the game is over.

### Treasures

When a treasure is rolled, the "total treasures counter" adds 1 and the goal is to collect as many as possible before they run out of dice or the total traps is 3 or more.

## Technologies Used

---

### Language

Python

#### Python Packages

### Other technologies used

## Testing

---

### CI Python Lint
https://pep8ci.herokuapp.com/

![flowchart](https://i.imgur.com/vNDHrqQ.png)

### Lighthouse

![flowchart](https://i.imgur.com/WeIe1zR.png)

## Manual Testing

### Validate inputs

### No dice left

### Did not play

### End game with collected treasures

### Too many traps triggered

## Bugs

---

### Index is out of range

![flowchart](https://i.imgur.com/VI8rxZk.png)

### Total traps are not updating

![flowchart](https://i.imgur.com/Ct8CLrs.png)

![flowchart](https://i.imgur.com/xdhPvOU.png)

## Deploying the project

---

### Deploying with Heroku

### Clone the project

## Credits

---

### Content

- The game loosely based on the Steve Jackson Games dice-game ["Zombie Dice"](http://www.sjgames.com/dice/zombiedice/).




### Code

- time sleep : https://www.guru99.com/python-time-sleep-delay.html

## Special thanks

---