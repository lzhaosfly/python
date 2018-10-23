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

def main():
    pool = Pool()  # default is you CPU core number
    pool.apply_async(func1, ('func1...arg1', 'func1...agr2'))
    pool.apply_async(func2, ('func2...arg1...', 'func1...agr2...'))

    pool.close()
    pool.join()


if __name__ == '__main__':
    main()
