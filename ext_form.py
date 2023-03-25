#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
import zipfile as zp

class ExForm:
    def open(self, name):
        result = None
        f = zp.ZipFile(name, 'r')
        if get_encrypted():
            result = self.decrypt(f.read('data.txt').decode(get_encode()))
        else:
            result = f.read('data.txt').decode(get_encode())
        self.text.insert(END, result)
        lst_tag = str(f.read('tags.csv').decode(get_encode())).split('\n')
        for i in lst_tag:
            self.lst_tags.append(i.split(','))
        self.write_tags()
        f.close()

    def save(self, file, data, cryptage = True):
        z = zp.ZipFile(file, 'w')
        f = z.open('data.txt', 'w')
        if get_encrypted() and cryptage:
            f.write(self.encrypt(data))
        else:
            f.write(data.encode(get_encode()))
        f.close()
        f = z.open('tags.csv', 'w')
        for i in self.lst_tags:
            f.write(str(','.join(i) + '\n').encode())
        f.close()
        z.close()        

if __name__ == '__main__':
    from __init__ import *
