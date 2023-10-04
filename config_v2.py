from confr import *
from tooltip import *
from tkinter import *
from progress import *
from tkinter import ttk
from tkinter import font
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinter.colorchooser import *
from switchbt import *

bg_type = get_dark()
if bg_type:
    BG = get_bgd()
    FG = get_fgd()
else:
    BG = get_bgl()
    FG = get_fgl()

class ScreenMenu:
    def rtnTrue(self):
        return True

    def __init__(self, parent, master = None):
        self.main = Frame(parent)
        self.main['bg'] = BG

        self.dic = {lg('file'): ['', ('menu', 'file')],
                    lg('edit'): ['', ('menu', 'edit')],
                    lg('view'): ['', ('menu', 'view')],
                    lg('AI'): ['', ('menu', 'ai')],
                    lg('style'): ['', ('menu', 'style')],
                    lg('variables'): ['', ('menu', 'vars')],
                    lg('format'): ['', ('menu', 'format')],
                    lg('run'): ['', ('menu', 'run')],
                    lg('export'): ['', ('menu', 'export')],
                    lg('crypt'): ['', ('menu', 'crypt')],
                    lg('archive'): ['', ('menu', 'arch')],
                    lg('minitel'): ['', ('menu', 'minitel')],
                    lg('update'): ['', ('menu', 'update')],
                    lg('extension'): ['', ('menu', 'extension')],
                    lg('macro'): ['', ('menu', 'macro')],
                    lg('options'): ['', ('menu', 'opt')],
                    lg('help'): ['', ('menu', 'help')],}

        row = 0
        col = 0
        Label(self.main, bg = BG, fg = FG, text = 'Vert : Menu Visible; Rouge : Menu masqué', font = ('Consolas', 12, 'italic')).grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 5)
        for k, v in self.dic.items():
            row += 1
            if not v:
                Frame(self.main, borderwidth = 1, relief = SUNKEN, height = 4, bg = '#bbbbbb').grid(row = row, column = 0, sticky = EW, columnspan = 6, padx = 5, pady = 5)
                continue
            v = v.copy()
            v[1] = read(v[1][0], v[1][1])

            Label(self.main, bg = BG, fg = FG, text = k, font = ('Courier', 10)).grid(row = row, column = col, sticky = 'w', padx = 5, pady = 5)
            if k == lg('options'):
                self.dic[k].append(self.rtnTrue)
                continue

            s = Switch(self.main, stat = v[1])
            s.grid(row = row, column = col + 1, sticky = 'w')
            self.dic[k].append(s.get)

            if row == int(len(self.dic) / 2):
                row = 0
                col = 3
                Frame(self.main, borderwidth = 1, relief = SUNKEN, width = 4, bg = '#bbbbbb').grid(row = 1, column = 2, sticky = NS, rowspan = int(len(self.dic) / 2) + 1, padx = 5, pady = 5)

    def get(self):
        return self.main

    def results(self):
        r = {}
        for name, data in self.dic.items():
            if data:
                r[name] = {'result': data[-1](), 'section': data[1][0], 'option': data[1][1]}

        return r


class ScreenSecu:
    def __init__(self, parent, browser, master = None):
        self.main = Frame(parent)
        self.main['bg'] = BG
        self.browser = browser

        self.dic = {lg('encrypting'): ['s', ('global', 'encrypt')],
                    lg('connexion'): ['s', ('global', 'conn')],
                    lg('key'): ['', ('crypt', 'key')],
                    '1': None,
                    lg('username'): ['', ('security', 'username')],
                    lg('password'): ['*', ('security', 'password')],
                    '2': None,
                    lg('navig'): ['c', ('global', 'browser')],
                    'Discord': ['s', ('global', 'discord')],
                    '3': None,
                    lg('tips'): ['s', ('global', 'tips')],
                    }

        row = -1
        col = 0
        for k, v in self.dic.items():
            row += 1
            if not v:
                Frame(self.main, borderwidth = 1, relief = SUNKEN, height = 4, bg = '#bbbbbb').grid(row = row, column = 0, sticky = EW, columnspan = 6, padx = 5, pady = 5)
                continue
            v = v.copy()
            v[1] = read(v[1][0], v[1][1])

            Label(self.main, bg = BG, fg = FG, text = k, font = ('Courier', 10)).grid(row = row, column = col, sticky = 'w', padx = 5, pady = 5)

            if v[0] == 's':
                s = Switch(self.main, stat = v[1])
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

            elif v[0] in ('', '*'):
                e = StringVar(master = master)
                e.set(v[1])
                Entry(self.main, show = v[0], textvariable = e).grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(e.get)

            elif v[0] == 'c':
                c = ttk.Combobox(self.main, values = self.browser)
                c.grid(row = row, column = col + 1, sticky = 'w')
                try:
                    index = self.browser[v[1]]
                    c.current(index)
                except:
                    c['value'] = list(c['value']) + [v[1]]
                    c.current(END)

                self.dic[k].append(c.get)

    def get(self):
        return self.main

    def results(self):
        r = {}
        for name, data in self.dic.items():
            if data:
                r[name] = {'result': data[-1](), 'section': data[1][0], 'option': data[1][1]}

        return r


