#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
from iomenu import *

class ClkRight:
    def __clk__(self):
        self.text.bind('<Button-3>', self.ClkRight)
        
    def ClkRight(self, evt):
        popup = Menu(self.master, tearoff=0)
        for name, command, image, separator, search, puces in self.menu_clk_right:
            if separator:
                popup.add_separator()
            elif search:
                mre = Menu(popup, tearoff=0)
                popup.add_cascade(label=lg('Search'), menu=mre)
                mre.add_command(label=lg('Researchi'), command=self.internet_research)
            elif puces:
                popup.add_checkbutton(label=lg('Puces'), onvalue=1, offvalue=0, variable=self.puces)
            else:
                popup.add_command(label=lg(name), command=command, image = self.images[name if image == None else image], compound='left')

        popup.tk_popup(evt.x_root, evt.y_root)

if __name__ == '__main__':
    from __init__ import *
