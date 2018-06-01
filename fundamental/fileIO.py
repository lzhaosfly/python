import os

with open(os.path.join(os.path.dirname(__file__), 'hello.py')) as file:
    for line in file:
        print(line)

print(file.closed)