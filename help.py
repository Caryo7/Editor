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

class help_:
    curseurs = ['arrow', 'man', 'based_arrow_down', 'middlebutton', 'based_arrow_up', 'mouse', 'boat', 'pencil', 'bogosity', 'pirate', 'bottom_left_corner', 'plus', 'bottom_right_corner', 'question_arrow', 'bottom_side', 'right_ptr', 'bottom_tee', 'right_side', 'box_spiral', 'right_tee', 'center_ptr', 'rightbutton', 'circle', 'rtl_logo', 'clock', 'sailboat', 'coffee_mug', 'sb_down_arrow', 'cross', 'sb_h_double_arrow', 'cross_reverse', 'sb_left_arrow', 'crosshair', 'sb_right_arrow', 'diamond_cross',
               'sb_up_arrow', 'dot', 'sb_v_double_arrow', 'dotbox', 'shuttle', 'double_arrow', 'sizing', 'draft_large', 'spider', 'draft_small', 'spraycan', 'draped_box', 'star', 'exchange', 'target', 'fleur', 'tcross', 'gobbler', 'top_left_arrow', 'gumby', 'top_left_corner', 'hand1', 'top_right_corner', 'hand2', 'top_side', 'heart', 'top_tee', 'icon', 'trek', 'iron_cross', 'ul_angle', 'left_ptr', 'umbrella', 'left_side', 'ur_angle', 'left_tee', 'watch', 'leftbutton', 'xterm', 'll_angle', 'X_cursor', 'lr_angle']

    def About(self):
        if self.dialoging:
            return

        self.dialoging = True
        zak = Toplevel(self.master)
        zak.overrideredirect(1)
        zak.update()
        zak.wm_attributes('-topmost', 1)
        self.moving = IntVar(master = zak)
        self.moving.set(0)
        zak.bind('<ButtonPress-1>', lambda _: self.moving.set(1))
        zak.bind('<ButtonRelease-1>', lambda _: self.moving.set(0))
        def move(self, evt):
            if self.moving.get():
                zak.geometry('+' + str(evt.x_root) + '+' + str(evt.y_root))

        zak.bind('<Motion>', lambda evt: move(self, evt))
        zak.transient(self.master)
        zak.iconbitmap(self.ico['help'])
        zak.resizable(False, False)
        zak['bg'] = '#bbbbbb'
        zak.config(borderwidth = 5)
        zak.protocol('WM_DELETE_WINDOW', lambda : self.protocol_dialog(zak))
        zak.title(lg('About'))

        padx = 0

        cadre = Frame(zak, relief = SUNKEN, borderwidth = 2, bg = '#bbbbbb')
        cadre.grid(row = 0, column = 0, padx = 10, pady = 0)

        logo = Frame(cadre, bg = '#bbbbbb')
        logo.grid(row = 0, column = 0, sticky = N, padx = 10, pady = 0)

        cad = Frame(cadre, bg = '#bbbbbb')
        cad.grid(row = 1, column = 0, sticky = N, padx = 10, pady = 0)

        icon = PhotoImage(master = self.master, file = str(str(self.ico['win']).replace('.ico', '.png')))
        Label(logo, image = icon).grid(row = 0, column = 0, sticky = W, rowspan=2, padx = 10, pady = 0) ########

        Label(logo, text = f'{self.title}', fg = '#000000', bg = '#bbbbbb', font = ('Courier', 20, 'bold')).grid(row = 0, column = 1, sticky = E, padx = 10, pady = 0)

        Label(cad, text = 'Version :',       justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 1, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = f'{self.version}', justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 1, column = 1, sticky = W, padx = 10, pady = 5)
        
        Label(cad, text = lg('writeby'), justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 2, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.AUTHOR,   justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 2, column = 1, sticky = W, padx = 10, pady = 5)
        
        #Label(cad, text = lg('email'),                       justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 3, column = 0, sticky = E, padx = padx, pady = 5)
        #s1 = Label(cad, text = 'bravocharlie1273@orange.fr', justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 3, column = 1, sticky = W, padx = 10, pady = 5)
        
        #Label(cad, text = lg('phone'),       justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 4, column = 0, sticky = E, padx = padx, pady = 5)
        #s2 = Label(cad, text = '07.87.25.46.41', justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 4, column = 1, sticky = W, padx = 10, pady = 5)

        Label(cad, text = lg('site'),       justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 3, column = 0, sticky = E, padx = padx, pady = 5)
        s3 = Label(cad, text = self.URL.replace('https://', ''), justify = LEFT, fg = 'blue', bg = '#bbbbbb', font = ('Courier', 11, 'underline'), cursor = 'hand2')
        s3.grid(row = 3, column = 1, sticky = W, padx = 10, pady = 5)
        s3.bind('<Button-1>', lambda evt: self.open_internet(self.URL))
        
        Label(cad, text = lg('copyright'),      justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 4, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = 'All Right Reserved', justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 4, column = 1, sticky = W, padx = 10, pady = 5)

        Frame(cad, borderwidth = 1, relief = SUNKEN, height = 2, bg = '#bbbbbb').grid(row=5, column=0, sticky=EW, columnspan=3, padx=5, pady=5)

        Label(cad, text = 'Python :', justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 6, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.PYTHON_VERSION,      justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 6, column = 1, sticky = W, padx = 10, pady = 5)
        
        Label(cad, text = 'Arduino :', justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 7, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.ARDUINO_VERSION,      justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 7, column = 1, sticky = W, padx = 10, pady = 5)

        Frame(cad, borderwidth = 1, relief = SUNKEN, height = 2, bg = '#bbbbbb').grid(row=8, column=0, sticky=EW, columnspan=3, padx=5, pady=5)

        Label(cad, text = lg('GUI'), justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 9, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.GUI_VERSION,      justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 9, column = 1, sticky = W, padx = 10, pady = 5)

        Label(cad, text = lg('compilator'), justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 10, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.COMPILATOR_VERSION,              justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 10, column = 1, sticky = W, padx = 10, pady = 5)

        Label(cad, text = lg('langs'), justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 11, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.LANGS_VERSION,       justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 11, column = 1, sticky = W, padx = 10, pady = 5)

        Label(cad, text = lg('flm'), justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 12, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.FILE_VERSION,     justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 12, column = 1, sticky = W, padx = 10, pady = 5)

        Label(cad, text = lg('formf'), justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 13, column = 0, sticky = E, padx = padx, pady = 5)
        Label(cad, text = self.FORM_VERSION,     justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = 13, column = 1, sticky = W, padx = 10, pady = 5)

        Frame(cad, borderwidth = 1, relief = SUNKEN, height = 2, bg = '#bbbbbb').grid(row=14, column=0, sticky=EW, columnspan=3, padx=5, pady=5)

        Button(cad, text = lg('copyright'), justify = CENTER, relief = GROOVE, bd = 3, command = None        ).grid(row = 15, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)
        Button(cad, text = lg('License'),   justify = CENTER, relief = GROOVE, bd = 3, command = self.License).grid(row = 16, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)
        Button(cad, text = lg('autors'),    justify = CENTER, relief = GROOVE, bd = 3, command = self.Authors).grid(row = 17, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)

        def close():
            zak.destroy()
            self.dialoging = False

        Button(zak, text = lg('close'), command = close, relief = SOLID, bd = 3).grid(row = 1, column = 0, padx = 10, pady = 10)
        zak.bind('<Escape>', lambda evt: close())
        zak.bind('<Return>', lambda evt: close())
        zak.update()

    def ToDo(self):
        f = open(self.path_prog + '/TODO.txt', 'r', encoding = get_encode())
        SimpleDialog(self.master,
                     text=f.read(),
                     buttons = [lg('close')],
                     default = 0,
                     title = lg('About')).go()
        f.close()

    def License(self):
        f = open(self.path_prog + '/LICENSE', 'r', encoding = get_encode())
        r = f.read()
        f.close()
        zak = Toplevel(self.master)
        zak.transient(self.master)
        zak.title(lg('license'))
        zak.iconbitmap(self.ico['help'])
        zak.bind('<Escape>', lambda evt: zak.destroy())
        zak.bind('<Return>', lambda evt: zak.destroy())
        t = Text(zak, fg = 'black', bg = '#f0f0f0', width = 80)
        t.insert('end', r)
        t.config(stat = 'disabled')
        t.pack()
        Button(zak, text = lg('exit'), command = zak.destroy).pack()

    def Authors(self):
        SimpleDialog(self.master,
                     text='Auteur : Ben CARYO',
                     buttons = [lg('close')],
                     default = 0,
                     title = lg('License')).go()
            
    def insert(self, title, data):
        if not(self.dialoging):
            self.text.delete('0.0', END)
            self.text.insert(END, data)
            self.saved = True
            self.path = title
            self.update_line_numbers()
            self.master.title(self.title + ' - ' + self.path)

    def infos(self):
        if not(self.dialoging):
            self.open(name = self.path_prog + '/infos.form')

    def documentation(self):
        if not(self.dialoging):
            f = open(self.path_prog + '/help.hlp', 'r', encoding = get_encode())
            self.insert('Documentation', f.read())
            f.close()

#help().About()
if __name__ == '__main__':
    from __init__ import *


