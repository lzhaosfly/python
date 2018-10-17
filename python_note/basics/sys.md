# Sys

## 1. getsizeof

```python
import sys

x ="abd"
print (len(x)) # len() queries for the number of items contained in a container
print (sys.getsizeof(x)) # on the other hand returns the memory size of the object
```

## 2. argv

get argv

```python
import sys

for i in sys.argv:
    print(i)
```

## 3. sys path

check the module path `sys.path`
