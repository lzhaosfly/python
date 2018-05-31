# iterator

## 1. ITERATORS? ITERABLES??

*   Iterator - an object that can be iterated upon. An object which returns data, one element at a time when next() is called on it
*   Iterable - An object which will return an Iterator when iter() is called on it.

```python
def my_for(iterable, func):
	iterator = iter(iterable)
	while True:
		try:
			thing = next(iterator)
		except StopIteration:
			break
		else:
			func(thing)

def square(x):
	print(x*x)

my_for("lol", print)
my_for([1,2,3,4,5], square)
```

## 2. custoer iterator

```python
class Counter:
	def __init__(self, low, high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIterationß

for x in Counter(50,70):
	print(x)
```

We can also use generator here, then we don't need `__next(self)__`:

```python
class Counter(object):
    def __init__(self, start, end):
        self._current = start
        self._end = end

    def __iter__(self):
        while self._current < self._end:
            yield self._current
            self._current += 1


count = Counter(10, 50)
for i in count:
    print(i)
```
