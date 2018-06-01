# CSV file

## 0. Please also check `os.path` module

[`os.path`](https://docs.python.org/3/library/os.path.html)

*   `os.path.basename(path)`
*   `os.path.dirname(__file__)`
*   `os.path.exists(path)`
*   `os.path.getsize(path)`
*   `os.path.getctime(path)`
*   `os.path.isabs(path)`
*   `os.path.isfile(path)`
*   `os.path.isdir(path)`
*   `os.path.join(path, *paths)`
*   `os.path.samefile(path1, path2)`

## 1. read csv file

Using `csv.reader` or `csv.DictReader` to read a csv file

*   `csv.reader` will read the csv file and assign each row to a list iterator
*   `csv.DictReader` will read each row and assign each row to a dict iterator, the key is the header row
*   Readers accept a delimiter kwarg in case your data isn't separated by commas.

```python
# Using reader
from csv import reader

with open(os.path.join(os.path.dirname(__file__), "fighters.csv")) as file:
    # csv_reader = reader(file, delimiter="|")
    csv_reader = reader(file)
    next(csv_reader) #To skip the headers
    for fighter in csv_reader:
    	# Each row is a list
    	# Use index to access data
    	print(f"{fighter[0]} is from {fighter[1]}")

# Reading/Parsing CSV Using a DictReader:
from csv import DictReader
with open(os.path.join(os.path.dirname(__file__), "fighters.csv")) as file:
    csv_reader = DictReader(file)
    for row in csv_reader:
        # Each row is an OrderedDict!
        print(row['Name']) #Use keys to access data, key is the header row
```

## 2. Write csv file

using `csv.writer` or `csv.DictWriter` to write a csv file

```python
# csv.writer
from csv import writer
with open("fighters.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Character", "Move"])
    csv_writer.writerow(["Ryu", "Hadouken"])

# csv.DictWriter
from csv import DictWriter
with open("example.csv", "w") as file:
    headers = ("Character", "Move")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerow({
        "Character": "Ryu",
        "Move": "Hadouken"
    })
```
