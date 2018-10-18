class Human(object):
    def __init__(self, first: str, last, age):
        self._first = first
        self._last = last
        self.__fullName = first + last
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

    @property
    def fullName(self):
        return self.__fullName

    # @fullName.setter
    # def fullName(self, val):
    #     self.__fullName = val


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
print(jane.fullName)
# jane.fullName = "Jane111"
# print(jane.fullName)

lei = Teacher("lei", "zhao", 27, "test")
print(lei.first)
