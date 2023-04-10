#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

class Images:
    def __images__(self):
        self.images = {'new' : PhotoImage(file = self.path_prog + '/image/plus.png'),
                       'open' : PhotoImage(file = self.path_prog + '/image/open.png'),
                       'save' : PhotoImage(file = self.path_prog + '/image/save.png'),
                       'saveas' : PhotoImage(file = self.path_prog + '/image/saveas.png'),
                       'savecopyas' : PhotoImage(file = self.path_prog + '/image/savecopyas.png'),
                       'settings' : PhotoImage(file = self.path_prog + '/image/config.png'),
                       'print': PhotoImage(file = self.path_prog + '/image/printer.png'),
                       'close': PhotoImage(file = self.path_prog + '/image/close.png'),
                       'exit': PhotoImage(file = self.path_prog + '/image/fermer.png'),

                       'undo': PhotoImage(file = self.path_prog + '/image/undo.png'),
                       'redo': PhotoImage(file = self.path_prog + '/image/redo.png'),
                       'cut': PhotoImage(file = self.path_prog + '/image/cut.png'),
                       'copy': PhotoImage(file = self.path_prog + '/image/copy.png'),
                       'past': PhotoImage(file = self.path_prog + '/image/past.png'),
                       'gotol': PhotoImage(file = self.path_prog + '/image/gotol.png'),
                       'select': PhotoImage(file = self.path_prog + '/image/selectall.png'),
                       'search' : PhotoImage(file = self.path_prog + '/image/find.png'),
                       'replace': PhotoImage(file = self.path_prog + '/image/replace.png'),

                       'infobar': PhotoImage(file = ''),#self.path_prog + '/'),
                       'ruban': PhotoImage(file = ''),#self.path_prog + '/'),
                       'buttonbar': PhotoImage(file = ''),#self.path_prog + '/'),
                       
                       'puces': PhotoImage(file = self.path_prog + '/image/puces.png'),
                       'news': PhotoImage(file = self.path_prog + '/image/style.png'),
                       'cstyle': PhotoImage(file = self.path_prog + '/image/cstyle.png'),
                       
                       'comment': PhotoImage(file = self.path_prog + '/image/comment.png'),
                       'uncomment': PhotoImage(file = ''),#self.path_prog + '/'),

                       'solve': PhotoImage(file = self.path_prog + '/image/solve.png'),
                       'compile': PhotoImage(file = self.path_prog + '/image/compile.png'),
                       'check': PhotoImage(file = self.path_prog + '/image/check.png'),
                       'run': PhotoImage(file = self.path_prog + '/image/run.png'),

                       'word': PhotoImage(file = self.path_prog + '/image/word.png'),
                       'pdf': PhotoImage(file = self.path_prog + '/image/pdf.png'),

                       'key': PhotoImage(file = self.path_prog + '/image/password.png'),
                       
                       'archive' : PhotoImage(file = self.path_prog + '/image/zip.png'),
                       'append': PhotoImage(file = self.path_prog + '/image/plus.png'),
                       'compare': PhotoImage(file = self.path_prog + '/image/compare.png'),

                       'send': PhotoImage(file = self.path_prog + '/image/send.png'),
                       'clear': PhotoImage(file = self.path_prog + '/image/clear.png'),
                       'bip': PhotoImage(file = self.path_prog + '/image/bip.png'),
                       'ulla': PhotoImage(file = ''),#self.path_prog + '/'),

                       'update': PhotoImage(file = ''),#self.path_prog + '/'),
                       'upgrade': PhotoImage(file = ''),#self.path_prog + '/'),

                       'load': PhotoImage(file = self.path_prog + '/image/load.png'),

                       'ihm': PhotoImage(file = self.path_prog + '/image/config.png'),
                       'lnb': PhotoImage(file = self.path_prog + '/image/line.png'),
                       'dark': PhotoImage(file = self.path_prog + '/image/dark.png'),
                       'visut': PhotoImage(file = self.path_prog + '/image/task.png'),
                       'lgv': PhotoImage(file = self.path_prog + '/image/lg.png'),

                       'about': PhotoImage(file = self.path_prog + '/image/help.png'),
                       'doc': PhotoImage(file = self.path_prog + '/image/doc.png'),
                       'todo': PhotoImage(file = self.path_prog + '/image/todo.png'),
                       'lines': PhotoImage(file = self.path_prog + '/image/line.png'),
                       'struct': PhotoImage(file = self.path_prog + '/image/tree.png'),
                       'prog': PhotoImage(file = self.path_prog + '/image/prog.png'),
                       }
        self.size_images = (15, 15)

if __name__ == '__main__':
    from __init__ import *
