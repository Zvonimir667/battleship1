# Battleship Game
This is a Python terminal game, which runs in the Code Institute terminal on Heroku.

The goal is to beat the computer by finding all of his ships before he finds yours.

## How to play

This is standars battleship game with 4 ships that occupies only one square on the board. Computer ships are hidden and you can only see the where you guess on his board.

Ships are indicated by a letter "S" and hits are indicated by letter "X".

Player and computer take turn in guessing and winner is the one who sinks all oponents ships.

## Features

- Ships are randomly placed on the board
- Player cannot see the computer ships
- Player cannot enter same coordinates twice, or hit outside the board

## Testing

- No errors were retured when I tested a code throught a PEP8 linter

![screenshot1](/assets/images/pic1)


## Deployment 

- The steps to deploy are as follows:
    - Fork or clone this repository
    - Create a new Heroku app
    - Add Config Var with key PORT and the value 8000
    - Set the buildbacks to Python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy

## Credits 

- Code Institute for deployment terminal
- Wikipedia for the details of the Battleship game

