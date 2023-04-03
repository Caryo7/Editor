#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
import zipfile as zp

class ExForm1:
    @classmethod
    def open(self, name):
        try:
            f = zp.ZipFile(name, 'r')
            result = f.read('data.txt').decode(get_encode())
            lst_tag = str(f.read('tags.csv').decode(get_encode())).split('\n')
            lst_tags = []
            for i in lst_tag:
                i = i.replace('\r', '')
                if i != '':
                    lst_tags.append(i.split(','))
            f.close()
            return (result, lst_tags)

        except Exception as e:
            log = open(self.path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [])

    @classmethod
    def save(self, file, data, lst_tags):
        try:
            z = zp.ZipFile(file, 'w')
            f = z.open('data.txt', 'w')
            f.write(data)
            f.close()
            f = z.open('tags.csv', 'w')
            for i in lst_tags:
                f.write(str(','.join(i) + '\n').encode())
            f.close()
            z.close()

        except Exception as e:
            log = open(self.path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


class ExForm2:
    @classmethod
    def open(self, name):
        try:
            f = zp.ZipFile(name, 'r')
            result = f.read('data.txt').decode(get_encode())
            lst_tag = str(f.read('tags.csv').decode(get_encode())).split('\n')
            lst_tags = []
            for i in lst_tag:
                i = i.replace('\r', '')
                if i != '':
                    lst_tags.append(i.split(','))
    
            meta = {}
            meta_data = f.read('meta.ini').decode(get_encode())
            for i in meta_data.split('\n'):
                if meta_data != '':
                    key, value = meta_data.split('-')
                    key = key.replace('"', '')
                    value = value.replace('"', '')
                    meta[key] = value
    
            f.close()
            return (result, lst_tags, meta)

        except Exception as e:
            log = open(self.path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [], {})

    @classmethod
    def save(self, file, data, lst_tags, meta):
        try:
            z = zp.ZipFile(file, 'w')
            f = z.open('data.txt', 'w') 
            f.write(data)
            f.close()
            f = z.open('tags.csv', 'w')
            for i in lst_tags:
                f.write(str(','.join(i) + '\n').encode())
            f.close()
            f = z.open('meta.ini', 'w')
            if 'version' not in meta.keys():
                meta['version'] = 'Form-2.0'
    
            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"').encode(get_encode()))
            f.close()
            z.close()

        except Exception as e:
            log = open(self.path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


class ExForm:
    def open(self, name):
        if '1.' in self.FORM_VERSION:
            data, lst_tags = ExForm1.open(name)
            meta = {}
        elif '2.' in self.FORM_VERSION:
            data, lst_tags, meta = ExForm2.open(name)
        else:
            data, lst_tags = ExForm1.open(name)
            meta = {}

        if get_encrypted():
            self.text.insert(END, self.decrypt(data))
        else:
            self.text.insert(END, data)

        for tag in lst_tags:
            self.lst_tags.append(tag)
        self.write_tags()
        self.meta = meta

    def save(self, file, data, meta):
        if get_encrypted():
            data = self.encrypt(data)
        else:
            data = data.encode(get_encode())

        if '1.' in self.FORM_VERSION:
            ExForm1.save(file, data, self.lst_tags)
        elif '2.' in self.FORM_VERSION:
            ExForm2.save(file, data, self.lst_tags, meta)
        else:
            ExForm1.save(file, data, self.lst_tags)

if __name__ == '__main__':
    from __init__ import *
