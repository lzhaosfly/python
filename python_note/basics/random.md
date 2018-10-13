# Random

## 1. shuffle

```python
from random import shuffle
x = [[i] for i in range(10)]
shuffle(x) # print x  gives  [[9], [2], [7], [0], [4], [5], [3], [1], [8], [6]]
```

## 2. random int / random float / random range/ random uniform

```python
# random int
from random import randint
print(randint(0, 9)) # give random int between 0 to 9 (includes 0 and 9)

# random float
from random import random
print(random()) # give random float btween 0 to 1

# random range select one
from random import randrange
print(randrange(0, 10, 2)) # select one number from range 0 to 10 and step is 2. which means random selec one number in [0, 2, 4, 6, 8]

# random uniform
import random
print(random.uniform(3, 9)) # generate one random float number between 3 to 9. It's a float not int
```

## 3. random choice

```python
from random import choice
msg = choice(('Hello there ', 'Go away ', 'I love you '))
print(msg)
```