class ScreenView:
    def __init__(self, parent, codage, langs, progs, master = None):
        self.main = Frame(parent)
        self.main['bg'] = BG
        self.codes = codage
        self.langs = langs
        self.progs = progs

        self.dic = {lg('codage'): ['lc', ('crypt', 'code')],
                    lg('langage'): ['lp', ('global', 'lang')],
                    lg('coloration'): ['sw', ('global', 'colors')],
                    lg('langue_pa') + ' ': ['ll', ('gen', 'lg')],
                    '1': None,
                    lg('errors'): ['sw', ('global', 'errors')],
                    lg('askc'): ['sw', ('global', 'askclose')],
                    lg('update'): ['sw', ('global', 'look_update')],
                    lg('notifs'): ['sw', ('global', 'notifs')],
                    '2': None,
                    lg('dark_mode'): ['sw', ('global', 'mode_dark')],
                    lg('line_number'): ['sw', ('global', 'line_number')],
                    lg('new_ihm_config'): ['sw', ('global', 'version_config')],
                    '3': None,
                    lg('buttonbar'): ['sw', ('view', 'bar_buttons')],
                    lg('infobar'): ['sw', ('view', 'bar_info')],
                    }

        row = -1
        col = 0
        for k, v in self.dic.items():
            row += 1
            if not v:
                Frame(self.main, borderwidth = 1, relief = SUNKEN, height = 4, bg = '#bbbbbb').grid(row = row, column = 0, sticky = EW, columnspan = 6, padx = 5, pady = 5)
                continue
            v = v.copy()
            if k == lg('langue_pa') + ' ':
                v[1] = sel_lg()
            else:
                v[1] = read(v[1][0], v[1][1])

            Label(self.main, bg = BG, fg = FG, text = k, font = ('Courier', 10)).grid(row = row, column = col, sticky = 'w', padx = 5, pady = 5)

            if v[0] == 'sw':
                s = Switch(self.main, stat = v[1])
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

            elif v[0] == 'lc':
                c = ttk.Combobox(self.main, values = self.codes)
                c.grid(row = row, column = col + 1, sticky = 'w')
                c.config(stat = 'disabled')
                try:
                    index = self.codes.index(v[1])
                    c.current(index)
                except:
                    c['value'] = list(c['value']) + [v[1]]
                    c.current(END)

                self.dic[k].append(c.get)

            elif v[0] == 'll':
                c = ttk.Combobox(self.main, values = list(self.langs.keys()))
                c.grid(row = row, column = col + 1, sticky = 'w')
                try:
                    index = list(self.langs.values()).index(v[1])
                    c.current(index)
                except:
                    c['value'] = list(c['value']) + [v[1]]
                    c.current(END)

                self.dic[k].append(c.get)

            elif v[0] == 'lp':
                c = ttk.Combobox(self.main, values = self.progs)
                c.grid(row = row, column = col + 1, sticky = 'w')
                try:
                    index = self.progs.index(v[1])
                    c.current(index)
                except:
                    c['value'] = list(c['value']) + [v[1]]
                    c.current(END)

                self.dic[k].append(c.get)

    def get(self):
        return self.main

    def results(self):
        r = {}
        for name, data in self.dic.items():
            if data:
                r[name] = {'result': data[-1](), 'section': data[1][0], 'option': data[1][1]}

        return r


