#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.ttk import *
from security import *
from confr import *
from pathlib import Path
import time, random, os

class Startup:
    def __init__(self):
        self.top = Tk()
        self.top.iconbitmap(PATH_PROG + '/image/icons/ico.ico')
        self.top.overrideredirect(1)
        self.width = 400
        self.height = 300
        self.top.geometry('+' + str(int((self.top.winfo_screenwidth()-self.width)/2)) + '+' + str(int((self.top.winfo_screenheight()-self.height)/2)))
        self.top.geometry(str(self.width) + 'x' + str(self.height))
        p = Path('')
        self.list = [('Verifing : ' + str(i), None) for i in list(p.glob('**/*'))]
        self.list += [('Reading : ' + str(i), None) for i in list(p.glob('**/*'))]
        self.list += [('Testing : ' + str(i), None) for i in list(p.glob('**/*.py'))]
        self.list += [('Importing : ' + str(i), None) for i in list(p.glob('**/*.py'))]
        self.list += [('Compiling : ' + str(i), None) for i in list(p.glob('**/*.py'))]
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
<<<<<<< Updated upstream
=======
        self.i = 0
        self.image = PhotoImage(master = self.top, file = PATH_PROG + '/image/icons/TarinoMark.png')

    def finish(self):
        time.sleep(2)
        self.pb['value'] = 100.0
        self.pc.set('100 %')
>>>>>>> Stashed changes
        self.top.update()
        self.stat = False
        self.go()

    def go(self):
        nb = len(self.list)
        i = 0
        for n, a in self.list:
            i += 1
            self.l.set(n + '...')
            self.pb['value'] = (i/nb)*100
            self.pc.set(str(int(self.pb['value']*10)/10) + ' %')
            self.motifs()
            self.top.update()
            if 'security.py' == n.replace('Compiling : ', '') and get_conn():
                t = conn(int(self.top.winfo_screenwidth() / 2), int((self.top.winfo_screenheight() / 2) + (self.height / 2)))
            else:
                time.sleep(random.randint(0, 10) / 250)

        try:
            t.active(self.top)
        except UnboundLocalError:
            self.top.destroy()

    def motifs(self):
        self.canvas.delete('all')
        self.list_line.append((random.randint(0, self.width-20), random.randint(0, self.height-65), random.randint(0, self.width-20), random.randint(0, self.height-65), self.colors[random.randint(0, len(self.colors)-1)]))
        for x1, y1, x2, y2, fill in self.list_line:
            self.canvas.create_line(x1, y1, x2, y2, fill=fill)
            
        self.canvas.create_text((self.width-20)/2, (self.height-65)/2, text='Editor', font=('Courier-New', 72), fill='#d9d9d9')

if __name__ == '__main__':
    from __init__ import *
