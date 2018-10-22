# OS module

## 0. if you want to check system version

if you want to check system version, then please check `platform.system()`. 

```python
if platform.system() == 'Windows':
    chromeDriverPath = './chromedriver_win32.exe'
elif platform.system() == 'Linux':
    chromeDriverPath = './chromedriver_linux'
elif platform.system() == 'Darwin' :
    chromeDriverPath = './chromedriver_mac'
```

## 1. common module

```python
import os

os.name # posix

os.uname # (sysname='Darwin', nodename='lzhao-mbp', release='17.7.0', version='Darwin Kernel Version 17.7.0: Thu Jun 21 22:53:14 PDT 2018; root:xnu-4570.71.2~1/RELEASE_X86_64', machine='x86_64')
# 注意: windows not support os.uname!!!

os.environ # environment variable
os.environ.get('somename') # environment variable
os.sep # os seperator, delimiter

os.curdir # 当前相对目录 return '.'
os.getcwd() # return full path

os.listdir('path') # list dir
os.mkdir('path') # make dir
os.rmdir('path') # rm dir

os.stat('path') # get file state

os.rename('oldName', 'newName')
os.remove('file path') # remove file

os.system('shell command') # run shell command
```

## 2. os path

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
*   `os.path.split(path)` (dir abs path, file)
*   `os.path.splitnext(path)` (abs file path, extension)