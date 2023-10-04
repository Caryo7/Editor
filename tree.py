#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
from pathlib import Path
import os

PATH_PROG = '.'#os.path.abspath(os.getcwd())

class Struct:
    def __init__(self):
        p = Path(PATH_PROG)
        lst = list(p.glob('**/*.py'))
        lst += list(p.glob('**/*.pyw'))
        lst_all_files = list(p.glob('**/*.*'))
        self.files = len(lst_all_files)

        for i in range(len(lst)):
            lst[i] = str(lst[i])

        self.bal = []
        self.fncts = 0
        self.classes = 0
        self.variables = 0
        for file in lst:
            try:
                f = open(file, 'r', encoding = get_encode())
                self.bal.append(lg('File') + ' : ' + file)
                tab = ' | '
                r = f.read()
                self.variables += r.count(' = ')

                for line in r.split('\n'):
                    if not line:
                        continue

                    #print(line.encode())
                    line = list(line)
                    try:
                        while line[0] == ' ':
                            line.pop(0)
                    except:
                        pass

                    line = ''.join(line)
                    if line == '':
                        continue

                    if line[:6] == 'class ':
                        self.classes += 1
                        if tab == ' |-- ':
                            tab = ' | '
                        n = 0
                        while line[n] not in ('(', ':'):n += 1
                        self.bal.append(tab + 'class ' + line[6:n])
                        tab = ' |-- '
                    
                    elif line[:4] == 'def ':
                        self.fncts += 1
                        n = 0
                        while line[n] not in ('(', ':'):n += 1
                        self.bal.append(tab + 'def ' + line[4:n])

                f.close()
                self.bal.append(' +-\n')
            except UnicodeDecodeError:
                pass

    def get(self):
        return self.bal

    def getFncts(self):
        return self.fncts

    def getClasses(self):
        return self.classes

    def getFiles(self):
        return self.files

    def getVariables(self):
        return self.variables


def code(path_prog):
    text = ''
    p = Path(path_prog)
    tt = list(p.glob('**/*.py')) + list(p.glob('**/*.pyw'))
    for fl in tt:
        file = str(fl)
        try:
            text += '\n############################################'
            text += '#' * (len(file) + 9)
            text += '\n'
            text += '###################### FILE : ' + str(file) + ' ######################\n'
            text += '############################################'
            text += '#' * (len(file) + 9)
            text += '\n\n'
            f = open(file, 'r', encoding = get_encode())
            text += f.read()
            f.close()
        except Exception as e:
            text += '### FILE : ' + file + '\n'
            text += '### ERROR : ' + str(e) + '\n'

    return text

def nbFncts():
    return Struct().getFncts()

def nbClasses():
    return Struct().getClasses()

def nbFiles():
    return Struct().getFiles()

def nbVariables():
    return Struct().getVariables()


class Code:
    def __init__(self, master, path_prog):
        self.path_prog = path_prog
        self.master = Toplevel(master)
        self.master.transient(master)
        self.master.iconbitmap(self.path_prog + '/image/icons/tree.ico')
        self.master.title(lg('program'))
        self.master.resizable(False, False)
        
        self.text = Text(self.master, width = 500, height = 40, bg = get_bgd(), fg = get_fgd())
        trw = 646
        scroll = Scrollbar(self.master, orient = 'vertical', command = self.text.yview)
        self.text.config(yscrollcommand = scroll.set)
        self.text.place(x = 0, y = 0)
        scroll.place(x = trw, y = 0, height = self.text.winfo_reqheight())
        b = Button(self.master, text = lg('close'), command = self.master.destroy)
        b.place(x = int((trw + scroll.winfo_reqwidth() - (b.winfo_reqwidth() / 2)) / 2), y = self.text.winfo_reqheight())
        self.master.bind_all('<Escape>', lambda evt: self.master.destroy())
        self.master.geometry(str(trw + scroll.winfo_reqwidth()) + 'x' + str(self.text.winfo_reqheight() + b.winfo_reqheight()))

        self.insert()

    def insert(self):
        self.text.insert('0.0', code(self.path_prog))
        self.text.config(stat = 'disabled')

    def Generate(self):
        self.master.mainloop()


class Tkin:
    def __init__(self, master, path_prog):
        self.path_prog = path_prog
        self.master = Toplevel(master)
        self.master.transient(master)
        self.master.iconbitmap(self.path_prog + '/image/icons/tree.ico')
        self.master.title(lg('Struct'))
        self.master.resizable(False, False)
        
        self.text = Text(self.master, width = 80, height = 20, bg = get_bgd(), fg = get_fgd())
        scroll = Scrollbar(self.master, orient = 'vertical', command = self.text.yview)
        self.text.config(yscrollcommand = scroll.set)
        self.text.place(x = 0, y = 0)
        scroll.place(x = self.text.winfo_reqwidth(), y = 0, height = self.text.winfo_reqheight())
        b = Button(self.master, text = lg('close'), command = self.master.destroy)
        b.place(x = int((self.text.winfo_reqwidth() + scroll.winfo_reqwidth() - (b.winfo_reqwidth() / 2)) / 2), y = self.text.winfo_reqheight())
        self.master.bind_all('<Escape>', lambda evt: self.master.destroy())
        self.master.geometry(str(self.text.winfo_reqwidth() + scroll.winfo_reqwidth()) + 'x' + str(self.text.winfo_reqheight() + b.winfo_reqheight()))

        self.insert()

    def tag_place(self, text, name, ln, first):
        i = self.text.index('insert')
        n = 0
        self.text.insert('end', text)
        run = False
        for n in range(ln):
            if self.text.get(i) == first:
                run = True
            if run:
                self.text.tag_add(name, i)
            i = self.text.index('{}+1char'.format(i))
            n += 1

        while n < len(text):
            n += 1
            self.text.tag_add('name', i)
            i = self.text.index('{}+1char'.format(i))

        self.text.insert('end', '\n')

    def insert(self):
        s = Struct()
        balises = s.get()
        for b in balises:
            if 'Fichier' in b:
                self.tag_place(b, 'file', 7, 'F')
            elif 'class' in b:
                self.tag_place(b, 'class', 8, 'c')
            elif 'def' in b:
                if b[5] == 'd':
                    self.tag_place(b, 'def', 9, 'd')
                elif b[3] == 'd':
                    self.tag_place(b, 'def', 6, 'd')
            else:
                self.text.insert('end', b + '\n')
            

        self.text.tag_config('file', foreground = '#ffff00')
        self.text.tag_config('class', foreground = '#ffa500')
        self.text.tag_config('def', foreground = '#71c970')
        self.text.tag_config('name', foreground = '#00c4ff')

        self.text.config(stat = 'disabled')

    def Generate(self):
        self.master.mainloop()

if __name__ == '__main__':
    from __init__ import *
