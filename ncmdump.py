# -*- coding: utf-8 -*-
"""
Created on Sun Jul 15 01:05:58 2018

@author: Nzix
"""

import struct
import base64
import json
import os
from Crypto.Cipher import AES
from mutagen import mp3, flac, id3

def dump(input_path, output_path = None):

    output_path = (lambda path, meta : os.path.splitext(path)[0] + '.' + meta['format']) if not output_path else output_path
    core_key = b'hzHRAmso5kInbaxW'
    meta_key = rb"#14ljk_!\]&0U<'("
    unpad = lambda s : s[0:-s[-1]]

    f = open(input_path,'rb')

    # magic header
    header = f.read(10)
    assert header[:8] == b'CTENFDAM'

    # key data
    key_length = f.read(4)
    key_length = struct.unpack('<I', bytes(key_length))[0]

    key_data = bytearray(f.read(key_length))
    key_data = bytes(byte ^ 0x64 for byte in key_data)

    cryptor = AES.new(core_key, AES.MODE_ECB)
    key_data = unpad(cryptor.decrypt(key_data))[17:]
    key_length = len(key_data)

    # key box
    key_data = bytearray(key_data)
    key_box = bytearray(range(256))
    j = 0

    for i in range(256):
        j = (key_box[i] + j + key_data[i % key_length]) & 0xff
        key_box[i], key_box[j] = key_box[j], key_box[i]

    # meta data
    meta_length = f.read(4)
    meta_length = struct.unpack('<I', bytes(meta_length))[0]

    meta_data = bytearray(f.read(meta_length))
    meta_data = bytes(byte ^ 0x63 for byte in meta_data)
    meta_data = base64.b64decode(meta_data[22:])

    cryptor = AES.new(meta_key, AES.MODE_ECB)
    meta_data = unpad(cryptor.decrypt(meta_data)).decode('utf-8')[6:]
    meta_data = json.loads(meta_data)

    # crc32
    crc32 = f.read(9)
    crc32 = struct.unpack('<I5x', bytes(crc32))[0]

    # album cover
    image_size = f.read(4)
    image_size = struct.unpack('<I', bytes(image_size))[0]
    image_data = f.read(image_size)

    # media data
    output_path = output_path(input_path, meta_data)
    m = open(output_path,'wb')

    while True:
        chunk = bytearray(f.read(0x8000))
        chunk_length = len(chunk)
        if not chunk:
            break

        for i in range(chunk_length):
            j = (i + 1) & 0xff
            chunk[i] ^= key_box[(key_box[j] + key_box[(key_box[j] + j) & 0xff]) & 0xff]

        m.write(chunk)

    m.close()
    f.close()

    # media tag
    if meta_data['format'] == 'flac':
        audio = flac.FLAC(output_path)
        # audio.delete()
        image = flac.Picture()
        image.type = 3
        image.mime = 'image/jpeg'
        image.data = image_data
        audio.clear_pictures()
        audio.add_picture(image)
    elif meta_data['format'] == 'mp3':
        audio = mp3.MP3(output_path)
        # audio.delete()
        image = id3.APIC()
        image.type = 3
        image.mime = 'image/jpeg'
        image.data = image_data
        audio.tags.add(image)
        audio.save()
        audio = mp3.EasyMP3(output_path)

    audio['title'] = meta_data['musicName']
    audio['album'] = meta_data['album']
    audio['artist'] = '/'.join([artist[0] for artist in meta_data['artist']])
    audio.save()
    
    return output_path

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        files = sys.argv[1:]
    else:
        files = [file_name for file_name in os.listdir('.') if os.path.splitext(file_name)[-1] == '.ncm']
    if sys.version[0] == '2':
        files = [file_name.decode(sys.stdin.encoding) for file_name in files]

    if not files:
        print('please input file path!')
        
    for file_name in files:
        try:
            dump(file_name)
            print(os.path.split(file_name)[-1])
        except Exception as e:
            print(e)
            pass
