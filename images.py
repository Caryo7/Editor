#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

class Images:
    def __images__(self):
<<<<<<< Updated upstream
        self.images = {'new' : PhotoImage(file = self.path_prog + '/image/plus.png'),
                       'open' : PhotoImage(file = self.path_prog + '/image/open.png'),
                       'save' : PhotoImage(file = self.path_prog + '/image/save.png'),
                       'saveas' : PhotoImage(file = self.path_prog + '/image/saveas.png'),
                       'savecopyas' : PhotoImage(file = self.path_prog + '/image/savecopyas.png'),
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
=======
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
>>>>>>> Stashed changes

                       'infobar': PhotoImage(file = ''),#self.path_prog + '/'),
                       'ruban': PhotoImage(file = ''),#self.path_prog + '/'),
                       'buttonbar': PhotoImage(file = ''),#self.path_prog + '/'),
                       
<<<<<<< Updated upstream
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
=======
                       'puces': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/puces.png'),
                       'news': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/style.png'),
                       'cstyle': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/cstyle.png'),
                       
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
>>>>>>> Stashed changes

                       'update': PhotoImage(file = ''),#self.path_prog + '/'),
                       'upgrade': PhotoImage(file = ''),#self.path_prog + '/'),

<<<<<<< Updated upstream
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
=======
                       'load': PhotoImage(master = self.master, file = self.path_prog + '/image/16x16/load.png'),

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
>>>>>>> Stashed changes
                       }
        self.size_images = (15, 15)

if __name__ == '__main__':
    from __init__ import *