class ScreenText:
    def get_color_pos(self, data):
        try:
            return list(self.colors.values()).index(data)
        except:
            return data
        
    def get_font_pos(self, data):
        try:
            return self.fonts.index(data)
        except:
            pass

    def __init__(self, parent, colors, fonts, master = None):
        self.main = Frame(parent)
        self.main['bg'] = BG
        self.colors = colors
        self.fonts = fonts

        self.dic = {lg('Light_Background_Color'): ['lc', ('text', 'bgl')],
                    lg('Light_Foreground_Color'): ['lc', ('text', 'fgl')],
                    lg('Dark_Background_Color'): ['lc', ('text', 'bgd')],
                    lg('Dark_Foreground_Color'): ['lc', ('text', 'fgd')],
                    '1': None,
                    lg('Font'): ['lf', ('text', 'font')],
                    lg('FS'): ['sp', ('text', 'size')],
                    lg('tab'): ['sp', ('text', 'tab')],
                    lg('puces'): ['sw', ('text', 'puces')],
                    }

        row = -1
        col = 0
        for k, v in self.dic.items():
            row += 1
            if not v:
                Frame(self.main, borderwidth = 1, relief = SUNKEN, height = 4, bg = '#bbbbbb').grid(row = row, column = 0, sticky = EW, columnspan = 6, padx = 5, pady = 5)
                continue
            v = v.copy()
            v[1] = read(v[1][0], v[1][1])

            Label(self.main, bg = BG, fg = FG, text = k, font = ('Courier', 10)).grid(row = row, column = col, sticky = 'w', padx = 5, pady = 5)

            if v[0] == 'lc':
                c = ttk.Combobox(self.main, value = list(colors.keys()))
                c.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(c.get)
                pos = self.get_color_pos(v[1])
                if isinstance(pos, int):
                    c.current(pos)
                else:
                    c['value'] = list(c['value']) + [pos]
                    c.current(END)

            elif v[0] == 'lf':
                c = ttk.Combobox(self.main, value = self.fonts)
                c.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(c.get)
                pos = self.get_font_pos(v[1])
                if isinstance(pos, int):
                    c.current(pos)
                else:
                    c.current(0)

            elif v[0] == 'sp':
                s = Spinbox(self.main, value = int(v[1]), from_ = 2, to = 90)
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

            elif v[0] == 'sw':
                s = Switch(self.main, stat = v[1])
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

    def get(self):
        return self.main

    def results(self):
        r = {}
        for name, data in self.dic.items():
            if data:
                r[name] = {'result': data[-1](), 'section': data[1][0], 'option': data[1][1]}

        return r


class ScreenFile:
    def __init__(self, parent, master = None):
        self.main = Frame(parent)
        self.main['bg'] = BG

        self.dic = {lg('Active'): ['sw', ('auto_save', 'active')],
                    lg('delay'): ['sp', ('auto_save', 'delay')],
                    lg('path'): ['e', ('auto_save', 'path')],
                    }

        row = -1
        col = 0
        for k, v in self.dic.items():
            row += 1
            if not v:
                Frame(self.main, borderwidth = 1, relief = SUNKEN, height = 4, bg = '#bbbbbb').grid(row = row, column = 0, sticky = EW, columnspan = 6, padx = 5, pady = 5)
                continue
            v = v.copy()
            v[1] = read(v[1][0], v[1][1])

            Label(self.main, bg = BG, fg = FG, text = k, font = ('Courier', 10)).grid(row = row, column = col, sticky = 'w', padx = 5, pady = 5)

            if v[0] == 'e':
                e = StringVar(master = master)
                e.set(v[1])
                Entry(self.main, textvariable = e).grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(e.get)
                def insert():
                    n = asksaveasfilename(title=lg('open') + ' ' + lg('bu'), initialdir='.', filetypes=[(lg('bu'), '.bu')])
                    if n:
                        e.set(n)

                Button(self.main, text = lg('...'), command = insert, width = 3).grid(row = row, column = col + 2, sticky = 'w')

            elif v[0] == 'sp':
                s = Spinbox(self.main, value = int(v[1]) / 60, from_ = 2, to = 90)
                s.grid(row = row, column = col + 1, sticky = 'w')
                ToolTip(s, text = lg('time_autosave'))
                self.dic[k].append(s.get)

            elif v[0] == 'sw':
                s = Switch(self.main, stat = v[1])
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

    def get(self):
        return self.main

    def results(self):
        r = {}
        for name, data in self.dic.items():
            if data:
                r[name] = {'result': data[-1](), 'section': data[1][0], 'option': data[1][1]}

        return r


