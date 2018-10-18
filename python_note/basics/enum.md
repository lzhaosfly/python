# Enum in python

## 1. define enum

```python
from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 1


def main():
    print(Weekday.Sun) # Weekday.Sun
    print(Weekday.Sun.value) # 1
```