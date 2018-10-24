# Pyautogui (control keyboard and mouse)

## 0. install

for windows: `pip install pyautogui`
for mac: `pip install pyobjc pyautogui`
for linux: `pip install python3-xlib pyautogui`

## 1. pre-intro

PyAutoGUI also has a fail-safe feature. Moving the mouse cursor to the upper-left corner of the screen will cause PyAutoGUI to raise the pyautogui .FailSafeException exception. Your program can either handle this excep- tion with try and except statements or let the exception crash your program. **Either way, the fail-safe feature will stop the program if you quickly move the mouse as far up and left as you can**. You can disable this feature by set- ting `pyautogui.FAILSAFE = False`

## 2. api

`moveTo(x, y)` Moves the mouse cursor to the given x and y coordinates. `moveRel(xOffset, yOffset)` Moves the mouse cursor relative to its cur-
rent position.
`dragTo(x, y)` Moves the mouse cursor while the left button is held down.
`dragRel(xOffset, yOffset)` Moves the mouse cursor relative to its cur- rent position while the left button is held down.
`click(x, y, button)` Simulates a click (left button by default).
`rightClick()` Simulates a right-button click.
`middleClick()` Simulates a right-button click.
`doubleClick()` Simulates a double left-button click.
`mouseDown(x, y, button)` Simulates pressing down the given button at
the position x, y.
`mouseUp(x, y, button)` Simulates releasing the given button at the
position x, y.
`scroll(units)` Simulates the scroll wheel. A positive argument scrolls
up; a negative argument scrolls down.
`typewrite(message)` Types the characters in the given message string. `typewrite([key1, key2, key3])` Types the given keyboard key strings.
`press(key)` Presses the given keyboard key string.
`keyDown(key)` Simulates pressing down the given keyboard key.
`keyUp(key)` Simulates releasing the given keyboard key.
`hotkey([key1, key2, key3])` strings down in order and then releasing them in reverse order.
`screenshot()` Returns a screenshot as an Image object. (See Chapter 17 for information on Image objects.)

```python
import pyautogui

im = pyautogui.screenshot()
im.getpixel((50, 200)) # (130, 135, 144)
pyautogui.pixelMatchesColor(50, 200, (130, 135, 144)) # True
```