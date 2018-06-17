# Decorator

## Tips

If you encounter "NoneType cannot be callable", then check if you return the `wrapper`

## 0. Decorator Pattern

No paramter decorator:

```python
from functools import wraps
# wraps preserves a function's metadata
# when it is decorated

def my_decorator(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        # do some stuff with fn(*args, **kwargs)
        return fn(*args, **kwargs)
    return wrapper
```

Paramter decorator:

```python
from functools import wraps

def my_decorator(val):
	def inner_decorator(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
            # do some stuff with val and fn
			return fn(*args, **kwargs)
		return wrapper
	return inner_decorator
```

## 1. What's Decorator?

*   Decorators are functions
*   Decorators wrap other functions and enhance their behavior
*   Decorators are examples of higher order functions
*   Decorators have their own syntax, using "@" (syntactic sugar)

## 2. example

no arguments example

```python
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Matt.")

# we don't need to set
# greet = be_polite(greet)
```

any arguments example

```python
# This version only accepts one argument
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# This version works with any number of args
def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

print(greet("todd"))
print(order(side="burger", main="fries"))
```

## 3. @wraps

Why we need @wraps? @wrap is used to preserve metadata of the wrap function

see this probelem:

```python
def log_function_data(fn):
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)  # log_function_data doc, not add doc!!!
print(add.__name__) # log_function_data, not add!!!
help(add) # it's help of log_function_data!!!
```

But always we want to keep the wrapped function metadata, that's why we need @wraps

```python
from functools import wraps
def log_function_data(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper


@log_function_data
def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__) # add doc
print(add.__name__) # add
help(add) # help of add
```

## 4. pass paramters to decorator

theory:

```python
# NOT WORKING CODE!
# JUST FOR DEMO PURPOSES!

# When we write:
@decorator
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator(func)


# When we write:
@decorator_with_args(arg)
def func(*args, **kwargs):
    pass
# We're really doing:
func = decorator_with_args(arg)(func)
```

implementation:

```python
from functools import wraps

def ensure_first_arg_is(val):
	def inner(fn):
		@wraps(fn)
		def wrapper(*args, **kwargs):
			if args and args[0] != val:
				return f"First arg needs to be {val}"
			return fn(*args, **kwargs)
		return wrapper
	return inner
```
