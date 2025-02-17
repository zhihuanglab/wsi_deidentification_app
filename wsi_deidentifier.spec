# -*- mode: python ; coding: utf-8 -*-
import imagecodecs

datas = [
    ('LICENSE', '.'),
    # Imagecodecs pyds you manually placed in "Resources"
    ("Resources\\imagecodecs\\_zlib.cp39-win_amd64.pyd", "imagecodecs"),
    ("Resources\\imagecodecs\\_jpeg8.cp39-win_amd64.pyd", "imagecodecs"),
    ("Resources\\imagecodecs\\_jpeg2k.cp39-win_amd64.pyd", "imagecodecs"),
    ("Resources\\imagecodecs\\_imcd.cp39-win_amd64.pyd", "imagecodecs"),
    ("Resources\\imagecodecs\\_shared.cp39-win_amd64.pyd", "imagecodecs"),
]

# Combine your existing hiddenimports with Twisted plugins
hiddenimports = (
    ["imagecodecs." + x for x in imagecodecs._extensions()]
    + [
        "imagecodecs._shared",
        "imagecodecs._imcd",
        "PySide6",
        "tifffile",
        "Pillow",
        "numpy",
        "zarr",
        "tiffslide",
        "pandas",
        "openpyxl",
    ]
)

a = Analysis(
    ['app\\main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='wsi_deidentifier',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False, # set True for testing
    disable_windowed_traceback=False, # set True for testing
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
