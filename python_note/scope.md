# Scope

## 1. global

`global` keyword is used when you want to access a global keyword in a function or other small scope

```python
total = 0

def increment():
    # global total # must add this global
    total += 1
    return total

print(increment()) # Error ! function can't access total
```

## 2. nonlocal

`nonlocal` is used when you want to access a keyword in a inner function but it defined in an outer function

```python
def outer():
    count = 0
    def inner():
        nonlocal count # if don't have this line, count can not be accessed in here
        count += 1
        return count
    return inner()
```
