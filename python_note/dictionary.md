# Dictionary

## 1. iterator

```python
user = {"name": "lzhao", age: 18}

for key in user.keys():
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f"{key}{value}")
```

## 2. using `in` to check if a **key** is in dict

```python
user = {"name": "lzhao", age: 18}

# Check key
"name" in user # True
"abc" in user # False

# Check value
"lzhao" in user.values() # True
```

## 3. some common method

`clear()` to clear the dictionary
`copy()` to copy the dictionary
`get(key)` to get the value which key is key. Note the difference with dictionary[]. If a key doesn't in dictionary, then **dictionary[key] will throw error**, but **dictionary.get(key) will give a None value**.
`{}.fromkeys("a", "b")` to create a dict
`pop(key)` to pop the key, value pair
`popitem()` removes a random key, value pair in dictionary
`update(dict)` update keys and values in a dictionary with another set of key, value pairs

```python
# fromkeys
{}.fromkeys("a", "b") # {"a": "b"}
{}.fromkeys(["email"], 'unknown') # {"email": "unknown"}
{}.fromkeys("a", [1, 2, 3, 4, 5]) # {"a": [1, 2, 3, 4, 5]}
{}.fromkeys(['name', 'age', 'score'], 'unknown') # {"name": "unknown", "age": "unknown", "score": "unknown"}
{}.fromkeys('phone': 'unknown') # {'p': 'unknown', 'h': 'unknown', 'o': 'unknown', 'n': 'unknown', 'e': 'unknown'}

# update
user = {'userid': '12345', 'name': 'lei'}
user.update({'name': 'lzhao', 'age': 18}) # Note: do not assign the value to original object!!!
print(user) # {'userid': '12345', 'name': 'lzhao', 'age': 18}
```

## 4. interesting syntax

```python
numbers = {'first': 1, 'second': 2, 'third': 3}
squared_numbers = {key: value**2 for key,value in numbers.items()} # {'first': 1, 'second': 4, 'third': 9}

{num: num**2 for num in [1, 2, 3, 4, 5]} # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

{num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4]} # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}
```
