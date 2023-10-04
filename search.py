#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from confr import *

class Search:
    def end_dialoging(self, zak):
        self.dialoging = False
        zak.destroy()

    def search(self, evt=None):
        if not(self.dialoging):
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'search', 'evt': evt})

            zak = Toplevel(self.master)
            zak.iconbitmap(self.ico['search'])
            zak.protocol('WM_DELETE_WINDOW', lambda : self.end_dialoging(zak))
            zak.transient(self.master)
            zak.title(lg('Search'))
            zak.resizable(width=False, height=False)

            Label(zak, text=lg('Keyword')).grid(row=0, column=0, sticky='e', padx = 5, pady = 5)
            Label(zak, text = 'Direction').grid(row = 2, column = 0, sticky = 'e', padx = 5, pady = 5)

            self.keyword_ = StringVar(master = self.master)
            self.keyword = ttk.Entry(zak, textvariable=self.keyword_, width=50)
            self.keyword.grid(row=0, column=1, sticky='w', padx = 5, pady = 5)
            self.keyword.bind('<Key>', self.resa)

            self.casse = IntVar(master = self.master)
            self.casse.set(0)
            casse = ttk.Checkbutton(zak, onvalue = 1, offvalue = 0, variable = self.casse, text = lg('match_cas'), command = self.resa)
            casse.grid(row = 1, column = 1, padx = 5, pady = 5)

            cdr = Frame(zak)
            cdr.grid(row = 2, column = 1)
            self.direction = StringVar(master = self.master)
            self.direction.set('d')
            up = ttk.Radiobutton(cdr, text = lg('Up'), variable = self.direction, value = 'u', command = self.resa)
            up.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = 'e')
            down = ttk.Radiobutton(cdr, text = lg('Down'), variable = self.direction, value = 'd', command = self.resa)
            down.grid(row = 0, column = 1, padx = 5, pady = 5, sticky ='w')

            b1 = ttk.Button(zak, text=lg('next'), command=self._search).grid(row=0, column=2, sticky='e', padx = 5, pady = 5)
            b2 = ttk.Button(zak, text=lg('Close'), command=lambda: self.end_dialoging(zak)).grid(row=1, column=2, sticky='e', padx = 5, pady = 5)
            self.searched = False
            self.indexitem = -1

    def resa(self, evt = None):
        self.searched = False
        self.indexitem = -1

    def _search(self):
        mot = self.keyword_.get()
        casse = not bool(self.casse.get())
        direc = self.direction.get()
        if not self.searched:
            dep, start = '0.0', '0.0'
            self.itemresults = []
            while True:
                start = self.text.search(mot, dep, END, nocase = casse)
                if not start:
                    break
    
                end = '{0}+{1}c'.format(start, len(mot))
                end = self.text.index(end)
                self.itemresults.append({'start': start, 'end': end, 'mot': mot})
                dep = self.text.index('{}+1c'.format(end))

            if len(self.itemresults) == 0:
                showwarning(lg('search'), lg('no_results'))
            else:
                self.searched = True
                self._search()

        else:
            if direc == 'd':
                self.indexitem += 1
                self.indexitem %= len(self.itemresults)
            else:
                self.indexitem -= 1
                if self.indexitem < 0:
                    self.indexitem += len(self.itemresults)

            item = self.itemresults[self.indexitem]

            self.text.tag_remove(SEL, '1.0', 'end')
            self.text.tag_add(SEL, item['start'], item['end'])
            self.text.mark_set(INSERT, item['start'])
            self.text.see(INSERT)
            self.text.focus_set()

    def replace(self, evt=None):
        if not(self.dialoging):
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'replace', 'evt': evt})

            zak = Toplevel(self.master)
            zak.iconbitmap(self.ico['replace'])
            zak.protocol('WM_DELETE_WINDOW', lambda : self.end_dialoging(zak))
            zak.transient(self.master)
            zak.title(lg('Replace'))
            zak.resizable(width=False, height=False)
            Label(zak, text=lg('Keyword')).grid(row=0, column=0, sticky='e')
            Label(zak, text=lg('Replace_by')).grid(row=1, column=0, sticky='e')
            Label(zak, text=lg('Type')).grid(row=2, column=0, sticky='e')
            self.keyword_ = StringVar()
            replace_ = StringVar()
            type__ = [lg('General'), lg('Match_casse')]
            self.keyword = ttk.Entry(zak, textvariable=self.keyword_, width=50)
            replace = ttk.Entry(zak, textvariable=replace_, width=50)
            self.type_ = ttk.Combobox(zak, values=type__)
            self.keyword.grid(row=0, column=1, sticky='w')
            replace.grid(row=1, column=1, sticky='w')
            self.type_.grid(row=2, column=1, sticky='w')
            self.type_.current(0)
            Button(zak, text=lg('Search'), command=self._search).grid(row=0, column=2, sticky='e')
            Button(zak, text=lg('Replace')).grid(row=1, column=2, sticky='e')
            Button(zak, text=lg('Close'), command=zak.destroy).grid(row=2, column=2, sticky='e')

    def gotol(self, evt=None, line = None):
        if not(self.dialoging):
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'gotol', 'evt': evt, 'line': line})

            if line:
                nb = line
            else:
                nb = askinteger(self.title, lg('WLDYWTG'))

            self.text.tag_add(SEL, str(nb) + ".0", str(nb) + ".100000")
            self.text.mark_set(INSERT, str(nb) + ".0")
            self.text.focus_set()
            self.dialoging = False

    def comment(self):
        if not(self.dialoging):
            if self.mode_record:
                self.events.append({'command': 'comment'})

            self.text.insert(INSERT, '# ')

    def selectall(self):
        self.text.tag_add(SEL, "1.0", END)
        self.text.mark_set(INSERT, "1.0")
        self.text.see(INSERT)

    def copy(self):
        if not(self.dialoging):
            if self.mode_record:
                self.events.append({'command': 'copy'})

            self.text.clipboard_clear()
            try:
                self.text.clipboard_append(self.text.selection_get())
            except TclError:
                self.error(7)

    def past(self):
        if not(self.dialoging):
            if self.mode_record:
                self.events.append({'command': 'past'})

            try:
                self.text.insert(INSERT, self.text.clipboard_get())
                self.texte += self.text.clipboard_get()
            except TclError:
                self.error(8)

    def cut(self):
        if not(self.dialoging):
            if self.mode_record:
                self.events.append({'command': 'cut'})

            self.copy()
            self.text.delete('sel.first', 'sel.last')

    def undo(self, evt=None):
        if not(self.dialoging):
            if self.mode_record:
                self.events.append({'command': 'undo', 'evt': evt})

            try:
                self.text.edit_undo()
            except TclError:
                pass

    def redo(self, evt=None):
        if not(self.dialoging):
            if self.mode_record:
                self.events.append({'command': 'redo', 'evt': evt})

            try:
                self.text.edit_redo()
            except TclError:
                pass

if __name__ == '__main__':
    from __init__ import *
    #RunTestMacro(inst='search')
