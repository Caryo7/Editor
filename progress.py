#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from confr import *
import time
from threading import Thread
import PyTaskbar

PATH_PROG = '.'#os.path.abspath(os.getcwd())

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


class ProgressTask:
    add = 1
    prog = 0

    def __init__(self, tb):
        self.tb = tb
        self.tb.setState("loading") # loading, normal, error, warning, done

    def step(self, first = False):
        if first:
            self.tb.setState("normal")
            self.prog += 1
            self.tb.setProgress(self.prog)
        else:
            self.prog += self.add
            self.prog = int(self.prog)
            self.tb.setProgress(self.prog)

    def stop(self):
        self.tb.setState("done")

    def reset(self):
        self.prog = 0
        self.tb.setProgress(0)

    def set(self, value, with_first = False):
        self.tb.setState("loading")
        if with_first:
            self.add = 99 / value
        else:
            self.add = 100 / value


class Waiter(Thread):
    pos = 0
    up = True
    on = True
    add = 1
    fpc = 0.0

    def __init__(self, master = None, tb = None, title = '', text = '', decimals = 0, autostart = True, double = False):
        Thread.__init__(self)
        if master:
            self.zak = Toplevel(master)
            self.zak.transient(master)
        else:
            self.zak = Tk()

        self.tb = tb
        if tb:
            self.ptb = ProgressTask(tb)

        self.zak.title(title)
        self.decimals = decimals
        self.title = title
        self.zak.resizable(False, False)
        self.zak.iconbitmap(PATH_PROG + '/image/icons/ProgressIcon.ico')
        self.zak.protocol('WM_DELETE_WINDOW', lambda : None)
        if double:
            self.zak.geometry('340x110')
        else:
            self.zak.geometry('340x80')

        Label(self.zak, text = text).place(x = 10, y = 10)
        self.pb = ttk.Progressbar(self.zak, orient = 'horizontal', mode = 'indeterminate', length = 280)
        self.pb.place(x = 10, y = 40)
        
        if double:
            self.prb = ttk.Progressbar(self.zak, orient = 'horizontal', mode = 'determinate', length = 280)
            self.prb.place(x = 10, y = 70)
            self.pc = StringVar(master = self.zak)
            self.update_numbers()
            Label(self.zak, textvariable = self.pc).place(x = 295, y = 70)

        self.zak.update()

        if autostart:
            self.start()

    def update_numbers(self):
        self.pc.set(str(self.arond(self.fpc)) + ' %')

    def arond(self, x):
        a = x
        for i in range(self.decimals):
            a *= 10
        a = int(a)
        for i in range(self.decimals):
            a /= 10
        return a

    def run(self):
        while self.on:
            try:
                if self.up:
                    self.pos += 1
                else:
                    self.pos -= 1
    
                if self.pos <= 0:
                    self.up = True
                elif self.pos >= 100:
                    self.up = False
    
                self.pb['value'] = self.pos
                self.zak.update()
                time.sleep(0.05)
            except:
                break

    def stop(self):
        self.on = False
        if self.tb:
            self.ptb.stop()
        self.zak.destroy()

    def set(self, maxi, with_first = True):
        if with_first:
            self.add = 99
        else:
            self.add = 100
        self.add /= maxi
        if self.tb:
            self.ptb.set(maxi, with_first)

    def step(self, text = '', first = False):
        try:
            if first:
                self.prb['value'] = 0.0
                self.prb['value'] += 1.0
                if self.tb:
                    self.ptb.step(first)
            else:
                self.prb['value'] += self.add
                self.fpc += self.add
                if self.tb:
                    self.ptb.step()
                self.update_numbers()
                if text != '':
                    self.zak.title(self.title + ' - ' + text)
                self.zak.update()
        except:
            pass


