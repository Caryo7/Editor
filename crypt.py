#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *
import random
from tkinter.messagebox import *
from exor import *

class Cesar:
    @classmethod
    def encrypt(self, data):
        t = ''
        l = len(str(self.key)) + 2
        for i in list(data):
            t += '0'*(l-len(str(ord(i) * self.key))) + str(ord(i) * self.key)
        return t
    
    @classmethod
    def decrypt(self, data):
        t = []
        r = ''
        l = len(str(self.key)) + 2
        for i in range(int(len(data)/l)):
            t.append(int(data[i*l:(i+1)*l]))

        for i in t:
            r += chr(int(i/self.key))
        return r


class Crypt:
    def __crypt__(self):
        self.key = get_key()
        if self.key == 1:
            self.generate_key()
        
    def encrypt(self, data):
        if self.iscrypt_cesar.get():
            return Cesar.encrypt(data)
        else:
            return ''

    def decrypt(self, data):
        if self.iscrypt_cesar.get():
            return Cesar.decrypt(data)
        else:
            return ''

    #def decrypt(self, data):
        #pass
    
    def generate_key(self):
        if self.mode_record:
            self.events.append({'command': 'key'})

        if askyesno(self.title, lg('YAGTCK')):
            write_key(random.randint(10 ** (random.randint(1, 2)), 10 ** (random.randint(2, 6))))
            self.key = get_key()
            while self.key == 1:
                self.generate_key()

    def cipher_file(self, name, key):
        if self.iscrypt_exor.get():
            e = ExOr()
            e.send(name, key)
            e.crypt()
        else:
            pass

    def uncipher_file(self, name, key):
        self.cipher_file(name, key)

if __name__ == '__main__':
    from __init__ import *
