#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from glob import glob # glob
import os, time
from tooltip import *

try:
    import win32api
    import win32print
except ImportError:
    from errors import *
    ERROR(2)

from confr import *

class Printer:
    def __printer__(self):
        ""
        
    def print_window(self, evt=None):
        self.askprinter()

    def askprinter(self):
        try:
            self.all_printers = [printer[2] for printer in win32print.EnumPrinters(2)]
            maxi = 0
            for i in self.all_printers:
                if len(i) > maxi:
                    maxi = len(i)
        except NameError:
            self.all_printers = []
            maxi = 20

        self.root = Tk()
        self.root.iconbitmap(self.ico['printer'])
        self.root.resizable(width = False, height = True)
        self.root.title(lg('print'))
        Label(self.root, text = lg('caimp'), font = ('Consolas', 14)).place(x = 10, y = 10)
        self.lst = Listbox(self.root, font = ('Consolas', 13), width = maxi, height = 10, selectmode = MULTIPLE)
        self.lst.place(x = 10, y = 50)
        for printer in self.all_printers:
            self.lst.insert('end', printer)

        Label(self.root, text = lg('exemp'), font = ('Consolas', 14)).place(x = 10, y = 295)
        self.spin = ttk.Spinbox(self.root, from_ = 1, to_ = 99, font = ('Consolas', 15), width = 5)
        self.spin.place(x = 10, y = 325)
        self.spin.set(1)

        self.rv = IntVar()
        self.rsv = ttk.Checkbutton(self.root, onvalue = 1, offvalue = 0, variable = self.rv, text = lg('resve'))
        self.rsv.place(x = 10, y = 365)
        ToolTip(self.rsv, text = lg("notimp")) #############

        Button(self.root, text = lg('startimp'), command = self.begin).place(x = 10, y = 395)
        Button(self.root, text = lg('close'), command = self.root.destroy).place(x = 10, y = 430)

        self.l = Label(self.root, text = lg('stnpr'), font = ('Consolas', 11))
        self.l.place(x = 10, y = 465)
        self.l.config(foreground = 'blue')

        self.root.geometry(str(330) + 'x' + str(500))

    def begin(self):
        selected = self.lst.curselection()
        if len(selected) == 0:
            showerror(lg('print'), lg('vdsui'))
            return

        self.export_pdf(True, lambda : self.start_print(selected))

    def start_print(self, selected):
        for itp in selected:
            win32print.SetDefaultPrinter(self.all_printers[itp])
            pdf_dir = self.path_prog + '/temp\\temp_pdf.pdf'
            for nb in range(int(self.spin.get())):
                for f in glob(pdf_dir, recursive = True):
                    win32api.ShellExecute(0, "print", f, None,  ".",  0)

        self.root.destroy()


if __name__ == '__main__':
    from __init__ import *
