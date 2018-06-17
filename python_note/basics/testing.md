# Testing

## 1. unit test

**When writing a test file, the file name should be `test_something` !!!**

use `unittest` library to do unit test. [unitTest](https://blog.csdn.net/qq_18150497/article/details/76714258)
[official unitTest](https://docs.python.org/3/library/unittest.html#command-line-interface)

Using `python -m unittest -v` to run all the unittest

```python
import unittest
from robot import Robot

class RobotTests(unittest.TestCase):
    def setUp(self):
        self.mega_man = Robot("Mega Man", battery=50)

    def test_charge(self):
        self.mega_man.charge()
        self.assertEqual(self.mega_man.battery, 100)

    def test_say_name(self):
        self.assertEqual(
            self.mega_man.say_name(),
            "BEEP BOOP BEEP BOOP.  I AM MEGA MAN")
        self.assertEqual(self.mega_man.battery, 49)


if __name__ == "__main__":
    unittest.main()
```
