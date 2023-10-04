#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import zipfile as zp

class Zip:
    def __init__(self, file):
        self.z = zp.ZipFile(file, 'r')

    def read(self, file):
        self.f = self.z.open(file)
        r = self.f.read()
        self.f.close()
        return r

    def update(self, texttoadd, code):
        for file in self.z.namelist():
            print(file)
            print(texttoadd)

            self.f = self.z.open(file, 'r')
            r = self.f.read().decode(code)
            self.f.close()

            r += texttoadd + '\n'

            self.f = self.z.open(file, 'w')
            self.f.write(r.encode(code))
            self.f.close()

class Lg(Zip):
    def __init__(self, langue = 'fr', code = 'utf-8', path_prog = '.'):
        Zip.__init__(self, path_prog + '/lang.lg')
        self.langue = langue
        self.code = code
        self.data = self.read(langue + '.lang').decode(self.code)
        self.data = self.data.replace('\r', '')
        data = self.data.split('\n')
        self.dic = {}
        for value in data:
            if value == '':
                continue

            if value[0] == '[':
                continue

            spl = value.split(' = ')
            self.dic[spl[0].lower()] = spl[1]

    def get(self):
        return self.dic

    def set(self, k, v):
        self.update(k + ' = ' + v, self.code)
        self.__init__()

if __name__ == '__main__':
    l = Lg('an', 'utf-8')
    print(l.get())
    #k = str(input('Nom option : '))
    #v = str(input('Valeur par défaut : '))
    #l.set(k, v)
