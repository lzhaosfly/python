from collections import Counter, OrderedDict

c = Counter([1, 1, 1, 2, 12, 213124, 123, 123, 213])
print(c)

c = Counter('asdxqwedascasdqwd')
print(c)

print(c.most_common(2))
print(sum(c.values()))
