#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from pathlib import Path
import os, sys

class installer:
    def install(self):
        if not(get_installed()):self.create()
        else:self.already()
        
    def create(self):
        self.win()
        self.content()
        self.generate()
        
    def generate(self):
        self.root.mainloop()
        
    def win(self):
        self.root = Tk()
        self.root.iconbitmap('image/installer.ico')
        self.root.title('Setup wizzard')
        self.root.resizable(width=False, height=False)
        
    def content(self):
        Label(self.root, text='Directory').grid(row=0, column=0)
        self.dir_ = StringVar()
        self.dir = Entry(self.root, textvariable=self.dir_, width=60)
        self.dir.grid(row=0, column=1)
        Button(self.root, text='...', width=3, command=self.selectpath).grid(row=0, column=2)
        self.cdu_ = IntVar()
        self.cdu = Checkbutton(self.root, text='I agree to user conditions', variable=self.cdu_, offvalue=0, onvalue=1)
        self.cdu.grid(row=1, column=1, sticky='w')
        Button(self.root, text='Install', command=self.installation).grid(row=2, column=1, sticky='w')

    def name(self, file):
        nb = len(file)-1
        path = file.replace('\\', '/')
        while path[nb] != '/':nb -= 1
        nb += 1
        return path[nb:]
    
    def installation(self):
        dem = askyesnocancel('Setup Wizzard', 'Do you want to confirm installation ?')
        if dem == False:
            self.root.destroy()
        elif dem == None:""
        else:
            if self.cdu_.get() == 1:
                write('installer', 'installed', '1')
                p = Path()
                tt = list(p.glob('**/*'))
                lst = []
                for i in tt:lst.append(str(i))
                direc = self.dir_.get()
                for i in lst:
                    p = Path(i)
                    t = i.split('/')
                    if p.is_file() and '__pycache__' not in t:
                        fr = open(i, 'r', encoding='UTF-8')
                        fw = open(direc + '/' + i, 'w', encoding='UTF-8')
                        fw.write('\n'.join(fr.readlines()))
                        #print(i, '\n'.join(fr.read()))
                        fw.close()
                        fr.close()
                showinfo('Setup Wizzard', 'Installation finished !')
                self.root.destroy()
            else:
                showerror('Setup Wizzard', 'You must accept condition of utilisation')
            
    def selectpath(self):
        name = askdirectory(title='Open Path')
        self.dir_.set(name)
        
    def already(self):
        self.win()
        self.content()
        showwarning('Setup Wizzard', 'The program is already installed !')
        self.root.destroy()

if __name__ == '__main__':
    t = installer()
    t.install()
