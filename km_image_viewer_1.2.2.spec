# -*- mode: python -*-

block_cipher = None


a = Analysis(['km_image_viewer_1.2.2.py'],
             pathex=['C:\\Users\\teddy\\Desktop\\tkinter\\km_image_viewer_1.2.2'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas +=[('icon.ico','icon.ico','DATA'),('none.png','none.png','DATA')]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='km_image_viewer_1.2.2',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,icon='icon.ico',onefile=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='km_image_viewer_1.2.2')
