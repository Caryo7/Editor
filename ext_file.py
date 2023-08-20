#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *

class ExText:
    def open(self, name):
        f = open(name, 'r', encoding = get_encode())
        r = f.read()
        f.close()
        self.insert_text(r)

        self.saved = True
        self.savedd = True
        self.path = name
        self.add_f(self.path)
        self.autocolorwords()
        self.master.title(self.title + ' - ' + self.path)
        self.update_line_numbers(fforbid = True)
        self.text.focus()

    def save(self, file, data, cryptage = True):
        f = open(file, 'w', encoding = get_encode())
        f.write(data)
        f.close()

if __name__ == '__main__':
    from __init__ import *
