# Sorted

It's Sorted not sort!!!

## 1. array sort

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

## 2. dictionary sort

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
