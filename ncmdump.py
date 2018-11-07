#! /user/bin/env python3
# -*-coding: utf-8 -*-
from base64 import b64decode
from functools import partial
from json import loads
from os import scandir
from os.path import basename, join, isfile
from struct import unpack
from time import clock

from Crypto.Cipher import AES
from mutagen.flac import Picture, FLAC
from mutagen.id3 import APIC
from mutagen.mp3 import MP3
from numpy import fromstring


def bxor_numpy(b1, b2):
    n_b1 = fromstring(b1, dtype='uint8')
    n_b2 = fromstring(b2, dtype='uint8')
    return (n_b1 ^ n_b2).tostring()


def Dump():
    ncm_header = b'CTENFDAM'
    core_key = b'hzHRAmso5kInbaxW'
    meta_key = b"#14ljk_!\\]&0U<'("
    core_cryptor = AES.new(core_key, AES.MODE_ECB)
    meta_cryptor = AES.new(meta_key, AES.MODE_ECB)
    up = partial(unpack, '<I')
    range_256 = list(range(256))
    indexes = range_256[1:] + [0]

    def aes128_ecb_decrypt(ciphertext):
        plaintext = core_cryptor.decrypt(ciphertext)
        return plaintext[:- plaintext[-1]]

    def b64_aes128_ecb_decrypt(ciphertext):
        plaintext = meta_cryptor.decrypt(b64decode(ciphertext))
        return plaintext[:- plaintext[-1]]

    def _dump(file_path, output_path):
        with open(file_path, 'rb') as f:

            # magic header
            header = f.read(8)
            assert header == ncm_header

            # key data
            f.seek(2, 1)
            key_length = f.read(4)
            key_length = up(key_length)[0]

            key_data = f.read(key_length)
            key_data = bytes(byte ^ 0x64 for byte in key_data)
            key_data = aes128_ecb_decrypt(key_data)[17:]
            key_length = len(key_data)

            # key box
            key_box = bytearray(range_256)
            j = 0
            for i in range_256:
                j = (key_box[i] + j + key_data[i % key_length]) & 0xff
                key_box[i], key_box[j] = key_box[j], key_box[i]
            modify_keys = bytes(key_box[(key_box[i] + key_box[(key_box[i] + i) & 0xff]) & 0xff] for i in indexes)

            # meta data
            meta_length = f.read(4)
            meta_length = up(meta_length)[0]
            meta_data = f.read(meta_length)
            meta_data = bytes(byte ^ 0x63 for byte in meta_data)[22:]
            meta_data = b64_aes128_ecb_decrypt(meta_data).decode()[6:]
            meta_data = loads(meta_data)
            f.seek(9, 1)

            # album cover
            image_size = f.read(4)
            image_size = up(image_size)[0]
            image_data = f.read(image_size)

            # media data
            music_name = f'{basename(file_path).rsplit(".",maxsplit=1)[0]}.{meta_data["format"]}'
            output_path = join(output_path, music_name)
            print(music_name, end=' ··· ')
            if isfile(output_path):
                print('文件已存在')
                return
            music_data = f.read()
        l = len(music_data)
        full_chunk_count = l // 256
        last_chunk_length = l % 256
        modify_keys = modify_keys * full_chunk_count + modify_keys[:last_chunk_length]

        modified_music_data = bxor_numpy(modify_keys, music_data)

        with open(output_path, 'wb') as m:
            m.write(modified_music_data)
        if image_data == b'':
            print('没有封面')
        else:
            if image_data.startswith(b'\xFF\xD8\xFF\xE0'):
                mime = 'image/jpeg'
            elif image_data.startswith(b'\x89PNG\r\n\x1a\n'):
                mime = 'image/png'
            if meta_data['format'] == 'mp3':
                audio = MP3(output_path)
                audio.tags.add(
                    APIC(
                        mime=mime,
                        type=3,
                        data=image_data
                    )
                )

            elif meta_data['format'] == 'flac':
                audio = FLAC(output_path)
                audio.clear_pictures()
                cover = Picture(image_data)
                cover.mime = mime
                cover.desc = u'cover'
                audio.add_picture(cover)
            audio.save(v2_version=3)
        print('完成')

    return _dump


dump = Dump()


def search_and_dump(search_dir, output_dir):
    ncm_files_path = [i.path for i in scandir(search_dir) if i.name.endswith('.ncm')]
    l = len(ncm_files_path)
    i = 1
    st = clock()
    for file_path in ncm_files_path:
        print(f'{i}/{l}', end=' ')
        i += 1
        dump(file_path, output_dir)
    print(f'时间: {clock() - st:.2f}s')
