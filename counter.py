#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter.simpledialog import *
from pathlib import Path
import os

from confr import *
from tree import *

p = Path('')
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

def act(root=None):
    SimpleDialog(root,
        text="Lignes de programme du logiciel :\n" + 
             "Programme : " + str(lines()) + '\n' +
             "Nombre de Fonctions : " + str(nbFncts()) + '\n' + 
             "Nombre de Classes : " + str(nbClasses()),
        buttons=['Fermer'],
        title='Counter',
        default=0).go()

if __name__ == '__main__':
    root = Tk()
    act(root)
