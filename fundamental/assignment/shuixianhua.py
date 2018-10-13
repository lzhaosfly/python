def isShuixianhua(n: int):
    hundreds = n // 100
    tens = (n % 100) // 10
    ones = (n % 10)
    if hundreds ** 3 + tens ** 3 + ones ** 3 == n:
        return (hundreds, tens, ones)
    return None


def main():
    for i in range(100, 1000):
        if isShuixianhua(i) is not None:
            (hundreds, tens, ones) = isShuixianhua(i)
            print(f"{i} = {hundreds}^3 + {tens}^3 + {ones}^3")


if __name__ == '__main__':
    main()
