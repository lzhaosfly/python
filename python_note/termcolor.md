# [Termcolor package](https://pypi.org/project/termcolor/)

## 0. install

`conda install termcolor`

Using `help(termcolor)` to check documents

## 1. usage

```python
from termcolor import colored

text = colored("HI THERE", color='magenta',
               on_color='on_cyan', attrs=['blink'])
print(text)
```
