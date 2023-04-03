#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

from counter import *
from confr import *
from lgviewer import *
from tree import *

class MenuBar:
    def __menu__(self):
        def notyet(evt=None):
            self.error(3)
            
        menubar = Menu(self.master)
        self.menubar = menubar
        self.master['menu'] = menubar
        
        if get_menufile():
            menufichier = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('File'), menu=menufichier)
            menufichier.add_command(label=lg('New'), accelerator=self.get_accelerator('new'), stat='normal', command=self.new, image = self.images['new'], compound='left')
            menufichier.add_separator()
            menufichier.add_command(label=lg('Open'), accelerator=self.get_accelerator('open'), stat='normal', command=self.open, image = self.images['open'], compound='left')
            self.menurfl = Menu(menufichier, tearoff=0)
            menufichier.add_cascade(label=lg('RecentFile'), menu=self.menurfl)
            for k, n in self.get_rfl():
                cmd = lambda : self.open_recent(n)
                self.menurfl.add_command(label=str(k) + ' ' + n, command = cmd)
            self.menurfl.add_separator()
            self.menurfl.add_command(label = lg('clear_recent'), command = self.clear_recent, accelerator=self.get_accelerator('clear_recent'))

            menufichier.add_separator()
            menufichier.add_command(label=lg('Save'), accelerator=self.get_accelerator('save'), stat='normal', command=self.save, image = self.images['save'], compound='left')
            menufichier.add_command(label=lg('Save_as'), accelerator=self.get_accelerator('saveas'), stat='normal', command=self.saveas, image = self.images['saveas'], compound='left')
            menufichier.add_command(label=lg('Save_copy_as'), accelerator=self.get_accelerator('savecopyas'), stat='normal', command=self.savecopyas, image = self.images['savecopyas'], compound='left')
            menufichier.add_separator()
            menufichier.add_command(label=lg('Print'), accelerator=self.get_accelerator('print'), stat='normal', command=self.print_window, image = self.images['print'], compound='left')
            menufichier.add_separator()
            menufichier.add_command(label=lg('close'), accelerator=self.get_accelerator('close'), stat = 'normal', command=self.fermer, image = self.images['close'], compound='left')
            menufichier.add_command(label=lg('Exit'), accelerator=self.get_accelerator('quit'), stat='normal', command=self.Quitter, image = self.images['exit'], compound='left')
            
        if get_menuedit():
            menuedition = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Edit'), menu=menuedition)
            menuedition.add_command(label=lg('Undo'), accelerator=self.get_accelerator('undo'), stat='normal', command=self.undo, image = self.images['undo'], compound='left')
            menuedition.add_command(label=lg('Redo'), accelerator=self.get_accelerator('redo'), stat='normal', command=self.redo, image = self.images['redo'], compound='left')
            menuedition.add_separator()
            menuedition.add_command(label=lg('Cut'), accelerator='Ctrl + X', stat='normal', command=self.cut, image = self.images['cut'], compound='left')
            menuedition.add_command(label=lg('Copy'), accelerator='Ctrl + C', stat='normal', command=self.copy, image = self.images['copy'], compound='left')
            menuedition.add_command(label=lg('Past'), accelerator='Ctrl + V', stat='normal', command=self.past, image = self.images['past'], compound='left')
            menuedition.add_separator()
            menuedition.add_command(label=lg('Select_all'), accelerator='Ctrl + A', stat='disabled', command=notyet, image = self.images['select'], compound='left')
            menuedition.add_command(label=lg('Goto_line'), accelerator=self.get_accelerator('goto'), stat='normal', command=self.gotol, image = self.images['gotol'], compound='left')
            menuedition.add_separator()
            menuedition.add_command(label=lg('Search'), accelerator=self.get_accelerator('search'), stat='normal', command=self.search, image = self.images['search'], compound='left')
            menuedition.add_command(label=lg('Replace'), accelerator=self.get_accelerator('replace'), stat='normal', command=self.replace, image = self.images['replace'], compound='left')

        if get_menuview():
            menuview = Menu(menubar, tearoff = 0)
            menubar.add_cascade(label = lg('view'), menu = menuview)
            self.info_bar.set(get_infobar())
            self.ruban.set(get_ruban())
            self.boutons.set(get_boutons())
            menuview.add_command(label=lg('menu'), stat = 'disabled')
            menuview.add_checkbutton(label=lg('infobar'), onvalue=1, offvalue=0, variable=self.info_bar, image = self.images['infobar'], compound='left', command = self.changebars)
            menuview.add_checkbutton(label=lg('buttonbar'), onvalue=1, offvalue=0, variable=self.boutons, image = self.images['buttonbar'], compound='left', command = self.changebars)
            
        if get_menustyle():
            menustyle = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Style'), menu=menustyle)
            self.puces_ = menustyle.add_checkbutton(label=lg('Puces'), onvalue=1, offvalue=0, variable=self.puces)
            menustyle.add_command(label=lg('NewS'), command=self.ask_new_tag, accelerator=self.get_accelerator('news'), image = self.images['news'], compound='left')
            menustyle.add_command(label=lg('CStyle'), command=self.add_tag_here, accelerator=self.get_accelerator('cstyle'), image = self.images['cstyle'], compound='left')
            menustyle.add_separator()
            self.mls = Menu(menustyle, tearoff=0)
            menustyle.add_cascade(label=lg('Styles'), menu=self.mls)

        if get_menuformat():
            menufor = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Format'), menu=menufor)
            menufor.add_command(label=lg('Comment'), stat='normal', command=self.comment, accelerator=self.get_accelerator('comment'), image = self.images['comment'], compound='left')
            menufor.add_command(label=lg('Uncomment'), stat='disabled', accelerator=self.get_accelerator('uncomment'), image = self.images['uncomment'], compound='left')

        if get_menurun():
            menurun = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Run'), menu=menurun)
            menurun.add_command(label=lg('Compile'), stat='disabled', accelerator=self.get_accelerator('compile'), image = self.images['compile'], compound='left')
            menurun.add_command(label=lg('Runs'), stat='disabled', accelerator=self.get_accelerator('run'), image = self.images['run'], compound='left')
            menurun.add_command(label=lg('Check'), stat='disabled', accelerator=self.get_accelerator('check'), image = self.images['check'], compound='left')
            menurun.add_command(label=lg('Solve'), stat='disabled', accelerator=self.get_accelerator('solve'), image = self.images['solve'], compound='left')

        if get_menuexport():
            menuexp = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Export'), menu=menuexp)
            menuexp.add_command(label=lg('Export_Word'), command=self.export_word, accelerator=self.get_accelerator('expw'), image = self.images['word'], compound='left')
            menuexp.add_command(label=lg('Export_PDF'), command=self.export_pdf, accelerator=self.get_accelerator('expp'), image = self.images['pdf'], compound='left')

        if get_menucrypt():
            menucrypt = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Crypt'), menu=menucrypt)
            menucrypt.add_command(label=lg('Generate_key'), command=self.generate_key, accelerator=self.get_accelerator('key'), image = self.images['key'], compound='left')
            menucrypt.add_separator()
            menucrypt.add_command(label=lg('Algorithm'), stat='disabled')
            menucrypt.add_command(label=lg('Caesar'), stat='disabled')

        if get_menuarch():
            menuarch = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Archive'), menu=menuarch)
            menuarch.add_command(label=lg('Create_archive'), command=self.create_a, accelerator=self.get_accelerator('archive'), image = self.images['archive'], compound='left')
            menuarch.add_command(label=lg('Add_archive'), command=self.add_new_version, accelerator=self.get_accelerator('append'), image = self.images['append'], compound='left')
            menuarch.add_separator()
            menuarch.add_command(label=lg('Compare'), command=self.compare, accelerator=self.get_accelerator('compare'), image = self.images['compare'], compound='left')

        if get_menumin():
            menumin = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Minitel'), menu=menumin)
            menumin.add_command(label=lg('Send_minitel'), command=self.send_file, accelerator=self.get_accelerator('send'), image = self.images['send'], compound='left')
            menumin.add_command(label=lg('Clear_minitel'), command=self.home, accelerator=self.get_accelerator('clear'), image = self.images['clear'], compound='left')
            menumin.add_separator()
            menumin.add_command(label=lg('Bip'), command=self.bip, accelerator=self.get_accelerator('bip'), image = self.images['bip'], compound='left')
            menumin.add_command(label=lg('Ulla'), command=self.ulla, accelerator=self.get_accelerator('ulla'), image = self.images['ulla'], compound='left')

        if get_menuupd():
            menuupd = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Update'), menu=menuupd)
            menuupd.add_command(label=lg('INV'), command=self.get_update, accelerator=self.get_accelerator('update'), image = self.images['update'], compound='left')
            menuupd.add_checkbutton(label=lg('INVI'), accelerator=self.get_accelerator('upgrade'), onvalue = 1, offvalue = 0, variable = self.checkupdate)
            menuupd.add_separator()
            menuupd.add_command(label=lg('AV') + str(self.version), stat='disabled')

        if get_menuext():
            self.menuext = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Extension'), menu=self.menuext)
            self.load_ext(True)

        if get_menumacro():
            menumacro = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Macro'), menu=menumacro)
            menumacro.add_command(label=lg('Load'), command=self.load_macro, accelerator=self.get_accelerator('macro'), image = self.images['load'], compound='left')

        if get_menuopt():
            menuopt = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Options'), menu=menuopt)
            menuopt.add_command(label=lg('Options'), command=self.IHM, accelerator=self.get_accelerator('cnf'), image = self.images['ihm'], compound='left')
            menuopt.add_separator()
            menuopt.add_command(label=lg('Line_Number'), stat='normal', command=self.act_widget_ln, accelerator=self.get_accelerator('lnb'), image = self.images['lnb'], compound='left')
            menuopt.add_command(label=lg('Dark_Mode'), stat='normal', command=self.act_color_theme, accelerator=self.get_accelerator('dark'), image = self.images['dark'], compound='left')
            menuopt.add_separator()
            menuopt.add_command(label=lg('Tasks'), stat='normal', command=self.show, accelerator=self.get_accelerator('visut'), image = self.images['visut'], compound='left')
            menuopt.add_command(label=lg('Lgv'), stat = 'normal', command=lambda : LgViewer(self.master), accelerator=self.get_accelerator('lgv'), image = self.images['lgv'], compound='left')

        if get_menuhelp():
            menuaide = Menu(menubar, tearoff=0)
            menubar.add_cascade(label=lg('Help'), menu=menuaide)
            menuaide.add_command(label=lg('About'), stat='normal', command=self.About, accelerator=self.get_accelerator('about'), image = self.images['about'], compound='left')
            menuaide.add_command(label=lg('Documentation'), stat='normal', command=self.documentation, accelerator=self.get_accelerator('doc'), image = self.images['doc'], compound='left')
            menuaide.add_command(label=lg('todo'), stat = 'normal', command = self.ToDo, accelerator=self.get_accelerator('todo'), image = self.images['todo'], compound='left')
            menuaide.add_separator()
            menuaide.add_command(label=lg('Lines'), stat='normal', command=lambda : act(self.master), accelerator=self.get_accelerator('lines'), image = self.images['lines'], compound='left')
            menuaide.add_command(label=lg('struct'), stat = 'normal', command = Tkin, accelerator=self.get_accelerator('struct'), image = self.images['struct'], compound='left')
            menuaide.add_command(label=lg('program'), stat = 'normal', command = Code, accelerator=self.get_accelerator('prog'), image = self.images['prog'], compound='left')
            menuaide.add_separator()
            menusample = Menu(menuaide, tearoff=0)
            menusample.add_command(label = lg('infos'), command = self.infos)
            menuaide.add_cascade(label=lg('Sample'), menu=menusample)

        self.set_cmds()

if __name__ == '__main__':
    from __init__ import *