class ScreenMinitel:
    def __init__(self, parent, ports, master = None):
        self.main = Frame(parent)
        self.main['bg'] = BG
        self.ports = ports

        self.dic = {'Dev :': ['c', ('minitel', 'dev')],
                    lg('speed'): ['s', ('minitel', 'speed')],
                    'Byte Size :': ['s', ('minitel', 'bytesize')],
                    'Time out :': ['s', ('minitel', 'timeout')],
                    lg('alertemin'): ['sw', ('minitel', 'alerte')],
                    }

        row = -1
        col = 0
        for k, v in self.dic.items():
            row += 1
            if not v:
                Frame(self.main, borderwidth = 1, relief = SUNKEN, height = 4, bg = '#bbbbbb').grid(row = row, column = 0, sticky = EW, columnspan = 6, padx = 5, pady = 5)
                continue
            v = v.copy()
            v[1] = read(v[1][0], v[1][1])

            Label(self.main, bg = BG, fg = FG, text = k, font = ('Courier', 10)).grid(row = row, column = col, sticky = 'w', padx = 5, pady = 5)

            if v[0] == 'c':
                c = ttk.Combobox(self.main, values = self.ports)
                c.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(c.get)
                try:
                    index = self.ports.index(v[1])
                    c.current(index)
                except:
                    c['value'] = list(c['value']) + [v[1]]
                    c.current(END)

            elif v[0] == 's':
                s = Spinbox(self.main, value = v[1], from_ = 0, to = 9600)
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

            elif v[0] == 'sw':
                s = Switch(self.main, stat = v[1])
                s.grid(row = row, column = col + 1, sticky = 'w')
                self.dic[k].append(s.get)

    def get(self):
        return self.main

    def results(self):
        r = {}
        for name, data in self.dic.items():
            if data:
                r[name] = {'result': data[-1](), 'section': data[1][0], 'option': data[1][1]}

        return r


