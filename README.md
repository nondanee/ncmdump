# Netease Cloud Music Copyright Protection File Dump

![shield](https://img.shields.io/badge/python-2.7%7C3.4+-blue.svg)

## Credit

### Origin

- [anonymous5l/ncmdump](https://github.com/anonymous5l/ncmdump): Original repository

### Fork

- [JamieDummy/NCM_dump](https://github.com/JamieDummy/NCM_dump): Add GUI
- [mnilzg/ncmdump](https://github.com/mnilzg/ncmdump): Speed up with NumPy

## Dependency

If to install this package and run, dependencies will be automatically installed:

```bash
pip install pycryptodome mutagen argparse
```

## Install

You can install the package and run it globally:

```bash
pip install git+https://github.com/nondanee/ncmdump.git
```

## Usage

### Specify files

If installed:

```bash
ncmdump file_or_folder1[, file_or_folder2[,...]]
```

If not installed:

```bash
python ncmdump/ncmcli.py file_or_folder1[, file_or_folder2[,...]]
```

### Traverse working directory

If installed:

```bash
ncmdump
```

If not installed:

```bash
python ncmdump/ncmcli.py
```

### More options

If installed:

```bash
ncmdump -h
```

If not installed:

```bash
python ncmdump/ncmcli.py -h
```

<var>
usage: ncmdump [-h] [-f format] [-o output] [-d] [-c | -s] [input [input ...]]

positional arguments:
  input       ncm file or folder path

optional arguments:
  -h, --help  show this help message and exit
  -f format   customize naming format
  -o output   customize saving folder
  -d          delete source after conversion
  -c          overwrite file with the same name
  -s          skip conversion if file exist
</var>

**Supported name holder: %artist%, %title%, %album%**