# python String

## 1. str in another str

You can directly use `in` to do the judge. like (`includes` in js)

```python
"abc" in "abcd" # True
```

```js
'abcd'.includes('abc'); // true
```

## 2. use r to 明确后面的字符串不用转义

```python
a = "\\\t\\" # print \	\
b = r"\\\t\\" # print \\\t\\
```

## 3. common method

```python
str22 = "YOU are a gooD Man"

str22.lower() # 'you are a good man'
str22.upper() # 'YOU ARE A GOOD MAN'
str22.swapcase() # 'you ARE A GOOd mAN'
str22.capitalize() # 'You are a good man'
str22.title() # 'You Are A Good Man'
str22.center(22, "*") # '**YOU are a gooD Man**'
str22.ljust(22, "*") # 'YOU are a gooD Man****'
str22.rjust(22, "*") # '****YOU are a gooD Man'
str22.zfill(22) # '0000YOU are a gooD Man'
str22.count("YOU") # return 1. Count how many str in your str
str22.count("are", 5, len(str22)) # return 0. 从第5位开始, count how many str in your str
str22.find("YOU") # return 0
str22.find("hYOU") # return -1
str22.index("YOU") # return 0
str22.index("hYOU") # throw error !!
str22.rfind("gooD") # return 10, start finding from right to left
str22.rindex("gooD") # return 10

str33 = "**YOU are a gooD Man**"
str33.lstrip("*") # 'YOU are a gooD Man**'
str33.rstrip("*") # '**YOU are a gooD Man'
str33.strip("*") # 'YOU are a gooD Man'

 chr(65) # A; int to char
 ord('a') # 97. char to int
```
