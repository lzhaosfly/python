import time
import os
from threading import Thread


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
    t1 = Thread(target=func1, args=('func1...arg1', 'func1...agr2'))
    t2 = Thread(target=func2, args=('func2...arg1...', 'func1...agr2...'))
    t1.start()
    t2.start()

    # do something block main process
    while True:
        print(f"this is main process --- {os.getpid()}")
        time.sleep(1)


if __name__ == '__main__':
    main()
