#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

class Images:
    def __images__(self):
        self.images = {'new' : PhotoImage(master = self.master, file = self.path_prog + '/image/plus.png'),
                       'open' : PhotoImage(master = self.master, file = self.path_prog + '/image/open.png'),
                       'save' : PhotoImage(master = self.master, file = self.path_prog + '/image/save.png'),
                       'saveas' : PhotoImage(master = self.master, file = self.path_prog + '/image/saveas.png'),
                       'savecopyas' : PhotoImage(master = self.master, file = self.path_prog + '/image/savecopyas.png'),
                       'settings' : PhotoImage(master = self.master, file = self.path_prog + '/image/config.png'),
                       'print': PhotoImage(master = self.master, file = self.path_prog + '/image/printer.png'),
                       'close': PhotoImage(master = self.master, file = self.path_prog + '/image/close.png'),
                       'exit': PhotoImage(master = self.master, file = self.path_prog + '/image/fermer.png'),

                       'undo': PhotoImage(master = self.master, file = self.path_prog + '/image/undo.png'),
                       'redo': PhotoImage(master = self.master, file = self.path_prog + '/image/redo.png'),
                       'cut': PhotoImage(master = self.master, file = self.path_prog + '/image/cut.png'),
                       'copy': PhotoImage(master = self.master, file = self.path_prog + '/image/copy.png'),
                       'past': PhotoImage(master = self.master, file = self.path_prog + '/image/past.png'),
                       'gotol': PhotoImage(master = self.master, file = self.path_prog + '/image/gotol.png'),
                       'select': PhotoImage(master = self.master, file = self.path_prog + '/image/selectall.png'),
                       'search' : PhotoImage(master = self.master, file = self.path_prog + '/image/find.png'),
                       'replace': PhotoImage(master = self.master, file = self.path_prog + '/image/replace.png'),

                       'infobar': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       'ruban': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       'buttonbar': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       
                       'puces': PhotoImage(master = self.master, file = self.path_prog + '/image/puces.png'),
                       'news': PhotoImage(master = self.master, file = self.path_prog + '/image/style.png'),
                       'cstyle': PhotoImage(master = self.master, file = self.path_prog + '/image/cstyle.png'),
                       
                       'comment': PhotoImage(master = self.master, file = self.path_prog + '/image/comment.png'),
                       'uncomment': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),

                       'solve': PhotoImage(master = self.master, file = self.path_prog + '/image/solve.png'),
                       'compile': PhotoImage(master = self.master, file = self.path_prog + '/image/compile.png'),
                       'check': PhotoImage(master = self.master, file = self.path_prog + '/image/check.png'),
                       'run': PhotoImage(master = self.master, file = self.path_prog + '/image/run.png'),

                       'word': PhotoImage(master = self.master, file = self.path_prog + '/image/word.png'),
                       'pdf': PhotoImage(master = self.master, file = self.path_prog + '/image/pdf.png'),

                       'key': PhotoImage(master = self.master, file = self.path_prog + '/image/password.png'),
                       
                       'archive' : PhotoImage(master = self.master, file = self.path_prog + '/image/zip.png'),
                       'append': PhotoImage(master = self.master, file = self.path_prog + '/image/plus.png'),
                       'compare': PhotoImage(master = self.master, file = self.path_prog + '/image/compare.png'),

                       'send': PhotoImage(master = self.master, file = self.path_prog + '/image/send.png'),
                       'clear': PhotoImage(master = self.master, file = self.path_prog + '/image/clear.png'),
                       'bip': PhotoImage(master = self.master, file = self.path_prog + '/image/bip.png'),
                       'ulla': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),

                       'update': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),
                       'upgrade': PhotoImage(master = self.master, file = ''),#self.path_prog + '/'),

                       'load': PhotoImage(master = self.master, file = self.path_prog + '/image/load.png'),

                       'ihm': PhotoImage(master = self.master, file = self.path_prog + '/image/config.png'),
                       'lnb': PhotoImage(master = self.master, file = self.path_prog + '/image/line.png'),
                       'dark': PhotoImage(master = self.master, file = self.path_prog + '/image/dark.png'),
                       'visut': PhotoImage(master = self.master, file = self.path_prog + '/image/task.png'),
                       'lgv': PhotoImage(master = self.master, file = self.path_prog + '/image/lg.png'),

                       'about': PhotoImage(master = self.master, file = self.path_prog + '/image/help.png'),
                       'doc': PhotoImage(master = self.master, file = self.path_prog + '/image/doc.png'),
                       'todo': PhotoImage(master = self.master, file = self.path_prog + '/image/todo.png'),
                       'lines': PhotoImage(master = self.master, file = self.path_prog + '/image/line.png'),
                       'struct': PhotoImage(master = self.master, file = self.path_prog + '/image/tree.png'),
                       'prog': PhotoImage(master = self.master, file = self.path_prog + '/image/prog.png'),
                       }
        self.size_images = (15, 15)

if __name__ == '__main__':
    from __init__ import *
