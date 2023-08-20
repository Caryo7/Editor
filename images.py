#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

class Images:
    def __images__(self):
        self.images = {'new' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/plus.png'),
                       'open' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/open.png'),
                       'save' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/save.png'),
                       'saveas' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/saveas.png'),
                       'savecopyas' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/savecopyas.png'),
                       'settings' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/config.png'),
                       'print': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/printer.png'),
                       'close': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/close.png'),
                       'exit': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/fermer.png'),

                       'undo': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/undo.png'),
                       'redo': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/redo.png'),
                       'cut': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/cut.png'),
                       'copy': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/copy.png'),
                       'past': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/past.png'),
                       'gotol': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/gotol.png'),
                       'select': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/selectall.png'),
                       'search' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/find.png'),
                       'replace': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/replace.png'),

                       'infobar': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       'ruban': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       'buttonbar': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       
                       'puces': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/puces.png'),
                       'news': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/style.png'),
                       'cstyle': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/cstyle.png'),

                       'lst_vars': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/todo.png'),
                       'add_var': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/plus.png'),
                       'place_var': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/cursor.png'),
                       
                       'comment': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/comment.png'),
                       'uncomment': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),

                       'run_python': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/python.png'),
                       'solve': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/solve.png'),
                       'compile': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/compile.png'),
                       'check': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/check.png'),
                       'run': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/run.png'),

                       'word': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/word.png'),
                       'pdf': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/pdf.png'),

                       'key': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/password.png'),
                       
                       'archive' : PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/zip.png'),
                       'append': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/plus.png'),
                       'compare': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/compare.png'),

                       'send': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/send.png'),
                       'clear': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/clear.png'),
                       'bip': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/bip.png'),
                       'ulla': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),

                       'update': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       'upgrade': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),

                       'load': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/load.png'),
                       'rec': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/load.png'),
                       'pause': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/load.png'),
                       'play': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/load.png'),
                       'carre': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/load.png'),

                       'ihm': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/config.png'),
                       'lnb': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/line.png'),
                       'dark': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/dark.png'),
                       'visut': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/task.png'),
                       'win': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/windows.png'),
                       'lgv': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/lg.png'),

                       'about': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/help.png'),
                       'doc': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/doc.png'),
                       'todo': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/todo.png'),
                       'lines': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/line.png'),
                       'struct': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/tree.png'),
                       'prog': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/prog.png'),
                       }
        self.size_images = (15, 15)

if __name__ == '__main__':
    from __init__ import *
