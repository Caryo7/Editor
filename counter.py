#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.simpledialog import *
from pathlib import Path
import os

from confr import *
from tree import *

p = Path(os.path.abspath(os.getcwd()))
tt = list(p.glob('**/*.py')) + list(p.glob('**/*.pyw')) + list(p.glob('**/*.ext'))
s = 0
for i in tt:
    w = str(i)
    f = open(w, 'r', encoding = get_encode())
    try:
        r = f.read()
    except UnicodeDecodeError:
        r = '\n'
    f.close()
    s += r.count('\n')

def lines():
    return s

def act(main_self):
    zak = Toplevel(main_self.master)
    zak.transient(main_self.master)
    zak.title(lg('Info_log'))
    zak.iconbitmap(main_self.ico['win'])
    zak.resizable(False, False)

    dic = {lg("Nb_Lines"): str(lines()),
           lg("Nb_Fncts"): str(nbFncts()),
           lg("Nb_Class"): str(nbClasses()),
           lg("Nb_Files"): str(nbFiles())}

    row = 0
    for k, v in dic.items():
        Label(zak, text = k, font = ('Consolas', 12)).grid(row = row, column = 0, padx = 2, pady = 5, sticky = 'e')
        Label(zak, text = v, font = ('Consolas', 12)).grid(row = row, column = 1, padx = 2, pady = 5, sticky = 'w')
        row += 1

    Button(zak, text = lg('OK'), command = zak.destroy).grid(row = row, column = 0, padx = 10, pady = 5, columnspan = 2)

if __name__ == '__main__':
    from __init__ import *
