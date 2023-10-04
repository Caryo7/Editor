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
import os

class help_:
    curseurs = ['arrow', 'man', 'based_arrow_down', 'middlebutton', 'based_arrow_up', 'mouse', 'boat', 'pencil', 'bogosity', 'pirate', 'bottom_left_corner', 'plus',
                'bottom_right_corner', 'question_arrow', 'bottom_side', 'right_ptr', 'bottom_tee', 'right_side', 'box_spiral', 'right_tee', 'center_ptr', 'rightbutton', 'circle',
                'rtl_logo', 'clock', 'sailboat', 'coffee_mug', 'sb_down_arrow', 'cross', 'sb_h_double_arrow', 'cross_reverse', 'sb_left_arrow', 'crosshair', 'sb_right_arrow',
                'diamond_cross', 'sb_up_arrow', 'dot', 'sb_v_double_arrow', 'dotbox', 'shuttle', 'double_arrow', 'sizing', 'draft_large', 'spider', 'draft_small', 'spraycan',
                'draped_box', 'star', 'exchange', 'target', 'fleur', 'tcross', 'gobbler', 'top_left_arrow', 'gumby', 'top_left_corner', 'hand1', 'top_right_corner', 'hand2',
                'top_side', 'heart', 'top_tee', 'icon', 'trek', 'iron_cross', 'ul_angle', 'left_ptr', 'umbrella', 'left_side', 'ur_angle', 'left_tee', 'watch', 'leftbutton',
                'xterm', 'll_angle', 'X_cursor', 'lr_angle']

## Numéros de ligne impacté aux alentours de 130 !!!!!!!!!!!!

    auth_text = '''Contributeurs :


Aaron Caryo : (bgtarino@gmail.com)

Structure Python
Fonctions Python
Algorithmes d'import/export
Extension Fichiers .FORM

Jay Morrington : (animating.du.38@gmail.com)

Designer Graphique
Site internet PHP
Serveur discord (https://discord.gg/YPvQQAqgKw)

Développé sur une idée d'un ami'''

    def About(self):
        if self.dialoging:
            return

        self.dialoging = True

        if self.mode_record:
            self.events.append({'command': 'about'})

        root = Toplevel(self.master)
        root.transient(self.master)
        root.iconbitmap(self.ico['help'])
        root.resizable(False, False)
        root.config(borderwidth = 5)
        root.protocol('WM_DELETE_WINDOW', lambda : self.protocol_dialog(root))
        root.title(lg('About'))

        ong = ttk.Notebook(root)
        ong.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
        cad = Frame(ong, bg = '#bbbbbb')
        ong.add(text = lg('Version'), child = cad)

        logo = Frame(root)
        logo.grid(row = 0, column = 0, sticky = N, padx = 10, pady = 0)
        icon = PhotoImage(master = self.master, file = str(str(self.ico['win']).replace('.ico', '.png')))
        lb = Label(logo, image = icon)
        lb.grid(row = 0, column = 0, sticky = W, rowspan=2, padx = 10, pady = 0)
        lb.image = icon
        Label(logo, text = f'{self.title}', fg = '#000000', font = ('Courier', 20, 'bold')).grid(row = 0, column = 1, sticky = E, padx = 10, pady = 0)

        url = self.URL.replace('https://', '')
        url = url.split('.')
        url = url[0]

        dic = {'Version :': f'{self.version}',
               lg('site'): url,
               lg('copyright'): 'All Right Reserved',
               'separator1': None,
               'Python :': self.PYTHON_VERSION,
               'Arduino :': self.ARDUINO_VERSION,
               'separator2': None,
               lg('GUI'): self.GUI_VERSION,
               lg('compilator'): self.COMPILATOR_VERSION,
               lg('langs'): self.LANGS_VERSION,
               lg('flm'): self.FILE_VERSION,
               lg('formf_help'): self.FORM_VERSION,}

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
                    l.bind('<Button-1>', lambda evt: self.open_internet('mailto:' + v))
                    l.config(fg = 'blue', bg = '#bbbbbb', font = ('Courier', 11, 'underline'), cursor = 'hand2')

            row += 1

        h, w = 23, 70

        auth = Frame(ong)
        ong.add(text = lg('autors'), child = auth)
        ta = Text(auth, width = w, bg = '#f0f0f0', fg = 'black', height = h, font = ('Courier', 10))
        ta.grid()
        ta.insert('end', self.auth_text)
        ta.config(stat = 'disabled')
        def select_cursor(evt):
            ta.config(cursor = 'hand2')
        def unselect_cursor(evt):
            ta.config(cursor = '')
        def open_page(link):
            if link == 1:
                self.open_internet('mailto:bgtarino@gmail.com')
            elif link == 2:
                self.open_internet('mailto:animating.du.38@gmail.com')
            elif link == 3:
                self.open_internet('https://discord.gg/YPvQQAqgKw')

        links = {'link1': [('4.15', '4.33'), lambda _: open_page(1)],
                 'link2': [('11.18', '11.43'), lambda _: open_page(2)],
                 'link3': [('15.17', '15.46'), lambda _: open_page(3)],
                 }

        for ln, para in links.items():
            index, cmd = para
            ta.tag_add(ln, index[0], index[1])
            ta.tag_configure(ln, foreground = 'blue', font = ('Courier', 10, 'underline'))
            ta.tag_bind(ln, '<Control-Motion>', select_cursor)
            ta.tag_bind(ln, '<Leave>', unselect_cursor)
            ta.tag_bind(ln, '<Control-Button-1>', cmd)

        ta.tag_add('title', '1.0', '1.15')
        ta.tag_configure('title', font = ('Courier', 13, 'bold'))
        ta.tag_add('based', '17.0', '17.31')
        ta.tag_configure('based', font = ('Courier', 10, 'italic'))

        authors = {'1': ('4.0', '4.11'),
                   '2': ('11.0', '11.14')}

        for _, v in authors.items():
            ta.tag_add('auth', v[0], v[1])

        ta.tag_configure('auth', font = ('Courier', 10, 'underline'))


        cpr = Frame(ong)
        ong.add(text = lg('License'), child = cpr)
        t = Text(cpr, width = w, bg = '#f0f0f0', fg = 'black', height = h, font = ('Courier', 10), wrap = 'word')
        t.grid()
        f = open(self.path_prog + '/LICENSE', 'r', encoding = get_encode())
        t.insert('end', f.read())
        f.close()
        t.config(stat = 'disabled')

        def close():
            root.destroy()
            self.dialoging = False

        Button(root, text = lg('close'), command = close, relief = SOLID, bd = 3, width = 70).grid(row = 2, column = 0, padx = 10, pady = 10, columnspan = 2)
        root.bind('<Escape>', lambda evt: close())
        root.bind('<Return>', lambda evt: close())
        root.update()

    def ToDo(self):
        if self.mode_record:
            self.events.append({'command': 'todo'})

        f = open(self.path_prog + '/TODO.txt', 'r', encoding = get_encode())
        zak = Toplevel(self.master)
        zak.title(lg('About'))
        zak.iconbitmap(self.ico['todo'])
        Label(zak, text = f.read()).grid(pady = 5)
        Button(zak, text = lg('close'), command = zak.destroy, width = 30).grid(pady = 5)
        f.close()

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

            os.system('start ' + self.path_prog + '/documentation/Documentation.chm')

if __name__ == '__main__':
    from __init__ import *
