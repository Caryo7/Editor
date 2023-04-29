#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from security import *
from confr import *
from pathlib import Path
import time, random, os

class Startup:
    nb = 0

    def __init__(self, title = 'Editor'):
        self.title = title
        self.top = Tk()
        self.top.overrideredirect(1)
        self.top.wm_attributes('-topmost', 1)
        self.width = 400
        self.height = 300
        self.top.geometry('+' + str(int((self.top.winfo_screenwidth()-self.width)/2)) + '+' + str(int((self.top.winfo_screenheight()-self.height)/2)))
        self.top.geometry(str(self.width) + 'x' + str(self.height))
        self.colors = ('red', 'green', 'black', 'blue', 'pink', 'yellow', 'orange', 'white', 'purple', 'cyan', 'magenta', 'brown', 'grey')
        self.l = StringVar()
        Label(self.top, textvariable=self.l).place(x=10, y=250)
        self.pb = Progressbar(self.top, mode='determinate', orient='horizontal', length=self.width-70, value=0)
        self.pb.place(x=10, y=self.height-30)
        self.pc = StringVar()
        Label(self.top, textvariable=self.pc).place(x=self.width-55, y=270)
        self.canvas = Canvas(self.top, width=self.width-20, height=self.height-65)
        self.canvas.place(x=10, y=10)
        self.list_line = []
        self.i = 0

    def finish(self):
        time.sleep(2)
        self.pb['value'] = 100.0
        self.pc.set('100 %')
        self.top.update()
        time.sleep(0.5)
        try:
            self.t.active(self.top)
        except AttributeError:
            self.top.destroy()

    def kill(self):
        self.top.destroy()

    def add(self, text):
        self.i += 1
        self.l.set(text)
        self.pb['value'] = (self.i / self.nb) * 100
        self.pc.set(str(int(self.pb['value'])) + ' %')
        self.canvas.delete('all')
        for i in range(int(600 / self.nb)):
            self.list_line.append((random.randint(0, self.width-20), random.randint(0, self.height-65), random.randint(0, self.width-20), random.randint(0, self.height-65), self.colors[random.randint(0, len(self.colors)-1)]))

        for x1, y1, x2, y2, fill in self.list_line:
            self.canvas.create_line(x1, y1, x2, y2, fill=fill)
            
        self.canvas.create_text((self.width-20)/2, (self.height-65)/2, text=self.title, font=('Courier-New', 72), fill=self.top['bg'])
        self.top.update()
        
        if 'security' in text and get_conn():
            self.t = conn(int(self.top.winfo_screenwidth() / 2), int((self.top.winfo_screenheight() / 2) + (self.height / 2)))


if __name__ == '__main__':
    from __init__ import *
