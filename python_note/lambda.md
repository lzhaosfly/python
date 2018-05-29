# Lambda

If you want to use `map`, `filter` etc, then consider use list or dict comprehension

## 1. basic usage

```python
square2 = lambda num: num * num
add = lambda a, b: a + b

print(square2(2)) # 4
print(add(5, 6)) # 11
```

## 2. map

Note `map` will only return a map object, not a list object

```python
l = [1, 2, 3, 4]

doubles = list(map(lambda x: x * 2, l))

doubles # [2, 4, 6, 8]
```

## 3. filter

Note `filter` will only return a filter object, not a list object

```python
l = [1,2,3,4]

evens = list(filter(lambda x: x % 2 == 0, l))

evens # [2,4]
```

## 4. all/any

```python
people = ["Chare", "Casey", "Cathy", "Carly"]
all([name[0]=='c' for name in people]) # True
all(name[0]=='c' for name in people) # True, This is a generator. Generator format is prefer here as it's small than list
any([name[0]=='c' for name in people]) # True
```

## 5. reduce

```python
from functools import reduce
l = [2, 2, 3, 4]

product = reduce(lambda prev, elem : prev * elem, l, 1)
```
