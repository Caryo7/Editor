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

        if self.mode_record:
            self.events.append({'command': 'about'})

        zak = Toplevel(self.master)
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

        dic = {'Version :': f'{self.version}',
               lg('writeby'): self.AUTHOR,
               lg('email'): 'bravocharlie1273@orange.fr',
               lg('phone'): '07.87.25.46.41',
               lg('site'): self.URL.replace('https://', ''),
               lg('copyright'): 'All Right Reserved',
               'separator1': None,
               'Python :': self.PYTHON_VERSION,
               'Arduino :': self.ARDUINO_VERSION,
               'separator2': None,
               lg('GUI'): self.GUI_VERSION,
               lg('compilator'): self.COMPILATOR_VERSION,
               lg('langs'): self.LANGS_VERSION,
               lg('flm'): self.FILE_VERSION,
               lg('formf'): self.FORM_VERSION,
               'separator3': None,}

        row = 1
        for k, v in dic.items():
            if not v:
                Frame(cad, borderwidth = 1, relief = SUNKEN, height = 2, bg = '#bbbbbb').grid(row=row, column=0, sticky=EW, columnspan=3, padx=5, pady=5)

            else:
                Label(cad, text = k, justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, '')).grid(row = row, column = 0, sticky = E, padx = 0, pady = 5)
                l = Label(cad, text = v, justify = LEFT, fg = '#000000', bg = '#bbbbbb', font = ('Courier', 11, ''))
                l.grid(row = row, column = 1, sticky = W, padx = 10, pady = 5)
                if k == lg('site'):
                    l.bind('<Button-1>', lambda evt: self.open_internet(self.URL))
                    l.config(fg = 'blue', bg = '#bbbbbb', font = ('Courier', 11, 'underline'), cursor = 'hand2')
                elif k == lg('email'):
                    l.bind('<Button-1>', lambda evt: self.open_internet('bravocharlie1273@orange.fr'))
                    l.config(fg = 'blue', bg = '#bbbbbb', font = ('Courier', 11, 'underline'), cursor = 'hand2')

            row += 1

        Button(cad, text = lg('copyright'), justify = CENTER, relief = GROOVE, bd = 3, command = None        ).grid(row = row, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)
        Button(cad, text = lg('License'),   justify = CENTER, relief = GROOVE, bd = 3, command = self.License).grid(row = row + 1, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)
        Button(cad, text = lg('autors'),    justify = CENTER, relief = GROOVE, bd = 3, command = self.Authors).grid(row = row + 2, column = 0, sticky = EW, padx = 10, pady = 10, columnspan = 2)

        def close():
            zak.destroy()
            self.dialoging = False

        Button(zak, text = lg('close'), command = close, relief = SOLID, bd = 3).grid(row = 1, column = 0, padx = 10, pady = 10)
        zak.bind('<Escape>', lambda evt: close())
        zak.bind('<Return>', lambda evt: close())
        zak.update()

    def ToDo(self):
        if self.mode_record:
            self.events.append({'command': 'todo'})

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
            if self.mode_record:
                self.events.append({'command': 'doc'})

            f = open(self.path_prog + '/help.hlp', 'r', encoding = get_encode())
            self.insert('Documentation', f.read())
            f.close()

#help().About()
if __name__ == '__main__':
    from __init__ import *


