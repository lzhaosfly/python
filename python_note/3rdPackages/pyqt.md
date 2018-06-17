# Pyqt

## 0. install

`pip install pyqt5`

## 1. QT Designer

-   using `open -a Designer` to open a qt designer
-   using `cmd+r` to open run your design
-   using `pyuic5 something.ui -x -o something.py` to convert a qt designer file to a pyqt5 file

```python
# Using connect to bind an action
self.pushButton.clicked.connect(
            lambda: print("push button clicked!!!"))
```
