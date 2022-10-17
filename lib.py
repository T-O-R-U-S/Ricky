from time import sleep
from sys import stdout, stdin
from os import system, name
from enum import Enum


# Stores constants for colours.
class Colour(Enum):
    YELLOW: str = '\033[1;33m'
    GREEN: str = '\033[1;32m'
    RED: str = '\033[1;31m'
    BLUE: str = '\033[0;94m'
    PURPLE: str = '\033[0;35m'
    BLACK: str = '\033[1;30m'
    DEFAULT: str = '\033[1;0m'
    INHERIT: str = ''

    def __format__(self, _):
        return self.value

    def __str__(self):
        return self.value

    def __repr__(self):
        return self.value

# Character-by-character prompts without newlines at the end
def line_print(to_print: str, colour=Colour.DEFAULT, delay=0.05):
    stdout.write(colour.value)
    for i in to_print:
        stdout.write(i)
        stdout.flush()
        sleep(delay)

# Character-by-character prompts with newlines at the end
def show(to_print: str, colour=Colour.DEFAULT, delay=0.03):
    line_print(to_print, colour, delay)
    stdout.write('\n')

# Open-ended prompts
def prompt(to_print: str, colour=Colour.DEFAULT, delay=0.02):
    line_print(to_print + ' ', colour, delay)
    stdout.write(Colour.DEFAULT.value)
    stdout.flush()
    return stdin.readline().upper().strip()

# Yes or no prompts
def yes_or_no(to_print: str, colour=Colour.DEFAULT, delay: int = 0.02):
    line_print(to_print + ' [Y/N] ', colour, delay)
    stdout.write(Colour.DEFAULT.value)
    stdout.flush()
    return stdin.readline().lower().strip() == 'y'

def clear():
    # NT-based systems (a.k.a Windows)
    if name == 'nt':
        system('cls')
    # POSIX systems
    else:
        system('clear')

# For in-game animations
def animate(animation: [str]):
    print(Colour.DEFAULT)
    for frame in animation:
        clear()
        print(frame)
        sleep(0.5)