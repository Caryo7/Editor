#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread
import math, time

class Pi(Thread):
    def __init__(self, main_self):
        Thread.__init__(self)
        self.main_self = main_self

    def get(self):
        return self.pi

    def run(self):
        self.main_self.add_task(code='Surcharge', time=time.time(), desc='')
        piv = list(str(math.pi))
        self.pi  = 4
        i = 3
        oldn = 0
        t = time.time()
        while True:
            self.pi -= (4/i) - (4/(i+2))
            i += 4
            n = 0
            while list(str(self.pi))[n] == piv[n]:n += 1
            if n != oldn:oldn = n

class Surcharge:
    def __sur__(self):
        ""

    def start_sur(self):
        p = Pi(self)
        p.start()
    

def htest():
    t = Pi(self)
    t.start()
    print(t.get())
    time.sleep(12)
    print(t.get())

if __name__ == '__main__':
    htest()
