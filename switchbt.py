from tkinter import *
from confr import *
import os

PATH_PROG = '.'#os.path.abspath(os.getcwd())

IMGS = (PATH_PROG + '/image/48x48/on.png',
        PATH_PROG + '/image/48x48/off.png')

bg_type = get_dark()
if bg_type:
    BG = get_bgd()
    FG = get_fgd()
else:
    BG = get_bgl()
    FG = get_fgl()

class Switch:
    def __init__(self, parent, stat = 'normal', command = lambda: None, bg = BG):
        self.on = PhotoImage(master = parent, file = IMGS[0])
        self.off = PhotoImage(master = parent, file = IMGS[1])
        self.stat = stat
        self.command = command
        self.bg = bg

        if stat in ('normal', True, '1'):
            self.stat = True
            img = self.on
        else:
            self.stat = False
            img = self.off

        if self.bg:
            self.w = Label(parent, image = img, bg = self.bg)
        else:
            self.w = Label(parent, image = img)

        self.w.bind('<Button-1>', self.switch)

    def place(self, *args, **kwarg):
        self.w.place(*args, **kwarg)
    
    def grid(self, *args, **kwarg):
        self.w.grid(*args, **kwarg)
    
    def pack(self, *args, **kwarg):
        self.w.pack(*args, **kwarg)

    def config(self, command = lambda: None):
        self.command = command

    def switch(self, evt = None, aloadcmd = True):
        self.stat = not self.stat
        self.update()
        if aloadcmd:
            self.command()

    def get(self):
        return self.stat

    def set(self, stat, aloadcmd = True):
        self.stat = stat
        self.update()
        if aloadcmd:
            self.command()

    def update(self):
        if self.stat:
            img = self.on
        else:
            img = self.off

        self.w.config(image = img)
