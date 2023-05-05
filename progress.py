#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
import time
from threading import Thread

class Compute(Thread):
    def __init__(self, lencnt, trace):
        Thread.__init__(self)
        self.time = 0
        self.lst_rel = []
        self.t = time.time()
        self.breaker = False
        self.cnt = 0
        self.lcnt = lencnt
        self.tps_dep = time.time()
        self.elapsed = 0
        self.trace = trace

    def append(self):
        self.lst_rel.append(time.time() - self.t)
        self.t = time.time()
        self.cnt += 1

    def run(self):
        while not self.breaker:
            try:
                n = 0
                for i in self.lst_rel:
                    n += i
                n /= len(self.lst_rel)
                self.time = int((self.lcnt - self.cnt) * n)
                self.elapsed = int(time.time() - self.tps_dep)
                #self.trace()
            except ZeroDivisionError:
                self.time = 0
                self.elapsed = 0


class Progress:
    oldpos = 0

    def __init__(self, master, title, maximum, decimals = 0, offcolor='white', oncolor = 'green'):
        if master:
            self.zak = Toplevel(master)
            self.zak.transient(master)
        else:
            self.zak = Tk()

        self.zak.title(title)
        self.zak.iconbitmap('image/progress.ico')
        self.zak.protocol('WM_DELETE_WINDOW', self.Quitter)
        self.lcounter = maximum
        self.decs = decimals
        self.oncolor = oncolor
        self.offcolor = offcolor
        self.counter = 0
        self.title = title
        self.content()

    def content(self):
        self.canvas = Canvas(self.zak, width = 210, height = 30)
        self.canvas.place(x = 25, y = 25)
        self.pc = StringVar(master = self.zak)
        self.time_elapsed = StringVar(master = self.zak)
        self.time_stay = StringVar(master = self.zak)
        self.pc.set('0 %')
        self.time_elapsed.set(lg('tecc') + '0 s')
        self.time_stay.set(lg('tere') + '0 s')
        Label(self.zak, textvariable = self.pc).place(x = 235, y = 30)
        Label(self.zak, textvariable = self.time_elapsed).place(x = 30, y = 60)
        Label(self.zak, textvariable = self.time_stay).place(x = 30, y = 90)
        Button(self.zak, text = lg('Abord'), command=None, stat = 'disabled').place(x = 30, y = 120)
        Button(self.zak, text = lg('Stdbye'), command = None, stat = 'disabled').place(x = 150, y = 120)
        self.zak.geometry(str(290 + (self.decs * 5)) + 'x175')
        self.second = Compute(self.lcounter, self.trace)
        self.second.start()
        self.trace()

    def decimales(self, nb):
        a = nb / 2
        """for i in range(self.decs):
            a *= 10
        a = int(a)
        for i in range(self.decs):
            a /= 10"""
        return str(int(a)) + ' %'

    def trace(self, pos = oldpos, name = ''):
        self.canvas.delete('all')
        self.zak.title(self.title + ' ' + name)
        self.canvas.create_rectangle(5, 5, 205, 25, fill = self.offcolor)
        x = pos
        self.oldpos = pos
        self.canvas.create_rectangle(5, 5, x + 5, 25, fill = self.oncolor)
        self.pc.set(self.decimales(pos))
        self.second.append()
        self.time_elapsed.set(lg('tecc') + str(self.second.elapsed) + ' ' + lg('second'))
        self.time_stay.set(lg('tere') + str(self.second.time) + ' ' + lg('second'))
        self.zak.update()

    def step(self, *args):
        self.counter += 1
        self.trace((self.counter / self.lcounter) * 200, ' '.join(args))
        if self.counter == self.lcounter:
            self.second.breaker = True

    def Generate(self):
        self.zak.mainloop()

    def Quitter(self):
        self.second.breaker = True
        self.zak.destroy()
        return

if __name__ == '__main__':
    p = Progress(master = None, title = 'test1', maximum = 105, decimals = 2, oncolor = 'red')
    for i in range(105):
        p.step('blablabla', 'ablabla')
        #time.sleep(0.1)
    p.Generate()
