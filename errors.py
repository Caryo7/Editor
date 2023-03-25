#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from confr import *

mode = False
lst = []
cores = ['AttributeError : Printing function is not implemented !\nFirst, the program have to export to pdf your file !!!',
         'ImportError : No module named "win32api" !\nYou are not able to print a document !',
         'AttributeError : Command is not implemented !',
         'ImportError : No module named "reportlab" !',
         'ImportError : No module named "docx" !',
         'ImportError : No module named "Serial" !',
         'TclError :  Selection empty (not able to copy) !',
         'TclError :  Selection empty (not able to cut) !',
         'SerialError : No port for serial utils (Minitel (.py)) !',
         'MacroError : Macro Error !',
         'ProcessError : Ne peut pas tuer le processus choisit lg("tpinka") !']

class ErrorBox:
    def __init__(self, id):
        self.id = int(id)
        self.root = Toplevel()
        #self.root.iconbitmap(self.path_prog + '/image/error.ico')#
        self.root.transient()
        self.root.protocol('WM_DELETE_WINDOW', self.close)
        self.root.bind('<Return>', self.close)
        self.root.bind('<Escape>', self.close)

        self.root.title(lg('Error'))
        i = PhotoImage(file = 'image/error.png')
        #Label(self.root, image = i).place(x = 10, y = 50)
        Label(self.root, text = lg('aeo'), font = ('Consolas', 12)).place(x = 10, y = 10)
        Label(self.root, text = lg('error') + ' ' + id, font = ('Consolas', 15, 'bold')).place(x = 100, y = 50)
        self.p = Button(self.root, text = '+', command = self.plus)
        self.p.place(x = 200, y = 100)
        Button(self.root, text = lg('close'), command = self.close).place(x = 10, y = 100)
        self.root.geometry(str(300) + 'x' + str(160))

    def close(self, evt = None):
        self.root.destroy()

    def plus(self):
        self.p.config(text = '-')
        self.p.config(command = self.moins)
        self.l = Label(self.root, text = cores[self.id - 1], wraplength = 275, font = ('Consolas', 13, 'italic'), justify = 'left')
        self.l.place(x = 10, y = 150)
        self.root.geometry(str(300) + 'x' + str(160 + self.l.winfo_reqheight()))

    def moins(self):
        self.p.config(text = '+')
        self.p.config(command = self.plus)
        self.l.destroy()
        self.root.geometry(str(300) + 'x' + str(160))


def ERROR(id):
    global mode
    if get_berror():
        if mode:
            ErrorBox(str(id))
        else:
            lst.append(id)

class Errors:
    def __errors__(self):
        "List of errors :"
        # 1 - AttributeError : Printing function not implemented
        # 2 - ImportError    : No module name "shlex"
        # 3 - AttributeError : Command not implemented
        # 4 - ImportError    : No module name "reportlab"
        # 5 - ImportError    : No module name "docx"
        # 6 - ImportError    : No module name "serial"
        # 7 - TclError       : Selection empty (copy)
        # 8 - TclError       : Selection empty (cut)
        # 9 - SerialError    : No port for serial utils (Minitel (.py))
        # 10 - MacroError    : Macro Error
        # 11 - ProcessError  : Ne peut pas tuer le processus choisit lg('tpinka')
        
    def error(self, id):
        ERROR(id)

    def runErrors(self):
        global mode
        mode = True
        try:
            for err in lst:
                ERROR(err)
        except:
            pass



if __name__ == '__main__':
    from __init__ import *
