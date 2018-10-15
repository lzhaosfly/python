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
`[1, 2] + [1, 2, 3]` return [1, 2, 1, 2, 3]
`[1, 2] * 3` return [1, 2, 1, 2, 1, 2]

`clear()` to remove all items
`pop()` to remove the last items
`pop(index)` to remove the **index** items
`remove(element)` to remove **element** from array, if element not exist, then throw error
`count(element)` will give you how many element shows in this array
`slice(start:end:step)` same as js slice
`index(x)` return the index of x
`insert(i, x)` insert x to **index** i. Like js `splice(i, 1, x)`
`max([1,2,3,4])` same as js `Math.max(...[1,2,3,4])`

`reverse()` same as js
`sort()` same as js
`'&'.join(str(x) for x in [1,2,3])` same as `[1,2,3].join('&')` js

Note:

-   Only **string array** can be **join**.

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

## 5. sort

```python
users = [
	{"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
	{"username": "katie", "tweets": ["I love my cat"]},
	{"username": "jeff", "tweets": [], "color": "purple"},
	{"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
	{"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
	{"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users,key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
sorted(users,key=lambda user: len(user["tweets"]), reverse=True)
```

If you want to write your own comparator sort function, then sort this way:

```python
from functools import cmp_to_key

def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0

sorted([36, 5, 12, 9, 21], key=cmp_to_key(reversed_cmp))

numbers = [5, 2, 9, 7]
numbers = sorted(numbers, key=cmp_to_key(lambda x,y: x-y)) # 升序
numbers = sorted(numbers, key=cmp_to_key(lambda x,y: y-x)) # 降序
```