class ScreenLinks:
    def __init__(self, parent, master, cmds = None, ico = None, path_prog = None):
        self.main = Frame(parent)
        self.path_prog = path_prog
        self.main['bg'] = BG
        self.tk = master
        self.ico = ico
        self.__keyb__, self.get_accelerator = cmds

        self.tree = ttk.Treeview(self.main, show = 'headings', columns = (1, 2, 3), height = 20)
        scroll = ttk.Scrollbar(self.main, orient = 'vertical', command = self.tree.yview)
        self.tree.place(x = 0, y = 0)
        self.tree.config(yscrollcommand = scroll.set)
        self.tree.heading(1, text = lg('event'))
        self.tree.heading(2, text = lg('key_t'))
        self.tree.heading(3, text = lg('action'))
        self.tree.column(1, width = 150)
        self.tree.column(2, width = 150)
        self.tree.column(3, width = 180)
        self.tree.bind('<Double-Button-1>', self.change_linkkey)

        self.insert_keys()

    def change_linkkey(self, evt):
        self.selected = self.tree.item(self.tree.selection())['values']
        if not self.selected:
            return

        self.root = Toplevel(self.tk)
        self.root.transient(self.tk)
        self.root.iconbitmap(self.ico)
        self.root.title(lg('configurator'))
        Label(self.root, text = self.selected[2], font = ('Consolas', 12), wraplength = 175).place(x = 10, y = 10)
        Label(self.root, text = lg('newrac'), font = ('Consolas', 13, 'bold')).place(x = 10, y = 50)
        e = StringVar(master = self.tk)
        self.e = Entry(self.root, textvariable = e, font = ('Consolas', 13, 'italic'), width = 17)
        self.e.place(x = 10, y = 90)
        self.e.insert('end', self.selected[1])
        self.list_keys = self.selected[1].split(' + ')
        self.fin_key = []
        shift = False
        self.control = False
        self.alt = False
        for i in self.list_keys:
            if i == 'Ctrl':
                self.fin_key.append('<Control')
            elif i == 'Alt':
                self.fin_key.append('Alt')
            elif i == 'Shift':
                shift = True
            else:
                self.fin_key.append(i.lower() if not shift else i.upper())

        self.e.bind('<KeyPress>', self.keypress_link)
        self.e.bind('<KeyRelease>', self.key_release_link)
        
        Button(self.root, command = self.valide_linkkey, text = lg('OK')).place(x = 10, y = 130)
        Button(self.root, command = self.root.destroy, text = lg('cancel')).place(x = 110, y = 130)
        Button(self.root, command = lambda : self.valide_linkkey(True), text = lg('retirer')).place(x = 10, y = 160)
        self.root.geometry('200x200')

    def key_release_link(self, evt):
        if evt.keysym in ('Control_L', 'Control_R'):
            self.control = False

        elif evt.keysym in ('Alt_L', 'Alt_R'):
            self.alt = False

    def keypress_link(self, evt):
        if len(evt.keysym) == 1:
            if 96 < ord(evt.keysym) < 96 + 26 or 64 < ord(evt.keysym) < 64 + 26:
                self.list_keys.append(evt.keysym.upper())
                self.fin_key.append(evt.keysym + '>')

        elif evt.keysym in ('Control_L', 'Control_R') and not self.alt:
            self.list_keys = ['Ctrl']
            self.fin_key = ['<Control']
            control = True

        elif evt.keysym in ('Shift_L', 'Shift_R') and not 'Shift' in self.list_keys:
            self.list_keys.append('Shift')

        elif evt.keysym in ('Alt_L', 'Alt_R') and self.list_keys[-1] != '' and 'Alt' not in self.list_keys:
            self.list_keys.append('Alt')
            self.fin_key.append('Alt')

        elif evt.keysym in ('Alt_L', 'Alt_R') and self.list_keys[-1] == '' and not self.control:
            self.list_keys = ['Alt']
            self.fin_key = ['<Alt']
            self.alt = True

        elif evt.keysym == 'ISO_Level3_Shift':
            self.list_keys = ['Ctrl']
            self.fin_key = ['<Control']
            self.list_keys.append('Alt')
            self.fin_key.append('Alt')

        elif evt.keysym[0] == 'F':
            self.list_keys = [evt.keysym]
            self.fin_key = ['<' + evt.keysym + '>']

        self.e.delete('0', 'end')
        self.e.insert('end', ' + '.join(self.list_keys))

    def valide_linkkey(self, delete = False):
        f = open(self.path_prog + '/keys.k', 'r', encoding = get_encode())
        r = f.read()
        f.close()

        res = ''
        for line in r.split('\n'):
            if not line:
                continue

            name, event = line.split(' = ')
            if name == self.selected[0]:
                if delete:
                    line = name + ' = '
                else:
                    line = name + ' = ' + '-'.join(self.fin_key)
            else:
                line = name + ' = ' + event
            res += line + '\n'

        f = open(self.path_prog + '/keys.k', 'w', encoding = get_encode())
        f.write(res)
        f.close()
        self.root.destroy()
        self.insert_keys()

    def clear_tree(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

    def insert_keys(self):
        self.clear_tree()
        try:
            self.__keyb__()
        except Exception:
            return

        f = open(self.path_prog + '/keys.k', 'r', encoding = get_encode())
        r = f.read()
        f.close()
        for line in r.split('\n'):
            if line == '':
                continue

            name = line.split(' = ')[0]
            event = self.get_accelerator(name)
            self.tree.insert('', 'end', values = (name, event, ''))

    def get(self):
        return self.main


class ScreenCustomize:
    def __init__(self, parent, master, nom_bts, mode, ico = None, path_prog = None):
        self.main = Frame(parent)
        self.path_prog = path_prog
        self.main['bg'] = BG
        if mode == 'clk':
            self.mode = '#clk'
        elif mode == 'bbt':
            self.mode = '#bts'

        self.nom_bts = nom_bts
        self.master = master
        self.ico = ico

        self.lst_bt = Listbox(self.main, height = 25, font = ('Courier', 14), width = 38)
        ToolTip(self.main, lg('PPKTA'))
        scroll2 = ttk.Scrollbar(self.main, orient = 'vertical', command = self.lst_bt.yview)
        self.lst_bt.place(x = 0, y = 0)
        self.lst_bt.config(yscrollcommand = scroll2.set)
        scroll2.place(x = self.lst_bt.winfo_reqwidth(), y = 0, height = self.lst_bt.winfo_reqheight(), width = 20)
        f = open(self.path_prog + '/menus.m', 'r')
        r = f.read()
        f.close()
        mod = False
        for line in r.split('\n'):
            if line == '':
                continue

            if line == self.mode:
                mod = True
                continue

            elif line[0] == '#':
                mod = False
                continue

            ln = line.split(',')
            if mod and self.mode == '#clk':
                if ln[4] == '1':
                    self.lst_bt.insert('end', lg('Separateur'))
                elif ln[2] == '1':
                    self.lst_bt.insert('end', lg('Puces'))
                elif ln[3] == '1':
                    self.lst_bt.insert('end', lg('search'))
                else:
                    self.lst_bt.insert('end', self.nom_bts[ln[0]])

            elif mod and self.mode == '#bts':
                if ln[2] == '1':
                    self.lst_bt.insert('end', lg('Separateur'))
                else:
                    self.lst_bt.insert('end', self.nom_bts[ln[1]])

        def append1(evt):
            a = Toplevel(self.master)
            a.transient(self.master)
            a.title(lg('configurator'))
            a.iconbitmap(self.ico)
            a.resizable(False, False)
            Label(a, text = lg('add')).place(x = 5, y = 5)
            lst = []
            for k, v in self.nom_bts.items():
                lst.append(v)
            c = ttk.Combobox(a, values = lst)
            c.place(x = 5, y = 35)
            def append2():
                pass

            b = Button(a, text = lg('add'), command = append2, stat = 'disabled')
            b.place(x = 5, y = 65)
            ToolTip(b, lg('notimp'))
            a.geometry('150x95')

        self.lst_bt.bind('+', append1)

    def get(self):
        return self.main


class Data:
    colors = {lg('black'): 'black', lg('white'): 'white', lg('blue'): 'blue', lg('green'): 'green', lg('yellow'): 'yellow', lg('red'): 'red', lg('pink'): 'pink', lg('orange'): 'orange', lg('grey'): 'grey', }
    colors_name = [v for v, _ in colors.items()]
    langs = {lg('anglais') : 'an',
             lg('francais') : 'fr',
             lg('allemand') : 'al',
             lg('espagnol') : 'es',
             lg('italien') : 'it',
             lg('chinois') : 'ch',}

    codages = ['UTF-8', 'UTF-16', 'UTF-4', 'ASCII']
    browsers = ['firefox']
    ports = []
    languages = ['Python', 'C++', 'C', 'Fortran', 'BASIC', 'Brain F', 'Cobol', 'Assembly']
    nom_bts = {'copy':      lg('copy'),
               'cut':       lg('cut'),
               'past':      lg('past'),
               'cstyle':    lg('cstyle'),
               'news':      lg('news'),
               'new':       lg('new'),
               'open':      lg('open'),
               'exit':      lg('exit'),
               'print':     lg('print'),
               'save':      lg('save'),
               'saveas':    lg('saveas'),
               'undo':      lg('undo'),
               'redo':      lg('redo'),
               'search':    lg('search'),
               'word':      lg('word'),
               'pdf':       lg('pdf'),
               'about':     lg('about'),
               'struct':    lg('struct'),
               'close':     lg('close'),
               'savecopyas':lg('savecopyas'),
               'replace':   lg('replace'),
               'gotol':     lg('gotol'),
               'tasks':     lg('tasks'),
               'puces':     lg('puces'),
               'research':  lg('research'),
               'add_var':   lg('add_var'),
               'place_var': lg('place_var'),}


class Configurator2(Data):
    def cancel(self):
        self.tk.destroy()
        self.dialoging = False

    def info(self, _):
        showinfo(self.title, lg('MWSNS'))

    def IHM(self):
        if self.dialoging:
            return

        self.dialoging = True

        if self.mode_record:
            self.events.append({'command': 'IHM'})

        self.tk = Toplevel(self.master)
        self.tk.title(lg('Configurator'))
        self.tk.resizable(False, False)
        self.tk.transient(self.master)
        self.tk.protocol('WM_DELETE_WINDOW', self.cancel)
        self.tk.iconbitmap(self.ico['config'])

        style = ttk.Style(self.tk)
        style.configure('lefttab.TNotebook', tabposition='wn', background = BG, foreground = FG)

        self.onglets = ttk.Notebook(self.tk, style = 'lefttab.TNotebook')
        self.onglets.grid(row = 0, column = 0, columnspan = 3)
        
        self.menus = ScreenMenu(self.onglets, master = self.tk)
        self.onglets.add(text = lg('Menu'), child = self.menus.get())

        self.secu = ScreenSecu(self.onglets, self.browsers, master = self.tk)
        self.onglets.add(text = lg('Security'), child = self.secu.get())

        self.te = ScreenText(self.onglets, self.colors, self.fonts, master = self.tk)
        self.onglets.add(text = lg('Text'), child = self.te.get())

        self.pr = ScreenView(self.onglets, self.codages, self.langs, self.languages, master = self.tk)
        self.onglets.add(text = lg('view'), child = self.pr.get())

        self.fl = ScreenFile(self.onglets, master = self.tk)
        self.onglets.add(text = lg('File'), child = self.fl.get())

        self.mini = ScreenMinitel(self.onglets, self.ports, master = self.tk)
        self.onglets.add(text = lg('Minitel'), child = self.mini.get())

        self.racc = ScreenLinks(self.onglets, self.tk, (self.__keyb__, self.get_accelerator), self.ico['config'], path_prog = self.path_prog)
        self.onglets.add(text = lg('racc'), child = self.racc.get())

        self.clk = ScreenCustomize(self.onglets, self.master, self.nom_bts, mode = 'clk', ico = self.ico['config'], path_prog = self.path_prog)
        self.onglets.add(text = lg('menuclkr'), child = self.clk.get())

        self.bbt = ScreenCustomize(self.onglets, self.master, self.nom_bts, mode = 'bbt', ico = self.ico['config'], path_prog = self.path_prog)
        self.onglets.add(text = lg('menubts'), child = self.bbt.get())

        larg = 20
        Button(self.tk, text = lg('cancel'), command = self.cancel, width = larg).grid(row = 1, column = 0)
        Button(self.tk, text = lg('Apply'), command = self.apply, width = larg).grid(row = 1, column = 1)
        Button(self.tk, text = lg('OK'), command = self.validate_choice, width = larg).grid(row = 1, column = 2)

    def validate_choice(self):
        p = Progress(self.tk, title = lg('configurator'), tb = self.tb)
        p.set(50)

        menus = self.menus.results()
        secu = self.secu.results()
        te = self.te.results()
        pr = self.pr.results()
        fl = self.fl.results()
        mini = self.mini.results()

        #racc = self.racc.results()
        #clk = self.clk.results()
        #bbt = self.bbt.result()

        log = open(self.path_prog + '/log.txt', 'a')

        def optim(section, option, value):
            if value == True:
                value = '1'
            elif value == False:
                value = '0'
            else:
                value = str(value)

            try:
                write(section, option, value)
            except Exception as e:
                log.write(str(e) + '\n')

        for k, v in menus.items():
            optim(v['section'], v['option'], v['result'])
            p.step()

        for k, v in secu.items():
            optim(v['section'], v['option'], v['result'])
            p.step()

        for k, v in te.items():
            if v['option'] in ('bgd', 'bgl', 'fgd', 'fgl') and v['result'] in self.colors:
                optim(v['section'], v['option'], self.colors[v['result']])
            else:
                optim(v['section'], v['option'], v['result'])

            p.step()

        for k, v in pr.items():
            if v['option'] == 'lg':
                set_n_lg(self.langs[v['result']])
            else:
                optim(v['section'], v['option'], v['result'])

            p.step()

        for k, v in fl.items():
            if v['option'] == 'delay':
                optim(v['section'], v['option'], int(float(v['result']) * 60))
            else:
                optim(v['section'], v['option'], v['result'])

            p.step()

        for k, v in mini.items():
            optim(v['section'], v['option'], v['result'])
            p.step()

        log.close()

        self.act_colorc = pr[lg('coloration')]['result']

        p.stop()
        print('Restarting...')
        self.cancel()
        self.master.destroy()
        self.__start__()

    def apply(self):
        self.configurating = True
        self.savecopyas(forcing = True, name = 'backup.form')
        self.validate_choice()
        self.open(name = 'backup.form', forcing = True)


def htest():
    c = Configurator2()
    c.dialoging = False
    c.master = Tk()
    c.ico = {'config': PATH_PROG + '/image/icons/config.ico'}
    c.fonts = list(font.families())
    c.fonts.sort()
    c.__start__ = lambda : print('start')
    c.IHM()
    c.master.mainloop()

if __name__ == '__main__':
    from __init__ import *
