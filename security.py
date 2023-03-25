#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.messagebox import *
from confr import *

class conn:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.root = Tk()
        self.root.iconbitmap(self.ico['security'])
        self.root.title(lg('Connexion'))
        self.root.wm_attributes('-topmost', 1)
        self.root.protocol('WM_DELETE_WINDOW', self.nothing)
        self.content()
        self.nb = 3
        self.stat = False
        
    def nothing(self):""
    
    def Quitter(self):
        self.root.destroy()
        self.master.destroy()
        
    def content(self):
        Label(self.root, text=lg('Username')).grid(row=0, column=0)
        Label(self.root, text=lg('Password')).grid(row=1, column=0)
        usn = StringVar()
        pwd = StringVar()
        self.usern = Entry(self.root, textvariable=usn, width=20, stat='disabled')
        self.passw = Entry(self.root, textvariable=pwd, width=20, stat='disabled', show='*')
        self.usern.grid(row=0, column=1)
        self.passw.grid(row=1, column=1)
        self.bt = Button(self.root, text=lg('Connexion'), command=self.connect, stat='disabled')
        self.bt.grid(row=2, column=1)
        self.bt.bind_all('<Return>', self.connect)
        self.root.update()
        self.x -= int(self.root.winfo_reqwidth() / 2)
        self.root.geometry('+' + str(self.x) + '+' + str(self.y))
        
    def connect(self, evt=None):
        if self.passw.get() == get_pwd() and self.usern.get() == get_usn():
            self.Quitter()
            self.stat = True
        else:
            if self.nb == 1:
                self.Quitter()
                exit(code='BadPassWord')
            else:
                self.nb -= 1
                self.bt.unbind_all('<Return>')
                showwarning(lg('Connexion'), 'Attention : plus que ' + str(self.nb) + ' tentatives !')
                self.bt.bind_all('<Return>', self.connect)

    def active(self, master):
        self.master = master
        self.bt['stat'] = 'normal'
        self.usern['stat'] = 'normal'
        self.passw['stat'] = 'normal'
        self.root.mainloop()


if __name__ == '__main__':
    from __init__ import *
