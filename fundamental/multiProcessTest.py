import time
import os
from multiprocessing import Process, Pool, Queue


# def func1(args1: str, args2: str):
#     while True:
#         print(
#             f"this is func1 with args: {args1}, {args2}---{os.getpid()}---{os.getppid()}")
#         time.sleep(1.2)


# def func2(args1: str, args2):
#     while True:
#         print(
#             f"this is func2 with args: {args1}, {args2}---{os.getpid()}---{os.getppid()}")
#         time.sleep(1.2)


# def main():
#     p1 = Process(target=func1, args=('func1...arg1', 'func1...agr2'))
#     p2 = Process(target=func2, args=('func2...arg1...', 'func1...agr2...'))
#     p1.start()
#     p2.start()

# #     p1.join()
# #     p2.join()

#     # do something block main process. If above had join, then this parent won't execute.
#     while True:
#         print(f"this is main process --- {os.getpid()}")
#         time.sleep(1)

# def main():
#     pool = Pool()  # default is you CPU core number
#     pool.apply_async(func1, ('func1...arg1', 'func1...agr2'))
#     pool.apply_async(func2, ('func2...arg1...', 'func1...agr2...'))

#     pool.close()
#     pool.join()


def write(q: Queue):
    print('write start...')
    for char in ('A', 'B', 'C', 'D'):
        q.put(char)
        time.sleep(1)
    print('write end...')


def read(q: Queue):
    print('read start...')
    while True:
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
