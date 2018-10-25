# Pyinstaller

Note: Pyinstaller looks currently only works good on windows. For mac, please take a look for py2app

## 0. install

`pip install pyinstaller`

## 1. easy usage

`pyinstaller -F --windowed *.py --clean`

## 2. if you need to bundle other file or folder

First, generate the spec file:

`pyi-makespec -w *.py`

This will generate a `*.spec` file. And in this file, you can bind any folder or file in `a.datas` part using tuple ('src', 'des').for example:

```
a = Analysis(['stockcharm.py'],
             pathex=['/Users/lzhao/Documents/my_git/python/tkinter_stockcharm'],
             binaries=[],
             datas=[('./driver/*', 'driver')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
```

Then run `pyinstaller -F  *.spec --clean` to generate exe file