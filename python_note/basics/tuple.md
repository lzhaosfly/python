# Tuple

**Tuple cannot add/remove/update an element!!!**

## 1. common method

`count(element)` Returns the number of times a value appears in a tuple
`index(element)` Returns the index at which a value is found in a tuple

```python
first_tuple = (1, 2 ,3 ,4 ,5)
first_tuple[0] # 1
first_tuple[3] # 4

for i in first_tuple:
    print(i)

x = (1,2,3,3,3)
x.count(1) # 1
x.count(3) # 3

x.index(1) # 0
x.index(5) # ValueError: tuple.index(x): x not in tuple
x.index(3) # 2 - only the first matching index is returned
```

Note:

-   when you create a single element tuple. **Make sure you has a comma**. `(2,)`
