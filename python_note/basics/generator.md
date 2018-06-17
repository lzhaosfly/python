# Generator

*   Generators are iterators
*   Generators can be created with generator functions
*   Generator functions use the yield keyword
*   Generators can be created with generator expressions

## 1. example

```python
def current_beat():
    nums = (1, 2, 3, 4)
    i = 0
    while True:
        if i >= len(nums):
            i = 0
        yield nums[i]
        i += 1


for i in current_beat():
    print(i)
```
