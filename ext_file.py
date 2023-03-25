#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *

class ExText:
    def open(self, name):
        f = open(name, 'r', encoding = get_encode())
        r = f.read()
        f.close()
        if get_encrypted():
            self.text.insert(END, self.decrypt(r))
        else:
            self.text.insert(END, r)

    def save(self, file, data, cryptage = True):
        f = open(file, 'w', encoding = get_encode())
        if get_encrypted() and cryptage:
            f.write(self.encrypt(data))
        else:
            f.write(data)
        f.close()

if __name__ == '__main__':
    from __init__ import *
