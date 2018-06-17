# Collections

[Collections module](https://docs.python.org/3/library/collections.html)

## 1. Counter

```python
from collections import Counter

c = Counter([1, 1, 1, 2, 12, 213124, 123, 123, 213])
print(c) # Counter({1: 3, 123: 2, 2: 1, 12: 1, 213124: 1, 213: 1})

c = Counter('asdxqwedascasdqwd')
print(c) # Counter({1: 3, 123: 2, 2: 1, 12: 1, 213124: 1, 213: 1})

print(c.most_common(2)) # [('d', 4), ('a', 3)]
print(sum(c.values())) # 17
```

## 2. OrderDict

`OrderDict()` is a dictionary that having key orders
