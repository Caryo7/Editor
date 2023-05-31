#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from confr import *

class TasksViewer:
    def __viewer__(self):
        self.lst_tasks = []
        self.lst_fnct = {}
        self.nb = 1
        
    def show(self):
        self.zak = Toplevel(self.master)
        self.zak.iconbitmap(self.ico['task'])
        self.zak.title(lg('TaV'))
        self.zak.transient(self.master)
        self.zak.resizable(width=False, height=False)
        self.tree = ttk.Treeview(self.zak, height=10, show='headings', columns=('Id', 'Name', 'Start Time', 'Stat', 'Loop'))
        self.tree.grid(row=0, column=0)
        self.tree.heading('Id', text=lg('Id'))
        self.tree.heading('Name', text=lg('Name'))
        self.tree.heading('Start Time', text=lg('ST'))
        self.tree.heading('Stat', text=lg('Stat'))
        self.tree.heading('Loop', text=lg('Loop'))
        self.tree.column('Id', width=35)
        self.tree.column('Name', width=200)
        self.tree.column('Start Time', width=145)
        self.tree.column('Stat', width=75)
        self.tree.column('Loop', width=60)
        for i in self.lst_tasks:
            self.tree.insert('', 'end', values=i)
        self.tree.bind('<Double-Button-1>', self.evt_tasks)
        self.tree.bind('<Button-3>', self.clkr)

    def clkr(self, evt):
        popup = Menu(self.zak, tearoff=0)
        popup.add_command(label=lg('kill'), command=lambda : self.kill(evt))
        popup.add_command(label=lg('info'), command=lambda : self.evt_tasks(evt))
        popup.tk_popup(evt.x_root, evt.y_root)

    def bool_str(self, string):
        if string == 'True':
            return True
        else:
            return False

    def kill(self, evt):
        s = self.tree.item(self.tree.selection())['values']

        if (not self.bool_str(s[-1])) or (s[3] in (lg('stopped'), lg('proto'))):
            #self.error(11)
            showerror(self.title, lg('tpinka'))
        else:
            showinfo(self.title, lg('tmcip'))
            self.set_taskstat(s[1], lg('killed'))
            self.zak.destroy()
            self.show()
        
    def evt_tasks(self, evt):
        select = self.tree.item(self.tree.selection())['values'][0] - 1
        showinfo(lg('TaV'), self.lst_tasks[select][5])
        
    def add_task(self, code, time, desc=None, killable = True, fnct = None):
        self.lst_tasks.append([self.nb, code, str(hex(int(time*1000))), lg('Running'), desc[:4], desc, fnct, killable])
        self.lst_fnct[fnct] = False
        self.nb += 1

    def finish_task(self, code, nom = lg('Stopped')):
        for id, cd, _, _, _, _, fnct, _ in self.lst_tasks:
            if cd == code:
                self.lst_tasks[id - 1][3] = nom
                self.lst_fnct[fnct] = True

    def set_taskstat(self, code, stat):
        self.finish_task(code = code, nom = stat)

if __name__ == '__main__':
    from __init__ import *
