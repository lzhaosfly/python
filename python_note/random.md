# Random

## 1. shuffle

```python
from random import shuffle
x = [[i] for i in range(10)]
shuffle(x) # print x  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]
```

## 2. random int / random float

```python
# random int
from random import randint
print(randint(0, 9)) # give random int between 0 to 9 (includes 0 and 9)

# random float
from random import random
print(random()) # give random float btween 0 to 1
```

## 3. random choice

```python
from random import choice
msg = choice(('Hello there ', 'Go away ', 'I love you '))
print(msg)
```
