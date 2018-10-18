from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 1


def main():
    print(Weekday.Sun)
    print(Weekday.Sun.value)


if __name__ == '__main__':
    main()
