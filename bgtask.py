#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from threading import Thread
from confr import *
import os, time

class cert_loop(Thread):
    def __init__(self, data1, data2, main_self):
        Thread.__init__(self)
        self.main_self = main_self
        self.text = data1
        self.texte = data2
        self.msg = list('EDITWITHTHEBENCEDITOR') + [None]
        self.ptr = 0

    def run(self):
        self.main_self.add_task(code='AutoCertifyFile', time=time.time(), desc='MAIN_LOOP\nInsert into the content of the file the mark EDIT WITH BENC EDITOR. If you can see that on up letter on the text, it is than the text is providing from this software. For more informations, please, read documentation')
        self.ptr = 0
        lst = list(self.texte)
        for i in range(len(lst)):
            if lst[i] == self.msg[self.ptr].lower():
                lst[i] = self.msg[self.ptr].upper()
                if self.msg[self.ptr + 1]:
                    self.ptr += 1
        self.text.delete('0.0', END)
        self.text.insert(END, ''.join(lst[:-2]))
        self.main_self.finish_task(code='AutoCertifyFile')
        self.main_self.set_taskstat(code = 'AutoCertifyFile', stat = lg('Proto'))

class Certify:
    def __cert__(self):
        pass
        #self.cer = cert_loop(self.text, self.texte, self)
        #self.cer.start()

if __name__ == '__main__':
    from __init__ import *