class Progress:
    add1 = 0
    add2 = 0
    fpc1 = 0.0
    fpc2 = 0.0

    def __init__(self, master = None, tb = None, title = '', decimals = 0, double = False, text = '', **args):
        if master:
            self.zak = Toplevel(master)
            self.zak.transient(master)
        else:
            self.zak = Tk()

        self.zak.title(title)
        self.double = double
        self.tb = tb
        if self.tb:
            self.ptb = ProgressTask(tb)

        self.decimals = decimals
        self.title = title
        self.zak.resizable(False, False)
        self.zak.iconbitmap(PATH_PROG + '/image/icons/ProgressIcon.ico')
        self.zak.protocol('WM_DELETE_WINDOW', lambda : None)
        Label(self.zak, text = text).place(x = 10, y = 10)
        self.add1 = 100 / 100
        self.pb1 = Progressbar(self.zak, orient = 'horizontal', mode = 'determinate', length = 280)
        self.pb1.place(x = 10, y = 40)
        self.pc1 = StringVar(master = self.zak)
        self.update_numbers()
        Label(self.zak, textvariable = self.pc1).place(x = 295, y = 40)
        if double:
            self.pb2 = Progressbar(self.zak, orient = 'horizontal', mode = 'determinate', length = 280)
            self.pb2.place(x = 10, y = 70)
            self.pc2 = StringVar(master = self.zak)
            self.update_numbers()
            Label(self.zak, textvariable = self.pc2).place(x = 295, y = 70)
            self.zak.geometry('340x110')
        else:
            self.zak.geometry('340x80')
        self.zak.update()

    def update_numbers(self):
        self.pc1.set(str(self.arond(self.fpc1)) + ' %')
        try:
            self.pc2.set(str(self.arond(self.fpc2)) + ' %')
        except AttributeError:
            pass

    def arond(self, x):
        a = x
        for i in range(self.decimals):
            a *= 10
        a = int(a)
        for i in range(self.decimals):
            a /= 10
        return a

    def set(self, value = 1, bar = 0, with_first = False):
        assert value > 0
        with_first = 99 if with_first else 100
        if bar == 0:
            if not self.double:
                if self.tb:
                    self.ptb.set(value, True if with_first == 99 else False)
            self.add1 = with_first / value
        elif bar == 1:
            if self.double:
                if self.tb:
                    self.ptb.set(value, True if with_first == 99 else False)
            self.add2 = with_first / value

    def step(self, text = '', bar = 0, first = False):
        if bar == 0:
            if not self.double:
                if self.tb:
                    self.ptb.step(first)
            self.pb1['value'] += self.add1
            self.fpc1 += self.add1
        elif bar == 1:
            if self.double:
                if self.tb:
                    self.ptb.step(first)
            self.pb2['value'] += self.add2
            self.fpc2 += self.add2

        if text != '':
            self.zak.title(self.title + ' - ' + text)
        self.update_numbers()
        self.zak.update()

    def reset(self, bar = 0):
        if bar == 0:
            self.pb1['value'] = 0
            self.fpc1 = 0.0
        elif bar == 1:
            self.pb2['value'] = 0
            self.fpc2 = 0.0
            
        self.update_numbers()
        self.zak.update()
        try:
            self.ptb.reset()
        except:
            pass

    def stop(self):
        if self.tb:
            self.ptb.stop()
        self.zak.destroy()


if __name__ == '__main__':
    while True:
        a = input('Progress/Waiter > [p/w] : ')
        if a == 'p':
            p = Progress(double = False)
            p.set(3)
            time.sleep(0.5)
            p.step('Bonjour')
            time.sleep(0.5)
            p.step('Hello')
            time.sleep(0.5)
            p.step('Allo')
            time.sleep(1)
            p.stop()

        elif a == 'w':
            w = Waiter(double = True)
            w.set(3, with_first = False)
            time.sleep(0.5)
            w.step(first = True)
            time.sleep(0.5)
            w.step('Bonjour')
            time.sleep(0.5)
            w.step('Hello')
            time.sleep(0.5)
            w.step('Allo')
            time.sleep(0.5)
            w.stop()

        else:
            print('Mauvais choix !')

