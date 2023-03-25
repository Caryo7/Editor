#!/usr/bin/env python 3
# -*- coding: utf-8 -*-
from tkinter import *
from tree import *

class IOMenu:
    def get_fnct(self, name):
        if name == 'copy':
            return self.copy
        elif name == 'cut':
            return self.cut
        elif name == 'past':
            return self.past
        elif name == 'cstyle':
            return self.add_tag_here
        elif name == 'news':
            return self.ask_new_tag
        elif name == 'new':
            return self.new
        elif name == 'open':
            return self.open
        elif name == 'exit':
            return self.Quitter
        elif name == 'print':
            return self.print_window
        elif name == 'save':
            return self.save
        elif name == 'saveas':
            return self.saveas
        elif name == 'undo':
            return self.undo
        elif name == 'redo':
            return self.redo
        elif name == 'search':
            return self.search
        elif name == 'word':
            return self.export_word
        elif name == 'pdf':
            return self.export_pdf
        elif name == 'about':
            return self.About
        elif name == 'struct':
            return Tkin
        elif name == 'close':
            return self.fermer
        elif name == 'savecopyas':
            return self.savecopyas
        elif name == 'replace':
            return self.replace
        elif name == 'gotol':
            return self.gotol
        elif name == 'tasks':
            return self.show

    def __load_menus__(self):
        f = open(self.path_prog + '/menus.m', 'r')
        r = f.read()
        f.close()

        self.menu_clk_right = []
        self.menu_bts = []
        remp = ''
        for line in r.split('\n'):
            if line == '#clk':
                remp = 'clk'
                continue

            elif line == '#bts':
                remp = 'bts'
                continue

            if remp == 'clk' and line != '':
                line = line.split(',')
                name, image, separator, search, puces = line
                self.menu_clk_right.append((name,
                                            self.get_fnct(name),
                                            None if image == '' else image,
                                            True if separator == '1' else False,
                                            True if search == '1' else False,
                                            True if puces == '1' else False))
    
            elif remp == 'bts' and line != '':
                line = line.split(',')
                wid, name, separator = line
                widget = Button if wid == 'B' else Checkbutton if wid == 'C' else None
                fnct = self.get_fnct(name) if wid == 'B' else {'onvalue': 1, 'offvalue': 0, 'variable': self.puces} if wid == 'C' else None
                self.menu_bts.append((widget,
                                      name,
                                      fnct,
                                      False if separator == '0' else True))


if __name__ == '__main__':
    from __init__ import *
