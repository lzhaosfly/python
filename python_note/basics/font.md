# [Font/pyfiglet](https://pypi.org/project/pyfiglet/)

## 0. install

`pip install pyfiglet`

Using `help(pyfiglet)` to check documents

## 1. usage

```python
from termcolor import colored
from pyfiglet import figlet_format

msg = input("What would you like to print? ")
color = input("What color? ")

valid_color = ('red', 'green', 'yellow', 'blue',
                'magenta', 'cyan', 'white')

if color not in valid_color:
    color = 'blue'
ascii_art = figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(colored_ascii)
```
