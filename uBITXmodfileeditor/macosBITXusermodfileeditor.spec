# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['uBITXusermodfileeditor.py'],
    pathex=[],
    binaries=[],
	datas=[('images/red-arrow-pointing-left59x36.png','./images'),('images/red-arrow-pointing-right59x36.png','./images'),('eeprommemorymap.xml','.'), ('usermodfiletemplate.xml','.'),('help.xml','.'), ('about.xml','.'), ('images/sample1-125x80.png','./images'),('images/sample2-125x80.png','./images'),('images/sample3-125x80.png','./images'),('images/sample4-125x80.png','./images'),('images/sample5-125x80.png','./images'),('images/sample6-125x80.png','./images'),('images/sample7-125x80.png','./images')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='uBITX_Manager_V2-01-25-23-winx64',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
