import asyncio
import time


def asyncfunc1():
    print('asyncfunc1 start...')
    time.sleep(3)
    print('asyncfunc1 end...')


def asyncfunc2():
    print('asyncfunc2 start...')
    time.sleep(3)
    print('asyncfunc2 end...')


def main():
    asyncfunc1()
    asyncfunc2()


if __name__ == '__main__':
    main()
