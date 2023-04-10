#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
import time, os, sys

from confr import *

class Win:
    def __win__(self):
        try:
            self.master = Tk()
        except TclError:
            os.system('cls' if sys.platform == 'Win32' else 'clear')
            print("##########################################################################################")
            print('##                                                                                      ##')
            print("## Problème de niveau 1 : Le système opérant ne propose pas d'environnement graphique ! ##")
            print("## Veuillez résoudre ce problème selon l'administrateur système !                       ##")
            print('##                                                                                      ##')
            print("##########################################################################################")
            input()
            return False

        self.master.title(self.title + ' - Untitled.x')
        self.master.protocol('WM_DELETE_WINDOW', self.Quitter)
        self.master.iconbitmap(self.ico['win'])
        self.lns = get_ln()
        self.dark = get_dark()
        self.dialoging = False
        self.add_task(code='ClosingAutoAsk', time=time.time(), desc='MAIN_LOOP\nThis short program ask to the user is he want to save his work before closing. If work is already saved, it does not ask anything')
        return True

    def fermer(self, evt = None):
        self.clear_text()
        self.stat_text(False)
        self.update_line_numbers()
        self.menufichier.entryconfig(lg('settings'), stat = 'disabled')
        self.master.title(self.title + ' - ' + lg('NFO'))
        
    def Quitter(self, evt=None):
        if self.saved == False or self.saved == None or get_askclose:
            dem = askyesnocancel(self.title, lg('DYWTS'))
            if dem == True:
                self.save()
                self.master.destroy()
                self.close()
                self.programme_termine = True
                # raise KeyboardInterrupt
                # exit(code='ClosedByUserWithSave')

            elif dem == False:
                self.master.destroy()
                self.close()
                self.programme_termine = True
                # raise KeyboardInterrupt
                # exit(code='ClosedByUserWithoutSave')

        else:
            self.master.destroy()
            self.close()
            # raise KeyboardInterrupt
            # exit(code='ClosedByUserWithAutoSave')
        
    def Generate(self):
        self.master.mainloop()

if __name__ == '__main__':
    from __init__ import *
