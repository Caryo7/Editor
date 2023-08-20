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
            Label(zak, text=lg('Keyword')).grid(row=0, column=0, sticky='e')
            Label(zak, text=lg('Type')).grid(row=1, column=0, sticky='e')
            self.keyword_ = StringVar()
            type__ = [lg('General'), lg('Match_casse')]
            self.keyword = ttk.Entry(zak, textvariable=self.keyword_, width=50)
            self.type_ = ttk.Combobox(zak, values=type__)
            self.keyword.grid(row=0, column=1, sticky='w')
            self.type_.grid(row=1, column=1, sticky='w')
            self.type_.current(0)
            Button(zak, text=lg('Search'), command=self._search).grid(row=0, column=2, sticky='e')
            Button(zak, text=lg('Close'), command=zak.destroy).grid(row=1, column=2, sticky='e')

    def _search(self):
        text = self.text.get('0.0', END)
        mc = self.keyword.get()
        lon = len(mc)
        r = []
        for i in range(len(list(text))-lon):
            if self.type_.get() == lg('General'):
                if str(text[i:i+lon]).lower() == mc.lower():r.append(i)
            else:
                if text[i:i+lon] == mc:r.append(i)
        showinfo(self.title, str(len(r)) + ' ' + lg('results found'))
        self.dialoging = False

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
    from main import *
    RunTestMacro(inst='search')
