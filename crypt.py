#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *
import random
from tkinter.messagebox import *

class Crypt:
    def __crypt__(self):
        self.key = get_key()
        if self.key == 1:
            self.generate_key()
        
    def encrypt(self, data):
        t = ''
        l = len(str(self.key)) + 2
        for i in list(data):
            t += '0'*(l-len(str(ord(i) * self.key))) + str(ord(i) * self.key)
        return t
    
    def decrypt(self, data):
        t = []
        r = ''
        l = len(str(self.key)) + 2
        for i in range(int(len(data)/l)):
            t.append(int(data[i*l:(i+1)*l]))

        for i in t:
            r += chr(int(i/self.key))
        return r
    
    def generate_key(self):
        if askyesno(self.title, lg('YAGTCK')):
            write_key(random.randint(10 ** (random.randint(1, 2)), 10 ** (random.randint(2, 6))))
            self.key = get_key()
            while self.key == 1:
                self.generate_key()

if __name__ == '__main__':
    t = Crypt()
    t.__crypt__()
    print(t.encrypt('Hello world!\nHow are you ?'))
    print(t.decrypt(t.encrypt('Hello world!\nHow are you ?')))
    t.title = 'NotePad'
    t.generate_key()

if __name__ == '__main__':
    from __init__ import *
