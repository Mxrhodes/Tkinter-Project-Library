# -*- mode: python -*-

block_cipher = None


a = Analysis(['books_frontend.py'],
             pathex=['C:\\Users\\rhode\\Desktop\\DojoAssigntments\\Python_Stack\\udemy_demo_scripts\\book_desk'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='books_frontend',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False )
