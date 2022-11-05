# LithicRivers (ABANDONED)

An ASCII game I never finished T_T

Successor: <https://github.com/HenryFBP/MountainFlow>

I am abandoning this project due to poor decisions on choosing UI frameworks and realizing my render functions are really annoying and unsustainable.

I plan to re-create this game outside of the terminal using a more mature dev framework that "just use asciimatics and curses bro" :P

![actual screenshot](media/screenshot.png)

## Play the game

Visit <https://replit.com/@HenryFBP/LithicRivers?embed=1> to play this game in an online terminal!

Visit <https://github.com/HenryFBP/LithicRivers/releases> to download a release for your platform.

If you have Docker, run this in bash:
    
    docker run --interactive --tty henryfbp/lithicrivers:latest

to run the game in terminal locally. Please note saved games will be lost.

Currently we support:

- Windows
- OSX 10
- OSX 11
- Debian (built on Ubuntu)

### How to play the game

read the help page

## wow, badges :P

[![Coverage Status](https://coveralls.io/repos/github/HenryFBP/LithicRivers/badge.svg?branch=release)](https://coveralls.io/github/HenryFBP/LithicRivers?branch=release)

[![forthebadge](https://forthebadge.com/images/badges/contains-technical-debt.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/built-with-swag.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/check-it-out.svg)](https://forthebadge.com)

[![forthebadge](https://forthebadge.com/images/badges/60-percent-of-the-time-works-every-time.svg)](https://forthebadge.com)

## running

    poetry install
    poetry run python -m lithicrivers

## building/release

### Docker

    docker build ./ --tag henryfbp/lithicrivers:latest
    docker run --interactive --tty henryfbp/lithicrivers:latest
    docker push henryfbp/lithicrivers

## notes

- https://github.com/peterbrittain/asciimatics/blob/v1.13/samples/tab_demo.py
- https://stackoverflow.com/questions/9575409/calling-parent-class-init-with-multiple-inheritance-whats-the-right-way/50465583#50465583
- https://github.com/zladovan/gorched
- https://github.com/matcool/term-tris
- https://github.com/topics/asciimatics
- https://github.com/meysam81/notable-newts
- https://github.com/JnyJny/GameOfLife
- https://github.com/VedantKhairnar/The-Maze-Runner

<!--

## meme

take a look at some of our reviews below...

![why do we exist...just to suffer...?](media/dafuq.png)

![gnerf](http://images3.memedroid.com/images/UPLOADED727/5c1d01829c2ff.jpeg)

god help me

-->
