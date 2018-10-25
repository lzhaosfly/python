# -*- mode: python -*-

block_cipher = None


a = Analysis(['ui_window.py'],
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
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='stockcharm',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='stockcharm')
app = BUNDLE(coll,
             name='stockcharm.app',
             icon=None,
             bundle_identifier=None)
