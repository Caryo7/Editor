#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinterdnd2 import *
from confr import *
from tooltip import *
from tree import *
import time, sys

class Content:
    width_linenb = 40
    height_infobar = 20
    width_scroll = 20
    height_ruban = 100
    height_boutons = 35
    old_height_boutons = 35

    def __content__(self):
        self.add_task(code='AutoResize', time=time.time(), desc='MAIN_LOOP\nWhen you resize window, this part of the program will be count the new size of window and will modify size of the text zone. Size of text zone is compute with coeficients, so, problems can be seen !', fnct = 'autoresize')
        self.add_task(code='AutoUnSave', time=time.time(), desc='MAIN_LOOP\nWhen you press a key, automaticly, the program is considering than you modified you data. It is gonna passed in mode : "Unsave"', fnct = 'autounsave')
        self.add_task(code='AutoUpdateLineNumbers', time=time.time(), desc='MAIN_LOOP\nWhen you press some keys, ths line number have to be update. Other wice, you can see problem and wrong number in front of line', fnct = 'autoline')
        self.add_task(code='AutoActiveMode', time=time.time(), desc='MAIN_LOOP\nThis mode is used to modify color of the text zone during your tests : when you press button in menu config', fnct = 'autoinvert')

        self.ruban = IntVar()
        self.info_bar = IntVar()
        self.boutons = IntVar()
        #self.ruban.set(get_ruban())
        #self.info_bar.set(get_infobar())
        #self.boutons.set(get_boutons())

        self.scroll = ttk.Scrollbar(self.master, orient='vertical')

        self.text = Text(self.master,
                         wrap = WORD,
                         yscrollcommand = self.scroll.set,
                         undo = True,
                         autoseparators = -1,
                         bg = get_bgd() if self.dark else get_bgl(),
                         fg = get_fgd() if self.dark else get_fgl(),
                         font = (get_font(), get_font_size()),
                         tabs = get_tabs(),
                         spacing1 = get_spacing1(),
                         spacing2 = get_spacing2(),
                         spacing3 = get_spacing3(),
                         #highlightbackbackground = read('text', 'highlightnfbackcolor'),
                         highlightcolor = read('text', 'highlightwfbackcolor'),
                         highlightthickness = read('text', 'highlightthickness'),
                         insertbackground = read('text', 'insertbackground'),
                         insertborderwidth = read('text', 'insertborderwidth'),
                         insertontime = read('text', 'insertontime'),
                         insertofftime = read('text', 'insertofftime'),
                         insertwidth = read('text', 'insertwidth'),
                         selectbackground = read('text', 'selectbackground'),
                         selectborderwidth = read('text', 'selectborderwidth'),)

        self.text.drop_target_register(DND_FILES)
        self.text.dnd_bind('<<Drop>>', self.drag_drop)
        self.text.focus()
        self.text.bind('<KeyPress>', self.unsave)
        self.text.bind('<KeyRelease>', self.infobar_changement)
        self.text.bind_all('<Button>', self.uln)
        self.text.bind_all('<MouseWheel>', self.uln)
        self.text.bind('<KeyRelease-Return>', self.act_puces)

        self.fonts = list(font.families())
        self.fonts.sort()

        self.scroll.config(command=self.text.yview)
        self.scroll.bind('<ButtonRelease-1>', self.uln)

        self.master.geometry(str(get_dims()[0]) + 'x' + str(get_dims()[1]))

        self.listchar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ',', ';', '!', '?', '.', '/', '§', '&', 'é', '"', '\'', '(', '-', 'è', '_', 'ç', 'à', ')', '=', '~', '#', '{', '[', '|', '`', '\\', '^', '@', ']', '}', '$', '£', '¤', '*', 'µ', '%', 'ù', ' ']
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'é', 'è', 'ç', 'à', '~', '#', '`', '^', '@', '$', '£', '¤', '*', 'µ', '%', 'ù', '_']
        self.lns = not(self.lns)
        self.act_widget_ln()

        self.keycodes       = ['Return', 'KP_Return', 'Next', 'Prior', 'BackSpace', 'Delete', 'Tab', 'Space', 'End', 'Home', 'Up', 'Down', 'Left', 'Right']
        self.keycode_unsave = ['Return', 'KP_Return', 'BackSpace', 'Delete', 'Tab', 'Space']
        
        self.update_line_numbers()
        self.puces = IntVar()
        self.puces.set(1 if get_puces() else 0)
        self.words = []
        self.texte = ''
        self.oldheight = self.master.winfo_height()
        self.oldwidth = self.master.winfo_width()
        self.master.bind('<Configure>', self.test_resize)

        #calltip = CallTip(self.text)

        self.conf_win(generate = True)
        self.__ac__()

    def get_index(self):
        return str(self.text.index('insert'))

    def move_to(self, index):
        self.text.see(index)
        self.text.mark_set('insert', index)

    def drag_drop(self, event):
        file = event.data
        self.open(name = file)

    def get_text(self, begin = '0.0', finish = 'end', save = False):
        if save:
            data = self.getBrutValueVars(self.text.get(begin, finish))
        else:
            data = self.text.get(begin, finish)

        if get_encrypted():
            data = self.encrypt(data)

        return data

    def clear_text(self):
        self.text.delete('0.0', 'end')

    def insert_text(self, data, with_vars = True):
        if get_encrypted():
            data = self.decrypt(data)

        if with_vars:
            data = self.getTextValueVars(data)

        self.text.insert(END, data)

    def insert_image(self, file, index):
        try:
            self.photos.append(PhotoImage(master = self.master, file=file))
            self.text.image_create(index, image=self.photos[-1])
        except:
            pass

    def stat_text(self, stat):
        if stat:
            self.text.config(stat = 'normal')
        else:
            self.text.config(stat = 'disabled')

    def test_resize(self, event = None):
        if isinstance(event.widget, Tk) and (event.width != self.oldwidth or event.height != self.oldheight):
            self.conf_win()
            self.oldheight = event.height
            self.oldwidth = event.width

    def changebars(self):
        if self.ruban.get():
            self.boutons.set(0)
        if self.boutons.get():
            self.ruban.set(0)
        self.conf_win(generate = True)
        
    def act_puces(self, evt=None):
        if self.puces.get():
            self.text.insert(INSERT, ' ' + self.text_puce + ' ')

    def append_bouton(self, width, typ, text = None, command = None, args = None):
        len_width = (width - 10) // (self.size_images[0] + 9 + 10)
        col = len(self.lst_bts) % len_width
        row = len(self.lst_bts) // len_width
        self.height_boutons = self.old_height_boutons
        for i in range(row):
            self.height_boutons += self.size_images[1] + 5 + 11

        if text:
            txt = lg(text)
            if text == 'exit':
                accelerator = self.get_accelerator('quit')
            else:
                accelerator = self.get_accelerator(text)

            if accelerator:
                txt += '\n(' + accelerator + ')'
        else:
            txt = ''

        if typ == Button:
            self.lst_bts.append(typ(self.frame_boutons, image = self.images[text], command = command, relief = 'flat', borderwidth = 0, highlightthickness = 0))
            self.lst_bts[-1].grid(row = row, column = col, padx = 10, pady = 5)
            ToolTip(self.lst_bts[-1], text = txt)

        elif typ == 'separator':
            self.lst_bts.append(Frame(self.frame_boutons, relief = SUNKEN, bd = 3, width = 4, height = self.size_images[1] + 5))
            self.lst_bts[-1].grid(row = row, column = col, padx = 5, pady = 5)

        else:
            self.lst_bts.append(typ(self.frame_boutons, text = '', **args))
            self.lst_bts[-1].grid(row = row, column = col, padx = 10, pady = 5)
            ToolTip(self.lst_bts[-1], text = txt)

    def conf_win(self, evt=None, generate = False):
        try:
            if self.lst_fnct['autoresize']:
                return
        except:
            pass

        if (not self.generating and not self.dialoging) or generate:
            h = self.master.winfo_height()
            w = self.master.winfo_width()

            x = 0
            y = 0

            if self.boutons.get(): ## MORCEAU DE CODE DANS MAIN.PY (__start__.py -> try)
                try:
                    self.frame_boutons.config(width = w, height = self.height_boutons)
                except AttributeError:
                    self.frame_boutons = Frame(self.master, width = w, height = self.height_boutons)
                    self.frame_boutons.place(x = 0, y = 0)
                    self.lst_bts = []

                for item in self.lst_bts:
                    item.destroy()
                self.lst_bts.clear()

                for widget, name, command, separator in self.menu_bts:
                    if separator:
                        self.append_bouton(w, 'separator')
                        continue

                    self.append_bouton(w, widget, name, command = command if not isinstance(command, dict) else None, args = command if isinstance(command, dict) else None)

                y += self.height_boutons
            else:
                try:
                    self.frame_boutons.destroy()
                    del self.frame_boutons
                except:
                    pass

            if self.lns:
                self.line_numbers_canvas.config(height=h - y - (self.height_infobar if self.info_bar.get() else 0))
                self.line_numbers_canvas.place(x=0, y = y)
                x += self.width_linenb

            self.text.place(x = x, y = y, width = w - x - self.width_scroll, height = h - y - (self.height_infobar if self.info_bar.get() else 0))
            x += w - x - self.width_scroll
            
            self.scroll.place(x = x, y = y, width = self.width_scroll, height = h - y - (self.height_infobar if self.info_bar.get() else 0))
            y += h - y - (self.height_infobar if self.info_bar.get() else 0)

            if self.info_bar.get():
                try:
                    self.infobar_changement()
                except Exception:
                    self.label_infobar = Label(self.master, text = '', bg = '#f0f0f0', fg = 'black', anchor = 'e', font = ('Consolas', 8))
                    self.infobar_changement()

                self.label_infobar.place(x = 0, y = y, height = self.height_infobar, width = w)

            else:
                try:
                    self.label_infobar.destroy()
                except:
                    pass

            self.update_line_numbers()

    def infobar_changement(self, evt = None, no_colors = False):
        if not no_colors:
            self.autocolorwords()

        if self.info_bar.get():
            lines = self.text.get('0.0', 'end').split('\n')
            (line, column) = self.text.index('insert').split('.')
            line, column = int(line), int(column)
            len_line = len(lines) - 1
            len_col = len(lines[line - 1])

            #self.label_infobar.config(text = lg('Encodage') + str(get_encode()) + '  ' + lg('Line') + str(line) + '/' + str(len_line) + '  ' + lg('Column') + str(column) + '/' + str(len_col) + '  ' + lg('Position') + str(self.text.index('insert')))
            self.label_infobar.config(text = lg('Line') + str(line) + '/' + str(len_line) + '  ' + lg('Column') + str(column))

    def uln(self, evt):
        if self.lst_fnct['autoline']:
            return
        if not(self.dialoging):
            self.text.after(0, self.update_line_numbers)

    def act_widget_ln(self):
        if self.lst_fnct['autoinvert']:
            return
        if not(self.dialoging):

            if self.mode_record:
                self.events.append({'command': 'lnb'})

            self.lns = not(self.lns)
            if self.lns:
                self.text.place(x=self.width_linenb, width = self.master.winfo_width() - self.width_scroll - self.width_linenb)
                self.line_numbers_canvas = Canvas(self.master,
                                                  width=self.width_linenb,
                                                  height=self.master.winfo_height() - (self.height_boutons if self.boutons.get() else 0) - (self.height_infobar if self.info_bar.get() else 0),
                                                  bg='#555555',
                                                  highlightbackground='#555555',
                                                  highlightthickness=0,
                                                  yscrollcommand=self.scroll.set)

                self.line_numbers_canvas.place(x=0, y = 0 if not self.boutons.get() else self.height_boutons)
            else:
                self.text.place(x=0, width = self.master.winfo_width() - self.width_scroll)
                try:
                    self.line_numbers_canvas.destroy()
                except:
                    ""

            self.update_line_numbers()

    def act_color_theme(self):
        if not(self.dialoging):

            if self.mode_record:
                self.events.append({'command': 'dark'})

            self.dark = not(self.dark)
            self.text.config(bg=get_bgd() if self.dark else get_bgl(), fg=get_fgd() if self.dark else get_fgl())

    def update_line_numbers(self, evt=None, fforbid = False):
        if not(self.dialoging) or fforbid:
            self.infobar_changement(no_colors = True)
            if self.lns:
                fnt = get_font()
                size = get_font_size()
                self.line_numbers_canvas.delete('all')
                i = self.text.index('@0,0')
                self.text.update()
                while True:
                    dline = self.text.dlineinfo(i)
                    if dline:
                        y = dline[1]
                        linenum = str(int(float(i.replace('.0', ''))%10000))
                        self.line_numbers_canvas.create_text(1, y, anchor='nw', text=linenum, fill='#ffffff', font=(fnt, size))
                        i = self.text.index('{0}+1line'.format(i))
                    else:
                        break

    def test_lnu(self, evt):
        if not(self.dialoging):
            if evt.keycode in self.keycodes or evt.keysym in self.keycodes:
                self.text.after(0, self.update_line_numbers)

    def split(self, value):
        r = []
        m = ''
        for i in value:
            if i in [' ', ',', '\n', '=', '(', ')', '[', ']', '{', '}', ':']:
                r.append(m)
                m = ''
            else:
                m += i
        return r

    def unsave(self, evt, forcing = False):
        if self.lst_fnct['autounsave']:
            return

        if forcing:
            self.nofileopened = False
            self.saved = False
            self.master.title('* ' + self.title + ' - ' + self.path + ' *')
            return

        if not self.dialoging:
            self.texte += evt.char
            self.text.edit_separator()
            self.test_lnu(evt)

            self.key_press_test(evt)
            
            if evt.char.lower() in self.listchar or (evt.keysym in self.keycode_unsave) or (evt.keycode in self.keycode_unsave):
                self.saved = False
                self.nofileopened = False
                self.master.title('* ' + self.title + ' - ' + self.path + ' *')

if __name__ == '__main__':
    from __init__ import *
