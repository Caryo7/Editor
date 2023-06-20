#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
import time

class Python:
    modes = {'keyword':('orange', None), 'dem':('purple', None)}
    colors = {'keyword':['await', 'async', 'nonlocal', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'exec', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield', 'None'],
              'dem':['open', 'isinstance', 'range', 'len', 'str', 'int', 'bool', 'float', 'char', 'method', 'type', 'print', 'input', 'eval', 'list', 'set', 'bin', 'bytes', 'exit', 'quit', 'Exception'],
              }

class Cpp:
    modes = {'keyword':('yellow', None), 'stdout':('green', None)}
    colors = {'keyword':['void', 'int', 'char', 'float', 'long', 'double', 'byte', 'class', 'if', 'while', 'do', 'switch'],
              'stdout':['endl', 'cout', 'cin'],
              }

class Colors(Python):
    def get_colors(self):
        if get_deck() == 'Python':
            return Python.colors
        elif get_deck() == 'C++':
            return Cpp.colors
        else:
            return {}

    def get_mode(self):
        if get_deck() == 'Python':
            return Python.modes
        elif get_deck() == 'C++':
            return Cpp.modes
        else:
            return {}

class AutoColor(Colors):
    def __ac__(self):
        self.wordi = self.text.index('@0,0')
        self.add_task(code='AutoColor', time=time.time(), desc='MAIN_LOOP\nRead every word on the text and put colors in case of word is on the data base (Actually, it work on python keywords) Caution : Can\'t be unstart in this version !', fnct = 'autocolor')
        
    def tryword(self):
        if self.lst_fnct['autocolor']:
            return
        mode = None
        for key, value in self.get_colors().items():
            if self.word in value:
                mode = key
                break

        if mode:
            for i in range(len(self.word)):
                self.text.tag_add(mode, index1=self.wordi)
                self.wordi = self.text.index('{0}+1char'.format(self.wordi))
            self.text.tag_config(mode,
                                 foreground=self.get_mode()[mode][0] if self.get_mode()[mode][0] else (get_fgd() if self.dark else get_fgl()),
                                 background=self.get_mode()[mode][1] if self.get_mode()[mode][1] else (get_bgd() if self.dark else get_bgl()))

    def autocolorwords(self):
        if self.lst_fnct['autocolor']:
            return

        self.words = self.split(self.text.get('0.0', END))
        n = 0
        for self.word in self.words:
            self.wordi = self.text.index('@0,0+{0}char'.format(str(n)))
            self.tryword()
            n += len(self.word) + 1

if __name__ == '__main__':
    from __init__ import *


