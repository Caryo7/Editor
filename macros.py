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
        ## La définition des modes se trouve dans main.py -> __init__

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

                        print(j)
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
        if self.recording:
            return

        self.events = []
        self.mode_record = True
        self.recording = True

    def switch_record(self):
        if self.recording:
            self.mode_record = not self.mode_record

    def finish_record(self):
        if not self.recording:
            return

        self.mode_record = False
        self.recording = False

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
            print(self.events)
            zak.destroy()
            f = open(e.get(), 'w')
            for event in self.events:
                for arg, value in event.items():
                    if arg == 'command':
                        f.write(value)
                        continue

                    if value == None:
                        continue

                    if isinstance(value, bool):
                        value = '1' if value else '0'
                    elif isinstance(value, int):
                        value = str(value)

                    f.write(' ' + str(arg) + ':' + str(value))
                f.write('\n')

            f.close()

        Button(zak, text = lg('...'), width = 3, command = ask).grid(row = 1, column = 1, padx = 5, sticky = 'w', pady = 5)
        Button(zak, text = lg('ok'), width = 20, command = ok).grid(row = 2, column = 0, padx = 5, pady = 10, columnspan = 2)


if __name__ == '__main__':
    from __init__ import *
