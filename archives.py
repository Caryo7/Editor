#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zipfile as zipfile
import os, time
from confr import *
from tkinter import *
from tkinter.messagebox import *

class Archives:
    def __arch__(self):
        ""
        
    def create_a(self):
        z = zipfile.ZipFile(self.path + '.zip', 'w')
        z.close()
        
    def add_new_version(self):
        if self.path != 'untitled.x':
            try:    
                z = zipfile.ZipFile(self.path + '.zip', mode='a')
                f = open(self.path, 'rb')
                nb = len(self.path) - 1
                while self.path[nb] != '/':nb -= 1
                nb += 1
                self.vername = 'Version ' + str(hex(int(time.time())))
                r = z.open(self.vername + '/' + self.path[nb:], mode='w')
                r.write(f.read())
                r.close()
                f.close()
                z.close()
            except:
                self.create_a()
                self.add_new_version()

    def start_analyse(self):
            z = zipfile.ZipFile(self.path + '.zip', mode='r')
            if int(self.cpl1.get())-1 > len(self.lv) and int(self.cpl2.get())-1 > len(self.lv):
                showerror(lg('Archive'), lg('BI'))
            else:
                ver = (int(self.cpl1.get())-1, int(self.cpl2.get())-1)
                self.cpl1.set('')
                self.cpl2.set('')
                couple = (self.lv[ver[0]], self.lv[ver[1]])
                f1 = z.open(couple[0][1], 'r')
                f2 = z.open(couple[1][1], 'r')
                r1 = f1.read().decode()
                r2 = f2.read().decode()
                f1.close()
                f2.close()
                t = 0
                i = -1
                if len(r1) != len(r2):
                    t = abs(len(r1) - len(r2))
                while True:
                    i += 1
                    try:
                        if r1[i] != r2[i]:
                            showwarning(lg('Archive'), lg("DAC") + str(i))
                            t += 1
                    except IndexError:
                        break
                if t == 0:
                    showinfo(lg('Archive'), lg('VI'))
                else:
                    showwarning(lg('Archive'), lg('NDD') + ' : ' + str(t))
                z.close()

    def compare(self):
        if self.dialoging:
            return

        self.dialoging = True
        if os.path.exists(self.path + '.zip'):
            z = zipfile.ZipFile(self.path + '.zip', mode='r')
            l = z.namelist()
            z.close()
            self.lv = []
            self.zak = Toplevel(self.master)
            self.zak.transient(self.master)
            self.zak.iconbitmap(self.ico['archive'])
            self.zak.title(lg('Archive'))
            lst = Listbox(self.zak, width=30, height=10)
            lst.grid(row=0, column=0)
            nb = 0
            for i in l:
                nb += 1
                n = 0
                while i[n] != '/':n += 1
                v = str(i[:n]).replace('Version ', '')
                lst.insert(END, str(nb) + ' : ' + v)
                self.lv.append((v, i))
            c = Frame(self.zak)
            c.grid(row=1, column=0)
            Label(c, text='1 : ').grid(row=0, column=0, sticky='e')
            Label(c, text='2 : ').grid(row=1, column=0, sticky='e')
            self.cpl1 = StringVar(master = self.master)
            self.cpl1_ = Entry(c, textvariable=self.cpl1, width=26)
            self.cpl1_.grid(row=0, column=1, sticky='w')
            self.cpl2 = StringVar(master = self.master)
            self.cpl2_ = Entry(c, textvariable=self.cpl2, width=26)
            self.cpl2_.grid(row=1, column=1, sticky='w')
            Button(self.zak, text=lg('OK'), command=self.start_analyse).grid(row=2, column=0)

        self.dialoging = False

        

"""if __name__ == '__main__':
    t = Archives()
    t.__arch__()
    t.master = Tk()
    t.path = '/home/caryo/Documents/Programmation/Python/Templates/Edit/test.txt'
    t.add_new_version()
    t.compare()"""

if __name__ == '__main__':
    from __init__ import *
