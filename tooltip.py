#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.font as tkFont

class ToolTip(object):
    id = None
    tw = None

    def __init__(self, widget, text='', color = '#FFFFEA', waittime = 500, wraplength = 270, relief = 'solid', borderwidth = 1, justify = 'left'):
        self.relief = relief
        self.borderwidth = borderwidth
        self.justify = justify
        self.color = color
        self.widget = widget
        self.text = text
        self.waittime = waittime
        self.wraplength = wraplength
        self.ln = self.text.split('\n')
        self.mode_dbl = True if len(self.ln) >= 2 else False

        #w_f = tkFont.Font(font=self.widget['font'])
        #font = w_f.actual()
        font = {'family': 'Segoe UI', 'size': 9}

        self.font_text = (font['family'], font['size'])
        self.font_title = (font['family'], font['size'], 'bold')

        if self.mode_dbl:
            self.title = self.ln[0]
            self.ln.pop(0)
            self.text = '\n'.join(self.ln)

        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        f = Frame(self.tw, relief = self.relief, background = self.color, borderwidth = self.borderwidth)
        f.pack(ipadx=1)

        if self.mode_dbl:
            ttl = Label(f,
                        text = self.title,
                        justify = self.justify,
                        background = self.color,
                        relief = None,
                        font = self.font_title,
                        wraplength = self.wraplength)

            ttl.grid(padx = 1)

        label = Label(f,
                      text = self.text,
                      justify = self.justify,
                      background = self.color,
                      relief = None,
                      font = self.font_text,
                      wraplength = self.wraplength)

        label.grid(padx = 1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

class CallTip:
    id = None
    endworld = (' ', ',', '\n', '\r', '\t', '/', '!', "'", '"')
    tw = None

    def __init__(self, widget, text = 'widget prefixe auto completition', color = '#FFFFEA', waittime = 500, wraplength = 180, relief = 'solid', borderwidth = 1, justify = 'left'):
        self.relief = relief
        self.borderwidth = borderwidth
        self.justify = justify
        self.color = color
        self.widget = widget
        self.text = text
        self.waittime = waittime
        self.wraplength = wraplength
        self.space = True
        self.widget.bind('<KeyRelease>', self.check_key)
        self.mots = []
        self.mot_en_cours = ''

    def check_key(self, evt):
        if evt.char == ' ':
            self.leave()
        else:
            self.showtip()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        try:
            self.lst.delete('0', 'end')
        except Exception:
            x = y = 0
            x, y, cx, cy = self.widget.bbox("insert")
            x += self.widget.winfo_rootx() + 25
            y += self.widget.winfo_rooty() + 20
            self.tw = Toplevel(self.widget)
            self.tw.wm_attributes('-topmost', 1)
            self.tw.wm_overrideredirect(True)
            self.tw.wm_geometry("+%d+%d" % (x, y))
            scroll = Scrollbar(self.tw)
            scroll.pack(side = RIGHT, fill = BOTH)
            self.lst = Listbox(self.tw, background = self.color, relief = self.relief, borderwidth = self.borderwidth, width=20, yscrollcommand = scroll.set)
            scroll.config(command = self.lst.yview)
            self.lst.pack(ipadx = 1)
            self.lst.bind('<Return>', self.complete)
            self.lst.bind('<Double-Button-1>', self.complete)

        t = list(self.widget.get('0.0', 'end'))
        mot = self.widget.get('insert -1c wordstart', 'insert wordend')

        self.mots = self.widget.get('0.0', 'end').lower().split(' ')
        n = 0
        while True:
            try:
                m = self.mots[n]
                if self.mots.count(m) > 1:
                    self.mots.pop(n)
                else:
                    n += 1
            except IndexError:
                break

        n = 0
        mot = mot.replace('\n', '')
        self.mots.sort()
        for word in self.mots:
            word = word.replace('\n', '')
            if mot in word:
                self.lst.insert('end', word)
                n += 1

        if n == 1:
            self.leave()

        self.mot_en_cours = mot

    def complete(self, evt):
        text = self.lst.get(self.lst.curselection())
        ln = len(self.mot_en_cours)
        for i in range(len(text)):
            if i < ln:
                pass
            else:
                self.widget.insert('insert', text[i])

        self.leave()

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

if __name__ == '__main__':
    root = Tk()
    btn1 = Button(root, text="button 1", width = 20)
    btn1.pack(padx=10, pady=5)
    button1_ttp = ToolTip(btn1, \
    'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet,\n'
    'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
    'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam'
    'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.', color = '#FFFFEA')

    tt = Text(root, width = 20, height = 3)
    tt.pack(padx = 10, pady = 5)
    CallTip(tt)
    root.mainloop()

