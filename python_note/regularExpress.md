# Regular expression

## 1. search

Search will only search the first element that matched

```python
import re

pattern = re.compile(r'(?P<first>\d{5})-\d{4}') # ?P<name> gives the name of capture group
match = pattern.search('The zip code is 98210-1138. 98210-1138.')

if match:
    print(match.group()) # 98210-1138
    print(match.group(1)) # 98210
    print(match.group('first')) # 98210
```

## 2. findAll

Find all occurs.

*   findAll no need to use group method
*   if you capture a group, then **findAll will only return the capture group, not whole match**.
*   if no capture a group, then findAll will return the whole match

```python
import re

pattern = re.compile(r'\d{5}-\d{4}')
matches = pattern.findall('The zip code is 98210-1138. 98210-1138.')

print(matches) # ['98210-1138', '98210-1138']

import re

pattern = re.compile(r'(\d{5})-(\d{4})')
matches = pattern.findall('The zip code is 98210-1138. 98210-1138.')

print(matches) # [('98210', '1138'), ('98210', '1138')]
```

## 3. sub

`Sub()` is substitute.

```python
import re
text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr.|Mrs.|Ms.) ([a-z])[a-z]+', re.I)
result1 = pattern.sub("\g<1> Murder", text) # \g<1> means first group, you can also use \g<name> if group has a name
result2 = pattern.sub("\g<1> \g<2>", text)
print(result1) # Last night Mrs. Murder and Mr. Murder murdered Ms. Murder
print(result2) # Last night Mrs. D and Mr. w murdered Ms. C
```

## 4. greedy and non-greedy match

Python default is using greedy match

Greedy match: Match the longgest match
non-greedy match: match the smallest match

```python
import re

# Greedy match
pattern = re.compile(r'\w{1,3}')
match = pattern.search('eyes')

if match:
    print(match.group()) # eyes

import re

# Non-greedy match, please Note the `{1,3}?`, '?' means non-greedy
pattern = re.compile(r'\w{1,3}?')
match = pattern.search('eyes')

if match:
    print(match.group())
```

**`.*` is a greedy match and `.*?` is a non-greedy match!!**

```python
pattern = re.compile(r'0(.*)5')
print(pattern.findall('012345012345')) # ['1234501234']

pattern = re.compile(r'0(.*?)5')
print(pattern.findall('012345012345')) # ['1234', '1234']

pattern = re.compile(r'0(.*)5')
print(pattern.search('012345012345').group()) # 012345012345

pattern = re.compile(r'0(.*?)5')
print(pattern.search('012345012345').group()) # 012345
```
