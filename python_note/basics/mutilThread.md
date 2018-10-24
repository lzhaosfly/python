# MultiThread

## 1. basic usage

```python
import time
from threading import Thread, current_thread


def func1(n: int):

    print(f'func 1 start at {current_thread().name}')
    result = 0
    for _ in range(10):
        result += n
        time.sleep(0.5)
    print(f'func 1 finish at {current_thread().name}')


def main():
    print('process start')
    # func1(1)  # running in MainThread

    t1 = Thread(target=func1, args=(1,))
    t1.start()
    t1.join()  # if we don't add join, then t1 won't wait mainThread running

    print('process end')


if __name__ == '__main__':
    main()
```

Note:

-   You can use `threading.current_thread().name` to get the thread name.
-   You can join the thread, then it will wait for its parent thread.
-   **Thread consume less resource than process**.