import re

pattern = re.compile(r'(\d{5})-(\d{4})')
matches = pattern.findall('The zip code is 98210-1138. 98210-1138.')

print(matches)

pattern = re.compile(r'0(.*)5')
print(pattern.search('012345012345').group())

pattern = re.compile(r'0(.*?)5')
print(pattern.search('012345012345').group())