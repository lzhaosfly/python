# Array

## 1. check if an elements in an array

use `in` to check

```python
a = [1, 2, 3]
if 4 in a:
    print(f"4 in {a}")
```

## 2. some common method

`[1].append(2) = [1].push(2) (js)`
`[1, 2].extend([1, 2, 3]) = [...[1, 2]], ...[1, 2, 3]] (js)`

`clear()` to remove all items
`pop()` to remove the last items
`pop(index)` to remove the **index** items
`remove(element)` to remove **element** from array, if element not exist, then throw error
`count(element)` will give you how many element shows in this array
`slice(start:end:step)` same as js slice

`reverse()` same as js
`sort()` same as js
`join()` same as js

## 3. reverse a string/list trick

```python
string = "This is fun!"
reversedString = string[::-1]
```

## 4. interest syntax for python

```python
numbers = [1, 2 ,3]

doubled_numbers = [number*2 for number in numbers] # It's like the map function in js

string_list = [str(num) for num in numbers] # ['1', '2', '3']

[bool(val) for val in [0, [], ""]] # [False, False, False]

evens = [num for num in numbers if num % 2 == 0]
odds = [num for num in numbers if num % 2 == 1]
```
