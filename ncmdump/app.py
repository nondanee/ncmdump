# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 13:32:51 2018

@author: Nzix
"""

import argparse, os, sys, traceback, re
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

if __package__ is None:
    from core import dump
else:
    from .core import dump

parser = argparse.ArgumentParser(
    prog = 'ncmdump', add_help = False
)
parser.add_argument(
    '-h', action = 'help',
    help = 'show this help message and exit'
)
parser.add_argument(
    'input', metavar = 'input', nargs = '*', default = ['.'],
    help = 'ncm file or folder path'
)
parser.add_argument(
    '-f', metavar = 'format', dest = 'format', default = '',
    help = 'customize naming format'
)
parser.add_argument(
    '-o', metavar = 'output', dest = 'output',
    help = 'customize saving folder'
)
parser.add_argument(
    '-d', dest = 'delete', action = 'store_true',
    help = 'delete source after conversion'
)
group = parser.add_mutually_exclusive_group()
group.add_argument(
    '-c', dest = 'cover', action = 'store_true',
    help = 'overwrite file with the same name'
)
group.add_argument(
    '-r', dest = 'rename', action = 'store_true',
    help = 'auto rename if file name conflicts'
)
args = parser.parse_args()

def validate_name(name):
    pattern = {u'\\': u'＼', u'/': u'／', u':': u'：', u'*': u'＊', u'?': u'？', u'"': u'＂', u'<': u'＜', u'>': u'＞', u'|': u'｜'}
    for character in pattern:
        name = name.replace(character, pattern[character])
    return name

def validate_collision(path):
    index = 1
    origin = path
    while os.path.exists(path):
        path = '({})'.format(index).join(os.path.splitext(origin))
        index += 1
    return path

def name_format(path, meta):
    information = {
        'artist': ','.join([artist[0] for artist in meta.get('artist')]) if 'artist' in meta else None,
        'title': meta.get('musicName'),
        'album': meta.get('album')
    }

    def substitute(matched):
        key = matched.group(1)
        if key in information:
            return information[key]
        else:
            return key

    name = re.sub(r'%(.+?)%', substitute, args.format)
    name = os.path.splitext(os.path.split(path)[1])[0] if not name else name
    name = validate_name(name)
    name += '.' + meta['format']
    folder = args.output if args.output else os.path.dirname(path)
    save = os.path.join(folder, name)
    if args.rename: save = validate_collision(save)
    return save

def main():
    if args.output:
        args.output = os.path.abspath(args.output)
        if not os.path.exists(args.output):
            print('output does not exist')
            exit()
        if not os.path.isdir(args.output):
            print('output is not a folder')
            exit()

    files = []
    for path in args.input:
        path = os.path.abspath(path)
        if not os.path.exists(path):
            continue
        if os.path.isdir(path):
            files += [os.path.join(path, name) for name in os.listdir(path) if os.path.splitext(name)[-1] == '.ncm']
        else:
            files += [path]

    if sys.version[0] == '2':
        files = [path.decode(sys.stdin.encoding) for path in files]

    if not files:
        print('empty input')
        exit()

    for path in files:
        try:
            save = dump(path, name_format, not args.cover)
            if save: print(os.path.split(save)[-1])
            if args.delete: os.remove(path)
        except KeyboardInterrupt:
            exit()
        except:
            print(traceback.format_exc())

if __name__ == '__main__':
    main()