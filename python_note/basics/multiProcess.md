# Multiprocess (多进程)

## 1. usage

```python
import time
import os
from multiprocessing import Process, Pool


def func1(args1: str, args2: str):
    while True:
        print(
            f"this is func1 with args: {args1}, {args2}---{os.getpid()}---{os.getppid()}")
        time.sleep(1.2)


def func2(args1: str, args2):
    while True:
        print(
            f"this is func2 with args: {args1}, {args2}---{os.getpid()}---{os.getppid()}")
        time.sleep(1.2)


def main():
    # p1 = Process(target=func1, args=('func1...arg1', 'func1...agr2'))
    # p2 = Process(target=func2, args=('func2...arg1...', 'func1...agr2...'))
    # p1.start() # must start
    # p2.start() # must start

    # p1.join() # join will make parent process wait p1
    # p2.join() # join will make parent process wait p2

    # Use pool, same with above
    pool = Pool()  # default is you CPU core number
    pool.apply_async(func1, ('func1...arg1', 'func1...agr2'))
    pool.apply_async(func2, ('func2...arg1...', 'func1...agr2...'))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
```

Note:

-   use `Process(target, args)` to create a new process.
-   `Process` must call `start` to start a new process.
-   use `os.getpid()` to get the process id. Use `os.getppid()` to get the parent process id.
-   parent prcocess won't affect sun process. If parent process end, sun process may not end. If you want parent to wait sun process ends, then use `process.join()`.
-   You can also use Pool to create multi process. **If you are using Pool, make sure you close the pool. And join must be after pool close**
-   **multiprocess can't share global value.**