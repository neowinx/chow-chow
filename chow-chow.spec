# -*- mode: python -*-
import os

path = os.getcwd()

a = Analysis(['chow-chow.py'],
             pathex=[os.getcwd()],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='chow-chow',
          debug=False,
          strip=None,
          upx=True,
          console=True )