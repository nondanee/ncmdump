# Netease Cloud Music Copyright Protection File Dump

![shield](https://img.shields.io/badge/python-2.7%20%7C%203.4%2B-blue)

## Credit

### Origin

- [anonymous5l/ncmdump](https://github.com/anonymous5l/ncmdump): Original repository

### Fork

- [JamieDummy/NCM_dump](https://github.com/JamieDummy/NCM_dump): Add GUI
- [mnilzg/ncmdump](https://github.com/mnilzg/ncmdump): Speed up with NumPy


### Contributor

- [@kalteblau](https://github.com/kalteblau): Validate path & collision
- [@HarrisonXi](https://github.com/HarrisonXi): Add missing identifier
- [@leconio](https://github.com/leconio): Handle dict key missing exception
- [@lonelyhentai](https://github.com/lonelyhentai): Add pip support

## Dependency

```
$ pip install pycryptodome mutagen
```

## Install

```
$ pip install git+https://github.com/nondanee/ncmdump.git
```

## Usage

### Execute

```sh
$ ncmdump -h # equivalent to "python ncmdump/app.py -h" and "python -m ncmdump.app -h"
usage: ncmdump [-h] [-f format] [-o output] [-d] [-c | -r] [input [input ...]]

positional arguments:
  input      ncm file or folder path

optional arguments:
  -h         show this help message and exit
  -f format  customize naming format
  -o output  customize saving folder
  -d         delete source after conversion
  -c         overwrite file with the same name
  -r         auto rename if file name conflicts
```

> Supported name format holder: `%artist%`, `%title%`, `%album%`

### Import

```python
from ncmdump import dump
```

```python
def dump(input_path, output_path = None, skip = True):
    '''
    args:
        input_path: a string of input file path
        output_path: a string of output file path or a naming function
        skip: a boolean controls conversion skipping when output file exists

    returns:
        a string of output file path or none if conversion is skipped
    '''
```
