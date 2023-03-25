#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter.filedialog import *
from pathlib import Path
from threading import *
from confr import *
import urllib.request as url
import os, inspect, zipfile as zf, time

PATH_PROG = str(os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0])))

class Check(Thread):
    def __init__(self, main_self):
        Thread.__init__(self)
        self.main_self = main_self
        
    def run(self):
        self.main_self.add_task('CheckUpdate', time.time(), desc='MAIN_LOOP\nTo inform you when a new update is available, this task was built. It is reading every 10 min on the net if a new version is not available. If that is, a massage is showing to yourself to inform you the news device. You can\'t stop this task.', killable = False)
        while True:
            try:
                f = url.urlopen('https://bgtarino.wixsite.com/editor')
                r = f.read().decode()
                f.close()
                index = r.index('version ')
                n = index + 8
                while r[n] != ' ':
                    n += 1
                if float(r[index + 8: n]) > float(self.main_self.version):
                    print('Nouvelle version !!! :', r[index + 8: n])
                    self.main_self.ask_install(old = False)
    
                elif float(r[index + 8: n]) == float(self.main_self.version):
                    pass
    
                else:
                    print('Ancienne version sur le site !')
                    #self.main_self.ask_install(old = True)

            except Exception:
                pass

            time.sleep(60)


class Installer(Thread):
    def __init__(self, old):
        Thread.__init__(self)
        self.old = old

    def run(self):
        f = url.urlopen('https://bgtarino.wixsite.com/editor/t%C3%A9l%C3%A9chargement')
        r = f.read().decode()
        f.close()
        index = r.index('Télécharger le code source')
        m = index
        while r[m] != '<':
            m -= 1
        inst = r[m:index].split(' ')
        file = ''
        for balise in inst:
            if 'href' in balise:
                file = balise.replace('href="', '')
                file = file.replace('"', '')
                break

        f = url.urlopen(file)
        r = f.read()
        f.close()
        f = open(PATH_PROG + '/temp/last_update.zip', 'wb')
        f.write(r)
        f.close()
        if not self.old:
            z = zf.ZipFile(q, 'r')
            for file in z.namelist():
                fle = file.replace('Edit/', '')
                if '.' in fle:
                    try:
                        f = open(PATH_PROG + '/' + fle, 'rb')
                        l = len(f.read())
                        f.close()
                        if len(z.read(file)) != l:
                            f = open(PATH_PROG + '/' + fle, 'wb')
                            f.write(z.read(file))
                            f.close()

                    except FileNotFoundError:
                        f = open(PATH_PROG + '/' + fle, 'wb')
                        f.write(z.read(file))
                        f.close()
            z.close()


class Update:
    def __update__(self):
        self.path = ''
        t = Check(self)
        t.start()
        self.checkupdate = IntVar()
        self.checkupdate.set(get_update_test())

    def copy_file(self, pathi, patho):
        fi = open(pathi, 'rb')
        l = fi.read()
        fi.close()
        fo = open(patho, 'wb')
        fo.write(l)
        fo.close()
        
    def get_update(self):
        q = askopenfilename(title=lg('Selectdir'), initialdir='.', filetypes = [(lg('zipf'), '*.zip')])
        if q:
            z = zf.ZipFile(q, 'r')
            for file in z.namelist():
                fle = file.replace('Edit/', '')
                if '.' in fle:
                    try:
                        f = open(PATH_PROG + '/' + fle, 'rb')
                        l = len(f.read())
                        f.close()
                        if len(z.read(file)) != l:
                            f = open(PATH_PROG + '/' + fle, 'wb')
                            f.write(z.read(file))
                            f.close()

                    except FileNotFoundError:
                        f = open(PATH_PROG + '/' + fle, 'wb')
                        f.write(z.read(file))
                        f.close()
            z.close()

    def ask_install(self, old = False):
        if self.checkupdate.get():
            dem = askyesno(self.title, lg('nva'))
            if dem and self.checkupdate.get():
                th = Installer(old)
                th.start()

        
def htest():
    t = Tk()
    u = Update()
    u.get_update()
    t.destroy()

if __name__ == '__main__':
    from __init__ import *
