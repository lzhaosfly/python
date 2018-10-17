# queue in python

## 1. if you are playing with data structure

If you are playing with data structure, then please use `Collections.deque()`

```python
from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

queue.popleft() # 1
queue.pop() # 3
```

Note:

-   when want something go into queue, please use `append`
-   The difference of `popleft()` and `pop()` is one for get the head of queue, the other is to get the tail of the queue

## 2. If you are playing with multi-thread

If you are playing with multi-thread, then you can use `Queue.queue`

[Check this page](https://docs.python.org/3/library/queue.html)

## 3. priority queue in data structure

Use `heapq` to create priority queue.

Check this [official doc](https://docs.python.org/3/library/heapq.html)

And this [stack overflow](https://stackoverflow.com/questions/11989178/how-to-heapify-by-field-from-custom-objects)

## 4. priority queue in multi thread

If you are playing with multi-thread, then you can use `Queue.PriorityQueue`

[official doc](https://docs.python.org/3/library/queue.html#Queue.PriorityQueue)

