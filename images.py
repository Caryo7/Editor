#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image, ImageTk
from pathlib import Path
import os

class IconImage:
    def __init__(self, master, file, path_prog):
        if not file:
            self.icon = PhotoImage(master = master, file = '')
            self.img = PhotoImage(master = master, file = '')
            return

        self.icon = PhotoImage(master = master, file = path_prog + '/image/16x16/' + file + '.png')
        #self.bt = PhotoImage(master = master, file = path_prog + '/image/48x48/' + file + '.png')
        #self.img = PhotoImage(master = master, file = path_prog + '/image/512x512/' + file + '.png')


class Images:
    def __images__(self):
        self.images = {'logo': self.path_prog + '/image/icons/icone',
                       'new' : IconImage(master = self.master, path_prog = self.path_prog, file = 'PlusIcon').icon,
                       'open' : IconImage(master = self.master, path_prog = self.path_prog, file = 'OpenIcon').icon,
                       'import' : IconImage(master = self.master, path_prog = self.path_prog, file = 'ImportIcon').icon,
                       'save' : IconImage(master = self.master, path_prog = self.path_prog, file = 'Save').icon,
                       'saveas' : IconImage(master = self.master, path_prog = self.path_prog, file = 'SaveAsIcon').icon,
                       'savecopyas' : IconImage(master = self.master, path_prog = self.path_prog, file = 'SaveAsCopyIcon').icon,
                       'settings' : IconImage(master = self.master, path_prog = self.path_prog, file = 'config').icon,
                       'print': IconImage(master = self.master, path_prog = self.path_prog, file = 'PrinterIcon').icon,
                       'close': IconImage(master = self.master, path_prog = self.path_prog, file = 'CloseIcon').icon,
                       'exit': IconImage(master = self.master, path_prog = self.path_prog, file = 'ShutIcon').icon,

                       'undo': IconImage(master = self.master, path_prog = self.path_prog, file = 'UndoIcon').icon,
                       'redo': IconImage(master = self.master, path_prog = self.path_prog, file = 'RedoIcon').icon,
                       'cut': IconImage(master = self.master, path_prog = self.path_prog, file = 'CutIcon').icon,
                       'copy': IconImage(master = self.master, path_prog = self.path_prog, file = 'CopyIcon').icon,
                       'past': IconImage(master = self.master, path_prog = self.path_prog, file = 'PasteIcon').icon,
                       'gotol': IconImage(master = self.master, path_prog = self.path_prog, file = 'gotol').icon,
                       'select': IconImage(master = self.master, path_prog = self.path_prog, file = 'SelectAll').icon,
                       'search' : IconImage(master = self.master, path_prog = self.path_prog, file = 'SearchIcon').icon,
                       'replace': IconImage(master = self.master, path_prog = self.path_prog, file = 'Replace').icon,

                       'infobar': IconImage(master = self.master, path_prog = self.path_prog, file = '').icon,###################################
                       'ruban': IconImage(master = self.master, path_prog = self.path_prog, file = '').icon,###################################
                       'buttonbar': IconImage(master = self.master, path_prog = self.path_prog, file = '').icon,###################################

                       'ai': IconImage(master = self.master, path_prog = self.path_prog, file = 'AiIcon').icon,
                       
                       'puces': IconImage(master = self.master, path_prog = self.path_prog, file = 'puces').icon,
                       'news': IconImage(master = self.master, path_prog = self.path_prog, file = 'PlusIcon').icon,
                       'cstyle': IconImage(master = self.master, path_prog = self.path_prog, file = 'cstyle').icon,

                       'lst_vars': IconImage(master = self.master, path_prog = self.path_prog, file = 'ToDoIcon').icon,
                       'add_var': IconImage(master = self.master, path_prog = self.path_prog, file = 'PlusIcon').icon,
                       'place_var': IconImage(master = self.master, path_prog = self.path_prog, file = 'CursorIcon').icon,
                       
                       'comment': IconImage(master = self.master, path_prog = self.path_prog, file = 'comment').icon,
                       'uncomment': IconImage(master = self.master, path_prog = self.path_prog, file = '').icon,###################################

                       'run_python': IconImage(master = self.master, path_prog = self.path_prog, file = 'python').icon,
                       'solve': IconImage(master = self.master, path_prog = self.path_prog, file = 'solve').icon,
                       'compile': IconImage(master = self.master, path_prog = self.path_prog, file = 'compile').icon,
                       'check': IconImage(master = self.master, path_prog = self.path_prog, file = 'check').icon,
                       'run': IconImage(master = self.master, path_prog = self.path_prog, file = 'RunIcon').icon,

                       'word': IconImage(master = self.master, path_prog = self.path_prog, file = 'word').icon,
                       'pdf': IconImage(master = self.master, path_prog = self.path_prog, file = 'pdf').icon,

                       'key': IconImage(master = self.master, path_prog = self.path_prog, file = 'Password').icon,
                       
                       'archive' : IconImage(master = self.master, path_prog = self.path_prog, file = 'zip').icon,
                       'append': IconImage(master = self.master, path_prog = self.path_prog, file = 'PlusIcon').icon,
                       'compare': IconImage(master = self.master, path_prog = self.path_prog, file = 'compare').icon,

                       'send': IconImage(master = self.master, path_prog = self.path_prog, file = 'SendIcon').icon,
                       'clear': IconImage(master = self.master, path_prog = self.path_prog, file = 'clear').icon,
                       'bip': IconImage(master = self.master, path_prog = self.path_prog, file = 'bip').icon,
                       'ulla': IconImage(master = self.master, path_prog = self.path_prog, file = 'minitel').icon,

                       'update': IconImage(master = self.master, path_prog = self.path_prog, file = 'Update').icon,###################################
                       'upgrade': IconImage(master = self.master, path_prog = self.path_prog, file = 'Upgrade').icon,###################################

                       'load': IconImage(master = self.master, path_prog = self.path_prog, file = 'load').icon,
                       'rec': IconImage(master = self.master, path_prog = self.path_prog, file = 'RecIcon').icon,
##                       'play': IconImage(master = self.master, path_prog = self.path_prog, file = 'switch').icon,
                       'pause': IconImage(master = self.master, path_prog = self.path_prog, file = 'Switch').icon,
                       'carre': IconImage(master = self.master, path_prog = self.path_prog, file = 'StopIcon').icon,

                       'ihm': IconImage(master = self.master, path_prog = self.path_prog, file = 'config').icon,
                       'lnb': IconImage(master = self.master, path_prog = self.path_prog, file = 'line').icon,
                       'dark': IconImage(master = self.master, path_prog = self.path_prog, file = 'DarkIcon').icon,
                       'visut': IconImage(master = self.master, path_prog = self.path_prog, file = 'Task').icon,
                       'win': IconImage(master = self.master, path_prog = self.path_prog, file = 'windows').icon,
                       'lgv': IconImage(master = self.master, path_prog = self.path_prog, file = 'lg').icon,

                       'about': IconImage(master = self.master, path_prog = self.path_prog, file = 'HelpIcon').icon,
                       'doc': IconImage(master = self.master, path_prog = self.path_prog, file = 'DocIcon').icon,
                       'todo': IconImage(master = self.master, path_prog = self.path_prog, file = 'ToDoIcon').icon,
                       'lines': IconImage(master = self.master, path_prog = self.path_prog, file = 'line').icon,
                       'struct': IconImage(master = self.master, path_prog = self.path_prog, file = 'TreeIcon').icon,
                       'prog': IconImage(master = self.master, path_prog = self.path_prog, file = 'Prog').icon,
                       }

        self.size_images = (16, 16)
        self.size_2 = (48, 48)
        self.size_3 = (512, 512)


def convert_size():
    print("Définition des chemins d'adresse...")
    pathinput = './image/512x512/'
    pathoutput_icon = './image/16x16/'
    pathoutput_bt = './image/48x48/'

    p = Path(pathinput)
    imgs = list(p.glob('*.png'))
    for img in imgs:
        print("Image :", img.name)
        image = Image.open(pathinput + img.name)

        icon = image.resize((16, 16))
        icon.save(pathoutput_icon + img.name)

        bt = image.resize((48, 48))
        bt.save(pathoutput_bt + img.name)

    print('Fin des conversions')
    print()


if __name__ == '__main__':
    print('1. Démarrer le logiciel')
    print('2. Convertir toutes les icones de 512x512 à 48x48 et 16x16')
    if int(input('> ')) == 1:
        from __init__ import *
    else:
        convert_size()
        from __init__ import *

