# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['uBITX_Settings_Editor.py'],
    pathex=['env\Lib\site-packages'],
    binaries=[],
    datas=[('img_red-arrow-pointing-left59x36.png','.'),('img_red-arrow-pointing-right59x36.png','.'),('eeprommemorymap.xml','.'), ('usermodfiletemplate.xml','.'),('help.xml','.'), ('about.xml','.'), ('img_Custom-125x80.png','.'),('img_sample1-125x80.png','.'),('img_sample2-125x80.png','.'),('img_sample3-125x80.png','.'),('img_sample4-125x80.png','.'),('img_sample5-125x80.png','.'),('img_sample6-125x80.png','.'),('img_sample7-125x80.png','.'), ('img_copy_icon25x25.png','.'),('img_Reload-24x24.png','.'), ('img_plain_red-arrow-pointing-left59x36.png','.'), ('img_plain_red-arrow-pointing-right59x36.png','.'), ('img_copy_icon25x25.png','.'), ('settingseditor.ico','.')],
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
	icon='settingseditor.ico',
    name='uBITX_Settings_Editor_V2RC1-05-29-23-win-intelx64',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    #console=True,
	console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
