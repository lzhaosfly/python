import re

pattern = re.compile(r'(\d{5})-(\d{4})')
matches = pattern.findall('The zip code is 98210-1138. 98210-1138.')

print(matches)

pattern = re.compile(r'0(.*)5')
print(pattern.search('012345012345').group())

pattern = re.compile(r'0(.*?)5')
print(pattern.search('012345012345').group())

text = "Last night Mrs. Daisy and Mr. white murdered Ms. Chow"

pattern = re.compile(r'(Mr\.|Mrs\.|Ms\.) ([a-z])[a-z]+', re.I)
result0 = pattern.sub("REDACATED", text)
result1 = pattern.sub(
    "\g<1> Murder", text
)  # \g<1> means first group, you can also use \g<name> if group has a name
result2 = pattern.sub("\g<1> \g<2>", text)
print(result0)  # Last night REDACATED and REDACATED murdered REDACATED
print(result1)  # Last night Mrs. Murder and Mr. Murder murdered Ms. Murder
print(result2)  # Last night Mrs. D and Mr. w murdered Ms. C
