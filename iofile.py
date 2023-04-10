#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from confr import *
from threading import Thread
import time
import zipfile
import sys

from ext_form import *
from ext_file import *

class Auto_Save(Thread):
    def __init__(self, main_self):
        Thread.__init__(self)
        self.intertime = int(get_inter_time())
        self.main_self = main_self
        
    def run(self):
        self.main_self.add_task(code='AutoSave', time=time.time(), desc='MAIN_LOOP\nThis task is running to save your work at a frequency. You can set it on the configuration page (Option -> Options -> Autosave -> Frequency). You can\'t stop it.')
        while True:
            if self.main_self.programme_termine:
                break
            time.sleep(self.intertime)
            if not not(self.main_self.savedd) and not(self.main_self.saved):
                self.main_self.save()
            else:
                f = open(self.main_self.path_prog + '/' + get_autosave_path(), 'w', encoding='UTF-8')
                f.write(self.main_self.text.get('0.0', END))
                f.close()


class File(ExForm, ExText):
    def __file__(self):
        self.path = 'untitled.x'
        self.saved = False
        self.savedd = False
        self.ast = Auto_Save(self)

        self.listext = ['.txt', '.log', '.py', '.pyw', '.html', '.htm', '.php', '.ino', '.h', '.c', '.cpp', '.cc', '.bat', '.bas', '.ba', '.bf', '.f', '.f90', '.f95', '.eq', '.ini', '.inf']
        self.listexta = ['.zip', '.PADS', '.form', '.dat', '.exe', '.7z', '.tar', '.gz', '.sqlite', '.mysql']
        self.ttext = [(lg('Formf'), '*.form'),
                      (lg('alf'), '*.*'),
                      (lg('TF'), '*.txt *.log *.dat'),
                      (lg('dbf'), '*.db *.sqlite *.mysql *.xml *.json'),
                      (lg('zipf'), '*.zip *.tar *.gz *.exe *.7z'),
                      (lg('exef'), '*.exe'),
                      (lg('HF'), '*.html *.htm *.php'),
                      (lg('AF'), '*.ino *.h *.c *.cpp'),
                      (lg('CF'), '*.cpp *.c *.h *.cc'),
                      (lg('PF'), '*.py *.pyw'),
                      (lg('BF'), '*.bat'),
                      (lg('BAF'), '*.bas *.ba'),
                      (lg('FF'), '*.f *.f90 *.f95'),
                      (lg('BRF'), '*.bf'),
                      (lg('EF'), '*.eq'),
                      (lg('WF'), '*.docx *.doc'),
                      (lg('BU'), '*.bu'),
                      (lg('sysf'), '*.PADS'),
                      (lg('if'), '*.ini *.inf'),
                      (lg('floppyf'), '*.floppy'),
                      ]
        self.meta = {}
# Bonjour et bienvenue dans cette petite information à propos de l'Editor.
# Vous utilisez actuellement la version 0.32.
# Bonne utilisation !!!

    def open_recent(self, name):
        self.open(evt = None, name = name)

    def open_this(self, args):
        if len(args) > 1:
            self.open(evt = None, name = args[1])

    def ext(self, name):
        if '.' not in name:
            return ''

        i = len(name) - 1
        while name[i] != '.':i -= 1
        return name[i:]

    def askopen(self):
        return askopenfilename(title=lg('Open'), initialdir='.', filetypes=self.ttext)

    def asksaveas(self):
        return asksaveasfilename(title=lg('Save_as'), initialdir='.', filetypes=self.ttext)
        
    def open(self, evt=None, name = None):
        if not self.dialoging:
            self.dialoging = True
            if not name:
                name = self.askopen()

            if name:
                try:
                    self.menufichier.entryconfig(lg('settings'), stat = 'disabled')
                    self.stat_text(True)
                    self.clear_text()
                    if self.ext(name) in self.listext:
                        ExText.open(self, name)

                    elif self.ext(name) in self.listexta:
                        ExForm.open(self, name)

                    self.saved = True
                    self.savedd = True
                    self.path = name
                    self.add_f(self.path)
                    self.dialoging = True
                    self.autocolorwords()
                    self.master.title(self.title + ' - ' + self.path)
                    self.update_line_numbers(fforbid = True)
                    self.dialoging = False

                except FileNotFoundError:
                    self.saved = False
                    self.path = 'untitled.x'
                    showerror(self.title, lg('FNF'))
            self.dialoging = False

    def save(self, evt=None):
        if not self.dialoging:
            if not self.savedd:
                self.saveas()
            elif not self.saved:
                if self.ext(self.path) not in self.listexta:
                    ExText.save(self, self.path, self.get_text())
                else:
                    ExForm.save(self, self.path, self.get_text(), self.meta)
                self.saved = True
                self.master.title(self.title + ' - ' + self.path)
                
    def saveas(self, evt=None, name = None):
        if not self.dialoging:
            self.dialoging = True
            if not name:
                name = self.asksaveas()
                if '.' not in name:
                    name += '.form'

            if name:
                self.path = name
                if self.ext(self.path) not in self.listexta:
                    ExText.save(self, self.path, self.get_text())
                else:
                    ExForm.save(self, self.path, self.get_text(), self.meta)
                self.saved = True
                self.savedd = True
                self.add_f(self.path)
            else:
                self.saved = False
                self.savedd = False
                self.path = 'untitled.x'
            self.master.title(self.title + ' - ' + self.path)
            self.dialoging = False
            
    def savecopyas(self, evt=None):
        if not self.dialoging:
            self.dialoging = True
            name = asksaveasfilename(title=lg('Save_copy_as'), initialdir='.', filetypes=self.ttext)
            if name:
                if self.ext(self.path) not in self.listexta:
                    ExText.save(self, self.path, self.get_text(), False)
                else:
                    ExForm.save(self, self.path, self.get_text(), False)
            self.dialoging = False
            
    def new(self, evt=None):
        if not self.dialoging:
            self.stat_text(True)
            self.saved = False
            self.savedd = False
            self.path = 'Untitled.x'
            self.text.delete('0.0', END)
            self.master.title(self.title + ' - ' + self.path)
            self.update_line_numbers()

if __name__ == '__main__':
    from __init__ import *
