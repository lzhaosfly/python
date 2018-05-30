class Human(object):
    def __init__(self, first, last, age):
        self._first = first
        self._last = last
        if age > 0:
            self._age = age
        else:
            self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, val):
        if val >= 0:
            self._age = val
        else:
            raise ValueError("Age can't be negative")


class Teacher(Human):
    def __init__(self, first, last, age, class_name):
        super().__init__(first, last, age)
        self._class_name = class_name

    @property
    def first(self):
        return self._first


jane = Human("Jane", "Goodall", -9)
print(jane.age)
jane.age = 123
print(jane.age)

lei = Teacher("lei", "zhao", 27, "test")
print(lei.first)

d = {lei: 1, jane: 2}
print(lei)
print(d[Teacher("lei", "zhao", 27, "test")])
