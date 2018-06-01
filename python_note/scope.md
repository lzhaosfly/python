# Scope

## 1. global

`global` keyword is used when you want to **assign** a global varibale in a function or other small scope. Note if only read, then it's not matter.

```python
total = 0

def increment():
    # global total # must add this global
    total += 1
    return total

print(increment()) # Error ! function can't access total
```

## 2. nonlocal

`nonlocal` is used when you want to **assign** a variable defined in outside function to a inner function but it defined in an outer function. Note if only read variable, then it's not matter.

```python
def outer():
    count = 0
    def inner():
        nonlocal count # if don't have this line, count can not be assigned in here
        count += 1
        return count
    return inner()
```
