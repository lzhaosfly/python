# Multiprocess (多进程)

## 1. basic usage

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
    p1 = Process(target=func1, args=('func1...arg1', 'func1...agr2'))
    p2 = Process(target=func2, args=('func2...arg1...', 'func1...agr2...'))
    p1.start() # must start
    p2.start() # must start

    p1.join() # join will make parent process wait p1
    p2.join() # join will make parent process wait p2


if __name__ == '__main__':
    main()
```

Note:

-   use `Process(target, args)` to create a new process.
-   `Process` must call `start` to start a new process.
-   use `os.getpid()` to get the process id. Use `os.getppid()` to get the parent process id.
-   parent prcocess won't affect sun process. If parent process end, sun process may not end. If you want parent to wait sun process ends, then use `process.join()`.
-   You can also use Pool to create multi process. Check below.
-   **multiprocess can't share global value.** If you want to share, pleas use `multiprocessing.Queue`. Check the mutilprocess communication part.

## 2. multiProcess pool

Pool is just like a syntax sugar for basic process

```python
import time
import os
from multiprocessing import Pool


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

    # Use pool, same with above
    pool = Pool()  # default (no params) is you CPU core number
    pool.apply_async(func1, ('func1...arg1', 'func1...agr2'))
    pool.apply_async(func2, ('func2...arg1...', 'func1...agr2...'))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
```

Note:

-   You don't need to start the pool. But you need to close the pool.
-   **If you are using Pool, make sure you close the pool. And join must be after pool close**

## 3. multiprocess communication (use `multiprocessing.Queue`)

```python
import time
from multiprocessing import Process, Queue

def write(q: Queue):
    print('write start...')
    for char in ('A', 'B', 'C', 'D'):
        q.put(char)
        time.sleep(1)
    print('write end...')


def read(q: Queue):
    print('read start...')
    while True: # must be dead for loop
        value = q.get()
        print(f'read value ' + value)
    print('read end...')


def main():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    pw.start()
    pr.start()

    pw.join()
    # pr.join() # as pr is a dead loop, so join won't work

    while True:  # need parent process to check if q was empty or not
        if q.empty():
            pr.terminate()
            break


if __name__ == '__main__':
    main()
```

Note:

-   You need to use `multiprocess.Queue` to communicate with each other.
-   `queue.get()` by default will block the code to run until it get a value.
-   For consumer, please use `while True` to always get it. And when the producer finish its process, you need to terminate the consumer process to exit. Make sure you check the queue is finish consumed.