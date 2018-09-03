# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['.\\test', 'D:\\System\\Downloads\\Admin'],
             binaries=[],
             datas=[],
             hiddenimports=['PyQt5.sip', 'pandas._libs.tslibs.timedeltas', 'pandas._libs.tslibs.np_datetime', 'pandas._libs.tslibs.nattype', 'pandas._libs.skiplist'],
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
          name='EIMS',
          debug=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, 
		  icon='D:\\System\\Downloads\\Admin\\res\\icon.ico')
