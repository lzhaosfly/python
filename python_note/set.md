# Set

## 1. common method

`add(element)` to add an element to a set
`remove(element)` to remove element from set. If value not exist in s, then throw error
`discard(element)` to remove element from set but won't throw exception if the element not exist
`copy()` to copy a set
`clear()` to remove all values in set

Set can also use `|` and `&` to do calculation

```python
s = {1, 4, 5}

4 in s # True
8 in s # False

# Loop
numbers = {1,2,3,4}
for number in numbers:
    print(number)

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s1 & s2 # {2, 3}
s1 | s2 # {1, 2, 3, 4}
```

## 2. interesting syntax

```python
{x**2 for x in range(10)} # {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

string = "sequoia"
{char for char in string if char in 'aeiou'} # {'o', 'e', 'u', 'i', 'a'}
```
