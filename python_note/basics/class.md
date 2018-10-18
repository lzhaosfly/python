# Class

## 1. getter and setter

using `@property` and `@something.setter` to do getter and setter

```python
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


jane = Human("Jane", "Goodall", -9)
print(jane.age)
jane.age = -123
print(jane.age)
```

## 2. name, \_name, \_\_name, \_\_name\_\_

There's a convention way for these 4 diffrent format:

*   name: public, can be access from outside class. like **public**.
*   \_name: private, only used within a class or its son class. Outside can still directly get, but not recommand! like **protected**
*   \_\_name: is only for current class. Inherit will not get this variable or method. like **private**.
*   \_\_name\_\_: it's for python internal function

## 3. class attributes and class method

```python
class User:
	active_users = 0 # This is a class attribute

	@classmethod # class method
	def display_active_users(cls): # cls means class
		return f"There are currently {cls.active_users} active users"

	@classmethod
	def from_string(cls, data_str):
		first,last,age = data_str.split(",")
		return cls(first, last, int(age))

	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age
		User.active_users += 1
```

## 4. inherits

*   Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx
*   Note Python3 super doesn't need `self`

```python
class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f"{self.name} is a {self.species}"

	def make_sound(self, sound):
		print(f"this animal says {sound}")


class Cat(Animal):
	def __init__(self, name, breed, toy):
		super().__init__(name, species="Cat") # Call init on parent class
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f"{self.name} plays with {self.toy}")
```

## 5. Multiple inherits

Python is using `MRO (Method Resolution Order)` to check the multiple inherits order

If there's a name conflict in parents class, then use the following 3 methods to check (Note CLASS means the CLASS name, not object, it's CLASS name!!! Just believe mro is a static method):

1.  CLASS.**mro**
2.  CLASS.mro()
3.  help(CLASS) <!--best check-->

## 6. **magic** methods

check this page for more magic methods: [magic method](https://docs.python.org/3/reference/datamodel.html)

```python
from copy import copy
class Human:
	def __init__(self, first, last, age):
		self.first = first
		self.last = last
		self.age = age

	def __repr__(self):
		return f"Human named {self.first} {self.last} aged {self.age}"

	def __len__(self):
		return self.age

	def __add__(self, other):
		# When you add two humans together...you get a newborn baby Human!
		if isinstance(other, Human):
			return Human(first='Newborn', last=self.last, age=0)
		return "You can't add that!"

	def __mul__(self, other):
		# When you multiply a Human by an int, you get clones of that Human!
		if isinstance(other, int):
			return [copy(self) for i in range(other)]
		return "CANT MULTIPLY!"
```

## 7. abstract method

```python
from abc import abstractmethod, ABCMeta

class Model(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        """This method should implement how to foo the model."""
```

## 8. magic __slots__ (limit dynamic added properties)

```python
class Character:
    __slots__ = ('name', 'hp', 'level', 'age', 'height')

    def __init__(self, name: str, hp: int, level: str):
        self.name = name
        self.hp = hp
        self.level = level
```

Note: in the above example, `Character` can only have `('name', 'hp', 'level', 'age', 'height')` properties. If you dynamiclly add other property, it will throw error.
