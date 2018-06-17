# Function

## 1. \*args and \*\*kwargs

`**kwargs` means `key word args`

```python
def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(1, 2, a=3, b=4) # (1, 2)  {'a': 3, 'b': 4}
```

## 2. function params order

1.  parameters
2.  \*args
3.  default keyword parameters
4.  \*\*kwargs

```python
def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]

print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))  
# a - 1
# b - 2
# args (3)
# instructor - "Colt"
# kwargs - {'last_name': "Steele", "job": "Instructor"}
```

## 3. unpack args and kwargs

Using `*` to unpack args and using `**` to unpack kwargs

```python
def sum_all_values(*args):
    return sum(args)

sum_all_values([1, 2, 3, 4]) # nope...Error
sum_all_values((1, 2, 3, 4)) # this does not work either...

sum_all_values(*[1, 2, 3, 4]) # 10
sum_all_values(*(1, 2, 3, 4)) # 10
```

```python
def display_names(first, second):
    return f"{first} says hello to {second}"

names = {"first": "Colt", "second": "Rusty"}

display_names(names) # nope..Error

display_names(**names) # "Colt says hello to Rusty"
```
