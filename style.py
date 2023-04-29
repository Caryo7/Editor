#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from confr import *

class Styles:
    def __style__(self):
        self.lst_tags = []
        self.char_p = ''

    def new_tag(self, bg, fg, name, i, r, save=True, menu=True):
        if save:
            self.lst_tags.append((name, bg, fg, i, r))

        if menu:
            self.mls.add_command(label=name, background=bg, foreground=fg, stat='disabled')

        while i != r:
            self.text.tag_add(name, index1=i)
            i = self.text.index('{0}+1char'.format(i))
        self.text.tag_config(name, background=bg, foreground=fg)
        self.unsave(evt = None, forcing = True)

    def selected_tag(self, evt):
        n = self.lst.curselection()[0]
        while self.lst_tags[n] == ['']:
            n += 1
        self.new_tag(bg=self.lst_tags[n][1], fg=self.lst_tags[n][2], name=self.lst_tags[n][0], i=self.deb_tag, r=self.fin_tag, save=True, menu=False)
        self.zak.destroy()
        self.dialoging = False

    def add_tag_here(self):
        if self.dialoging:
            return

        self.dialoging = True
        try:
            self.deb_tag = self.text.index('sel.first')
            self.fin_tag = self.text.index('sel.last')
            self.zak = Tk()
            self.zak.protocol('WM_DELETE_WINDOW', lambda : self.protocol_dialog(self.zak))
            self.zak.iconbitmap(self.ico['style'])
            self.zak.transient()
            self.zak.title(lg('Style'))
            self.lst = Listbox(self.zak)
            self.lst.grid()
            lst = []
            for i in self.lst_tags:
                if i[0] not in lst:
                    if i[0] != '':
                        self.lst.insert(END, i[0])
                        self.lst.itemconfig(END, background=i[1], foreground=i[2])
                        lst.append(i[0])
            self.lst.bind('<Double-Button-1>', self.selected_tag)
            b = ttk.Button(self.zak, text = lg('New'), command = self.ask_new_tag).grid()
        except TclError:
            showerror(self.title, lg('VDSUT'))
            self.dialoging = False

    def clear_tags(self):
        for name, _, _, _, _ in self.lst_tags:
            self.text.tag_remove('@0.0', 'end')

    def write_tags(self):
        #self.clear_tags()
        for i in self.lst_tags:
            if i[0] != '':
                self.new_tag(i[1], i[2], i[0], i[3], i[4], False)

    def config_tags(self):
        if self.dialoging:
            return

        self.dialoging = True
        self.zak = Tk()
        self.zak.iconbitmap(self.ico['style'])
        self.zak.protocol('WM_DELETE_WINDOW', lambda : self.protocol_dialog(self.zak))
        self.zak.transient()
        self.zak.title(lg('Style'))
        self.lst = Listbox(self.zak)
        self.lst.grid()
        lst = []
        for i in self.lst_tags:
            if i[0] not in lst:
                if i[0] != '':
                    self.lst.insert(END, i[0])
                    self.lst.itemconfig(END, background=i[1], foreground=i[2])
                    lst.append(i[0])

        def config_item(evt):
            popup = Menu(zak, tearoff=0)
            popup.add_command(label = 'modifier', command=None)
            popup.add_command(label = 'delete', command=None)
            popup.tk_popup(evt.x_root, evt.y_root)

        self.lst.bind('<Button-3>', config_item)

    def key_press_test(self, evt):
        if evt.char == ' ' and self.char_p == '':
            self.char_p += ' '
        elif evt.char in self.listchar and self.char_p == '':
            pass
            #self.char_p += 
        elif evt.char in ('-', '_', '*', '$', '¤', '°') and self.char_p == ' ':
            self.char_p += '+'
            self.text_puce = evt.char
        elif evt.char == ' ' and self.char_p == ' +':
            self.char_p = ''
            self.puces.set(1)
        elif self.puces.get() == 0:
            self.char_p == ''

        if evt.keycode in (36, 13) and self.char_p == '': # 36 pour Linux, 13 pour Windows (Entrée)
            self.char_p += '36'
        elif evt.keycode in (22, 8) and self.char_p == '36': # 22 pour Linux, 8 pour Windows (BackSpace)
            self.char_p += '22'
        elif evt.keycode in (22, 8) and self.char_p == '3622': # (BackSpace)
            self.char_p += '22'
        elif evt.keycode in (22, 8) and self.char_p == '362222': # (BackSpace)
            self.puces.set(0)
            self.char_p = ''
            self.text_puce = '-'
        elif self.puces.get() == 1:
            self.char_p = ''

    def ask_new_tag(self):
        try:
            self.zak.destroy()
        except TclError:
            pass
        except AttributeError:
            pass

        if self.dialoging:
            return

        self.dialoging = True

        try:
            self.i, self.r = self.text.index('sel.first'), self.text.index('sel.last')
            self.zak = Tk()
            self.zak.iconbitmap(self.ico['style'])
            self.zak.transient()
            self.zak.protocol('WM_DELETE_WINDOW', lambda : self.protocol_dialog(self.zak))
            self.zak.title(lg('Style'))
            Label(self.zak, text=lg('Name')).grid(row=0, column=0, sticky='e')
            Label(self.zak, text=lg('Background')).grid(row=1, column=0, sticky='e')
            Label(self.zak, text=lg('Foreground')).grid(row=2, column=0, sticky='e')
            self.name_ = StringVar()
            name = ttk.Entry(self.zak, textvariable=self.name_, width=32).grid(row=0, column=1, sticky='w')
            self.bg = ttk.Combobox(self.zak, values=self.colors_name)
            self.bg.grid(row=1, column=1, sticky='w')
            self.fg = ttk.Combobox(self.zak, values=self.colors_name)
            self.fg.grid(row=2, column=1, sticky='w')
            Button(self.zak, text=lg('ok'), command=self.nt).grid(row=3, column=1, sticky = 'w')
        except TclError:
            showerror(self.title, lg('VDSUT'))
            self.dialoging = False

    def nt(self):
        self.new_tag(self.colors[self.bg.get()],
                     self.colors[self.fg.get()],
                     self.name_.get(),
                     self.i,
                     self.r)

        self.zak.destroy()
        self.dialoging = False

if __name__ == '__main__':
    from __init__ import *
