# -*- mode: python ; coding: utf-8 -*-

files = [
    ('qml/main.qml', './qml'),
    ('qml/Auth.qml', './qml'),
    ('qml/App.qml', './qml'),
    ('qml/Authors.qml', './qml'),
    ('qml/Books.qml', './qml'),
    ('qml/Library.qml', './qml'),
    ('qml/Publishers.qml', './qml'),
    ('qml/Readers.qml', './qml'),
]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='AppLib',
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
    icon=['icon.ico'],
)
