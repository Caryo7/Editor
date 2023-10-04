#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from pathlib import Path
import zipfile
import sys
import os

from pswd import *
from confr import *

PATH_PROG = '.'#os.path.abspath(os.getcwd())

class LgViewer:
    def __init__(self, master = None):
        Password(self.create, tk = master)
        #self.create()

    def create(self):
        self.master = Tk()
        self.master.title('Lg Viewer')
        self.master.iconbitmap(PATH_PROG + '/image/icons/lg.ico')
        self.master.resizable(False, False)

        def write_temp():
            if askyesno('', 'Configmation'):
                self.write_temp()

        menu = Menu(self.master)
        self.master['menu'] = menu
        menu.add_command(label = 'Ouvrir', command = self.open)
        menu.add_command(label = 'Quitter', command = self.master.destroy)
        menu.add_command(label = 'Actualiser', command = self.insert_data)
        menu.add_command(label = 'Ecrire temp/', command = write_temp)
        menu.add_command(label = 'Ajouter', command = self.append)
        self.open()
        self.Generate()

    def open(self):
        self.file = askopenfilename(title = 'Open', initialdir = '.', filetypes = [('Language Files', '*.lg')])
        if self.file:
            self.get_columns()

            try:
                self.tree.destroy()
                self.scroll.destroy()
            except AttributeError:
                pass

            self.tree = ttk.Treeview(self.master, show = 'headings', columns = self.columns, height = 30, selectmode = 'browse')
            scroll = ttk.Scrollbar(self.master, orient = 'vertical', command = self.tree.yview)
            self.tree.place(x = 0, y = 0)
            self.tree.configure(yscrollcommand=scroll.set)

            largeur = int(self.master.winfo_screenwidth() / (len(self.columns) + 1))
            for i in range(len(self.columns)):
                self.tree.heading(i, text = self.columns_name[i])
                self.tree.column(i, width = largeur)

            scroll.place(x = largeur * (i + 1) + 2, y = 0, height = self.tree.winfo_reqheight())
            self.master.geometry(str((largeur * (i + 1)) + 2 + scroll.winfo_reqwidth()) + 'x' + str(self.tree.winfo_reqheight()))
            self.master.update()
            self.insert_data()
            self.tree.bind('<Double-Button-1>', self.modify)
            self.tree.bind('<Button-3>', self.clkright)

        else:
            self.master.destroy()

    def append(self):
        lgs = []
        for col in self.columns_name:
            lgs.append((col, ''))
        self.Popup(lgs, self.master, 'Ajouter')

    def Popup(self, lgs, master, type):
        assert type in ('Change', 'Ajouter')
        self.mode = type
        self.root = Toplevel()
        self.root.iconbitmap(PATH_PROG + '/image/icons/lg.ico')
        self.root.transient(master)
        self.root.title(type)
        self.root.resizable(False, False)

        Label(self.root, text = 'Champs : ', font = ('Consolas', 16, 'bold')).place(x = 50, y = 10)
        n = 0
        inter = 50
        self.dic = {}
        for name, texte in lgs:
            self.dic[name] = {'text': texte}
            self.dic[name]['label'] = Label(self.root, text = name, font = ('Consolas', 13))
            self.dic[name]['label'].place(x = 10, y = 50 + (n * inter))
            self.dic[name]['stringVar'] = StringVar()
            self.dic[name]['entry'] = ttk.Entry(self.root, font = ('Consolas', 14), width = 40)
            self.dic[name]['entry'].place(x = 100, y = 50 + (n * inter))
            self.dic[name]['entry'].config(textvariable = self.dic[name]['stringVar'])
            self.dic[name]['entry'].insert('0', self.dic[name]['text'])
            if name == 'Caller' and type == 'Change':
                self.dic[name]['entry'].config(stat = 'disabled')
            n += 1

        self.root.geometry(str(self.dic[name]['entry'].winfo_reqwidth() + 100 + 20) + 'x' + str(50 + (n * inter) + 50))
        Button(self.root, text = 'OK', command = self.validate).place(x = 50, y = (40 + (n * inter)))
        Button(self.root, text = 'Annuler', command = self.root.destroy).place(x = 150, y = (40 + (n * inter)))

    def validate(self):
        self.new = []
        for k, v in self.dic.items():
            self.new.append((v['text'], v['stringVar'].get()))

        self.root.destroy()
        if '' not in self.new:
            zp = zipfile.ZipFile(self.file)
            lst = zp.namelist()
            zp.close()
            i = -1
            for name in lst:
                if name[-5:] != '.lang':
                    z = zipfile.ZipFile(self.file)
                    f = open('temp/' + name, 'wb')
                    f.write(z.read(name))
                    f.close()
                    z.close()
                    continue
                else:
                    i += 1

                caller = self.new[0][1]
                value = self.new[i + 1][1]
                if self.mode == 'Ajouter':
                    z = zipfile.ZipFile(self.file)
                    f = open('temp/' + name, 'wb')
                    f.write(z.read(name) + str('\n' + caller + ' = ' + value).encode(get_encode()))
                    f.close()
                    z.close()

                elif self.mode == 'Change':
                    z = zipfile.ZipFile(self.file)
                    f = open('temp/' + name, 'wb')
                    rode = []
                    for line in z.read(name).split(b'\n'):
                        ln = line.split(b' = ')
                        if ln != '':
                            if ln[0] == caller.encode(get_encode()):
                                ln[1] = value.encode(get_encode())
                            rode.append(b' = '.join(ln))
                    f.write(b'\n'.join(rode))
                    f.close()
                    z.close()
            self.write_temp()

    def delete(self, evt):
        caller = self.tree.item(self.tree.selection())['values'][0]
        self.tree.delete(self.tree.selection())
        for name in self.columns_name:
            if name == 'Caller':
                continue

            z = zipfile.ZipFile(self.file)
            f = open('temp/' + name, 'wb')
            rode = []
            for line in z.read(name).split(b'\n'):
                ln = line.split(b' = ')
                if ln != '':
                    if ln[0] == caller.encode(get_encode()):
                        ln = []
                    rode.append(b' = '.join(ln))
            f.write(b'\n'.join(rode))
            f.close()
            z.close()
        self.write_temp()

    def write_temp(self):
        p = Path('temp')
        tt = list(p.glob('**/*'))
        z = zipfile.ZipFile(self.file, 'w')
        for name in tt:
            if '.lang' in str(name):
                f = open(str(name), 'rb')
                name = str(name).replace('temp/', '')
                name = str(name).replace('temp\\', '')
                zp = z.open(name, 'w')
                zp.write(f.read())
                zp.close()
                f.close()

        z.close()
        self.insert_data()

    def clkright(self, evt):
        m = Menu(self.master, tearoff = 0)
        m.add_command(label = 'Supprimer', command = lambda: self.delete(evt))
        m.tk_popup(evt.x_root, evt.y_root)

    def Generate(self):
        self.master.mainloop()

    def modify(self, evt):
        selected = self.tree.item(self.tree.selection())['values']
        lgs = []
        for i in range(len(selected)):
            lgs.append((self.columns_name[i], selected[i]))
        self.Popup(lgs, self.master, 'Change')

    def insert_data(self):
        for x in self.tree.get_children():
            self.tree.delete(x)
        z = zipfile.ZipFile(self.file)
        value = []
        for name in self.columns_name:
            if name == 'Caller':
                continue

            value.append([])
            caller = []
            for cmds in z.read(name).decode(get_encode()).replace('\r', '').split('\n'):
                if cmds != '' and cmds.split(' = ')[0][0] != '[':
                    value[-1].append(cmds.split(' = ')[1])
                    caller.append(cmds.split(' = ')[0].lower())

        for c in range(len(value[0])):
            rows = [caller[c]] + [value[i][c] for i in range(len(value))]
            self.tree.insert('', 'end', value = rows)

    def get_columns(self):
        z = zipfile.ZipFile(self.file)
        self.columns_name = ['Caller'] + z.namelist()
        z.close()
        n = 0
        for i in range(len(self.columns_name)):
            if self.columns_name[n][-5:] != '.lang' and self.columns_name[n] != 'Caller':
                self.columns_name.pop(n)
            else:
                n += 1
        self.columns = [i for i in range(len(self.columns_name))]

if __name__ == '__main__':
    l = LgViewer()
