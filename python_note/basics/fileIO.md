# FileIO

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

## 1. Open File

[open built in function](https://docs.python.org/3/library/functions.html#open)

Using `open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)` to open a file

Mode:

*   `r`: open for reading (default)
*   `r+`: read and write the file (write based on cursor)
*   `w`: open for writing, truncating the file first
*   `w+`: read and write the file (write based on cursor)
*   `x`: open for exclusive creation, failing if the file already exists
*   `a`: open for writing, appending to the end of the file if it exists
*   `b`: binary mode
*   `t`: text mode (default)
*   `+`: open a disk file for updating (reading and writing)
*   `U`: universal newlines mode (deprecated)

## 2. read File

```python
# Normal using
file = open('story.txt')
file.read() # Read file content until the cursor
file.seek(0) # Move cursor to 0 position
file.readline() # readline from file
file.close()

file.closed() # True

# Pythonior
import os

# Using with, no need to close file
with open(os.path.join(os.path.dirname(__file__), 'hello.py')) as file:
    for line in file: #read line
        print(line)

file.closed() # True
```

## 3. write file

```python
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        file.truncate()
```

## 4. `shutil` — High-level file operations

The `shutil` module offers a number of high-level operations on files and collections of files. In particular, functions are provided which support file copying and removal. For operations on individual files, see also the `os` module.

[shutil](https://docs.python.org/3/library/shutil.html)

*   `shutil.copyfile(src, dst, *, follow_symlinks=True)`
*   `shutil.copymode(src, dst, *, follow_symlinks=True)`
*   `shutil.copy(src, dst, *, follow_symlinks=True)`
*   `shutil.copy2(src, dst, *, follow_symlinks=True)`
*   `shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2, ignore_dangling_symlinks=False)`

-   `shutil.rmtree(path, ignore_errors=False, onerror=None)`
-   `shutil.move(src, dst, copy_function=copy2)`
-   `shutil.disk_usage(path)`
-   `shutil.chown(path, user=None, group=None)`

-   `shutil.make_archive(base_name, format[, root_dir[, base_dir[, verbose[, dry_run[, owner[, group[, logger]]]]]]])`
-   `shutil.get_archive_formats()`
-   `shutil.unpack_archive(filename[, extract_dir[, format]])`
