#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from confr import *

class Macro:
    def __macro__(self):
        self.inst = []
        self.events = []
        ## Les instructions possibles sont dans keyb.py -> self.actions

    def load_macro(self):
        n = askopenfilename(title=lg('open'), initialdir='.', filetypes=[(lg('mf'), '*.macro'), (lg('alf'), '*.*')])
        if n:
            try:
                f = open(n, 'r', encoding='UTF-8')
                ins = f.read().split('\n')
                f.close()
                self.inst = []
                for line in ins:
                    if not line:
                        continue

                    words = line.split(' ')
                    cmd = words[0]
                    words.pop(0)
                    self.inst.append({'command': cmd})
                    for j in words:
                        if not j:
                            continue

                        arg, value = j.split(':')
                        self.inst[-1][arg] = value

                self.run_macro()
            except FileNotFoundError:
                show(self.title, lg('FNF'))

    def run_macro(self):
        errors = []
        for inst in self.inst:
            info = self.actions[inst['command']]
            for arg, value in inst.items():
                try:
                    if arg == 'command':
                        continue

                    info[-1][arg]
                    if value == '0':
                        value = False
                    elif value == '1':
                        value = True

                    info[-1][arg] = value
                except KeyError:
                    errors.append('No keyword ' + arg)

            print('éxécution :', info[0], 'arguments :', info[-1])
            info[0](**info[-1])

        if errors:
            showerror(self.title, '\n'.join(errors))

        self.reset_tableactions()

    def record_macro(self):
        self.events = []
        self.mode_record = True

        #self.menumacro.entryconfig(3, state = 'normal')
        #self.menumacro.entryconfig(1, state = 'disabled')
        #self.menumacro.entryconfig(2, state = 'normal')

    def switch_record(self):
        self.mode_record = not self.mode_record

        #try:
        #self.menumacro.entryconfig(2,
        #                           image = self.images['play'] if not self.mode_record else self.images['pause'],
        #                           label = 'Reprendre' if not self.mode_record else 'Pause')
        #except:
            #pass

        #self.menumacro.entryconfig(3, state = 'disabled' if not self.mode_record else 'normal')

    def finish_record(self):
        self.mode_record = False
        #try:
        #self.menumacro.entryconfig(2, state = 'disabled')
        #except:
            #pass

        #self.menumacro.entryconfig(3, state = 'disabled')

        
        # demande ici les infos (fichier à enregistrer par exemple)
        zak = Toplevel(self.master)
        zak.transient(self.master)
        zak.title(lg('Macro'))
        zak.iconbitmap(self.ico['win'])
        zak.resizable(False, False)
        Label(zak, text = 'Enregistrer sous fichier :').grid(row = 0, column = 0, padx = 10, pady = 5, columnspan = 2)
        e = StringVar(master = zak)
        Entry(zak, textvariable = e, width = 20).grid(row = 1, column = 0, padx = 5, sticky = 'e', pady = 5)
        def ask():
            n = self.asksaveas(exts = [(lg('mf'), '*.macro'), (lg('alf'), '*.*')])
            if n:
                e.set(n)

        def ok():
            zak.destroy()

        Button(zak, text = lg('...'), width = 3, command = ask).grid(row = 1, column = 1, padx = 5, sticky = 'w', pady = 5)
        Button(zak, text = lg('ok'), width = 20, command = ok).grid(row = 2, column = 0, padx = 5, pady = 10, columnspan = 2)


if __name__ == '__main__':
    from __init__ import *
