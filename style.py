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
        self.item = (0,)
        self.m = 0

    def new_tag(self, bg, fg, name, i, r, save=True, menu=True, replace = False):
        if save:
            self.lst_tags.append((name, bg, fg, i, r))
        elif replace:
            for j in range(len(self.lst_tags)):
                if self.lst_tags[j][0] == name:
                    self.lst_tags[j] = (name, bg, fg, self.lst_tags[j][3], self.lst_tags[j][4])

        if menu:
            try:
                if name not in self.menu_styles:
                    self.menu_styles.append(name)
                    self.mls.add_command(label=name, background=bg, foreground=fg, stat='disabled')

            except AttributeError:
                pass

        if not replace:
            while i != r:
                self.text.tag_add(name, index1=i)
                i = self.text.index('{0}+1char'.format(i))

            if bg != '':
                self.text.tag_config(name, background=bg)
            if fg != '':
                self.text.tag_config(name, foreground=fg)

            self.unsave(evt = None, forcing = True)
        else:
            self.write_tags()
            self.lst.itemconfig(self.item, background = self.lst_tags[self.m][1], foreground = self.lst_tags[self.m][2])
            self.unsave(evt = None, forcing = True)
            self.item = (0,)
            self.m = 0

    def selected_tag(self, evt):
        p = self.lst.curselection()[0]
        old_n = self.lst_tags[0][0]
        n = 0
        m = 0
        while p != n:
            if self.lst_tags[n][0] != old_n:
                n += 1
            else:
                m += 1

            old_n = self.lst_tags[m][0]

        self.new_tag(bg=self.lst_tags[m][1], fg=self.lst_tags[m][2], name=self.lst_tags[m][0], i=self.deb_tag, r=self.fin_tag, save=True, menu=False)
        self.zak.destroy()

    def add_tag_here(self):
        try:
            self.deb_tag = self.text.index('sel.first')
            self.fin_tag = self.text.index('sel.last')
            self.zak = Toplevel()
            self.zak.iconbitmap(self.ico['style'])
            self.zak.transient(self.master)
            self.zak.title(lg('Style'))
            self.lst = Listbox(self.zak)
            self.lst.grid()
            for i in self.lst_tags:
                if i[0] != '':
                    self.lst.insert(END, i[0])
                    self.lst.itemconfig(END, background=i[1], foreground=i[2])
            self.lst.bind('<Double-Button-1>', self.selected_tag)
            b = ttk.Button(self.zak, text = lg('New'), command = self.ask_new_tag).grid()

        except TclError:
            showerror(self.title, lg('VDSUT'))
<<<<<<< Updated upstream

    def write_tags(self):
=======
            self.dialoging = False

    def clear_tags(self):
        self.mls.delete(0, END)
        for name, _, _, _, _ in self.lst_tags:
            self.text.tag_delete(name)

    def write_tags(self):
        self.clear_tags()
>>>>>>> Stashed changes
        for i in self.lst_tags:
            if i[0] != '':
                self.new_tag(i[1], i[2], i[0], i[3], i[4], False)

<<<<<<< Updated upstream
=======
    def config_tags(self):
        if self.dialoging:
            return

        self.dialoging = True
        self.zak1 = Toplevel(self.master)
        self.zak1.iconbitmap(self.ico['style'])
        self.zak1.protocol('WM_DELETE_WINDOW', lambda : self.protocol_dialog(self.zak1))
        self.zak1.transient(self.master)
        self.zak1.title(lg('Style'))
        self.lst = Listbox(self.zak1)
        self.lst.grid()
        lst = []
        for i in self.lst_tags:
            if i[0] not in lst:
                if i[0] != '':
                    self.lst.insert(END, i[0])
                    self.lst.itemconfig(END, background=i[1], foreground=i[2])
                    lst.append(i[0])

        def modifier(self, evt):
            item = self.lst.curselection()
            p = item[0]
            old_n = self.lst_tags[0][0]
            n = 0
            m = 0
            while p != n:
                if self.lst_tags[n][0] != old_n:
                    n += 1
                else:
                    m += 1
                old_n = self.lst_tags[m][0]

            self.item = p
            self.m = m
            self.ask_new_tag(mode_pre = True, values = list(self.lst_tags[self.m]), forcing = True)

        def supprimer(self, evt):
            item = self.lst.curselection()[0]
            self.lst.delete(item)
            nom = self.lst_tags[item][0]
            self.clear_tags()
            n = 0
            for i in range(len(self.lst_tags)):
                if self.lst_tags[n][0] == nom:
                    self.lst_tags.pop(n)
                else:
                    n += 1

            self.write_tags()
            self.unsave(evt = None, forcing = True)

        def config_item(self, evt):
            popup = Menu(self.zak1, tearoff=0)
            popup.add_command(label = 'modifier', command=lambda : modifier(self, evt))
            popup.add_command(label = 'delete', command=lambda : supprimer(self, evt))
            popup.tk_popup(evt.x_root, evt.y_root)

        self.lst.bind('<Button-3>', lambda evt: config_item(self, evt))

>>>>>>> Stashed changes
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

    def ask_new_tag(self, values = [None, None, None], mode_pre = False, forcing = False):
        try:
            self.zak.destroy()
        except TclError:
            pass
        except AttributeError:
            pass

<<<<<<< Updated upstream
        try:
            self.i, self.r = self.text.index('sel.first'), self.text.index('sel.last')
            self.zak = Toplevel()
=======
        if self.dialoging and not forcing:
            return

        self.dialoging = True

        try:
            if not mode_pre:
                self.i, self.r = self.text.index('sel.first'), self.text.index('sel.last')

            self.zak = Toplevel(self.master)
>>>>>>> Stashed changes
            self.zak.iconbitmap(self.ico['style'])
            self.zak.transient(self.master)
            self.zak.title(lg('Style'))
            Label(self.zak, text=lg('Name')).grid(row=0, column=0, sticky='e')
            Label(self.zak, text=lg('Background')).grid(row=1, column=0, sticky='e')
            Label(self.zak, text=lg('Foreground')).grid(row=2, column=0, sticky='e')
<<<<<<< Updated upstream
            self.name_ = StringVar()
=======
            self.name_ = StringVar(master = self.master)
            self.name_.set(values[0] if values[0] else '')
>>>>>>> Stashed changes
            name = ttk.Entry(self.zak, textvariable=self.name_, width=32).grid(row=0, column=1, sticky='w')
            self.bg = ttk.Combobox(self.zak, values=self.colors_name + [lg('normal')])
            self.bg.grid(row=1, column=1, sticky='w')
            self.bg.set(lg(values[1]) if values[1] else lg('normal'))
            self.fg = ttk.Combobox(self.zak, values=self.colors_name + [lg('normal')])
            self.fg.grid(row=2, column=1, sticky='w')
            self.fg.set(lg(values[2]) if values[2] else lg('normal'))
            Button(self.zak, text=lg('ok'), command=lambda : self.nt(mode_pre)).grid(row=3, column=1, sticky = 'w')

        except TclError:
            showerror(self.title, lg('VDSUT'))

    def nt(self, mode_pre):
        self.new_tag(self.colors[self.bg.get()] if self.bg.get() != lg('normal') else '',
                     self.colors[self.fg.get()] if self.fg.get() != lg('normal') else '',
                     self.name_.get(),
                     self.i if not mode_pre else '@0.0',
                     self.r if not mode_pre else '@0.0',
                     replace = mode_pre,
                     save = not mode_pre)

        self.zak.destroy()

if __name__ == '__main__':
    from __init__ import *
