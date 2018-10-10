from termcolor import colored
from pyfiglet import figlet_format

msg = input("What would you like to print? ")
color = input("What color? ")


def generate_art(msg: str, color):
    valid_color = ('red', 'green', 'yellow', 'blue',
                   'magenta', 'cyan', 'white')
    if color not in valid_color:
        color = 'blue'
    ascii_art = figlet_format(msg)
    # colored_ascii = colored(ascii_art, color=color)
    colored_ascii = colored(ascii_art, color=color)
    return colored_ascii


print(generate_art(msg, color))
