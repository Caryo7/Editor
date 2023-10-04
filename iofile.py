from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from confr import *
from threading import Thread
import time
import zipfile
import sys
import hashlib

from ext_form import *
from ext_file import *
from ocr import *

class Auto_Save(Thread):
    def __init__(self, main_self):
        Thread.__init__(self)
        self.intertime = int(get_inter_time())
        self.main_self = main_self
        
    def run(self):
        self.main_self.add_task(code='AutoSave', time=time.time(), desc='MAIN_LOOP\nThis task is running to save your work at a frequency. You can set it on the configuration page (Option -> Options -> Autosave -> Frequency). You can\'t stop it.')
        while True:
            if self.main_self.programme_termine:
                break
            time.sleep(self.intertime)
            if not not(self.main_self.savedd) and not(self.main_self.saved):
                self.main_self.save()
            else:
                f = open(self.main_self.path_prog + '/' + get_autosave_path(), 'w', encoding='UTF-8')
                f.write(self.main_self.text.get('0.0', END))
                f.close()


class File(ExForm, ExText):
    def __file__(self):
        self.path = 'untitled.x'
        self.saved = False
        self.savedd = False
        self.nofileopened = True
        self.ast = Auto_Save(self)

        self.listext = ['.xml', '.mxml', '.txt', '.log', '.py', '.pyw', '.html', '.htm', '.php', '.ino', '.h', '.c', '.cpp', '.cc', '.bat', '.bas', '.ba', '.bf', '.f', '.f90', '.f95', '.eq', '.ini', '.inf', '.bu']
        self.listexta = ['.zip', '.PADS', '.form', '.dat', '.exe', '.7z', '.tar', '.gz', '.sqlite', '.mysql']
        self.ttext = [(lg('ttfpec'), '*.form *.bu *.txt *.log *.html *.htm *.xml *.mxml *.php *.ino *.c *.h *.cpp *.cc *.bat *.bas *.ba *.py *.pyw *.f *.f90 *.f95 *.bf *.eq *.ini *.inf *.pdf *.jpg *.png'),
                      (lg('Formf'), '*.form'),
                      (lg('BU'), '*.bu'),
                      (lg('alf'), '*.*'),
                      (lg('TF'), '*.txt *.log *.dat'),
                      (lg('dbf'), '*.db *.sqlite *.mysql *.xml *.json'),
                      (lg('zipf'), '*.zip *.tar *.gz *.exe *.7z'),
                      (lg('exef'), '*.exe'),
                      (lg('HF'), '*.html *.htm *.php'),
                      (lg('XMLF'), '*.xml *.mxml'),
                      (lg('AF'), '*.ino *.h *.c *.cpp'),
                      (lg('CF'), '*.cpp *.c *.h *.cc'),
                      (lg('PF'), '*.py *.pyw'),
                      (lg('BF'), '*.bat'),
                      (lg('BAF'), '*.bas *.ba'),
                      (lg('FF'), '*.f *.f90 *.f95'),
                      (lg('BRF'), '*.bf'),
                      (lg('EF'), '*.eq'),
                      (lg('WF'), '*.docx *.doc'),
                      (lg('sysf'), '*.PADS'),
                      (lg('if'), '*.ini *.inf'),
                      (lg('floppyf'), '*.floppy'),
                      (lg('pdff'), '*.pdf *.pdff'),
                      (lg('imgf'), '*.jpg *.png'),
                      ]

        self.meta = {}
        self.variables = {}
        self.begin_time = time.time()
        self.photos = []

    def open_recent(self, name):
        self.open(evt = None, name = name)

    def open_this(self, args):
        if len(args) > 1:
            self.open(evt = None, name = args[1])

    def ext(self, name):
        if '.' not in name:
            return ''

        i = len(name) - 1
        while name[i] != '.':i -= 1
        return name[i:]

    def askopen(self):
        n = askopenfilename(title=lg('Open'), initialdir='.', filetypes=self.ttext, master = self.master)
        return n

    def asksaveas(self, path = '', exts = None):
        if not exts:
            exts = self.ttext.copy()

        n = asksaveasfilename(title=lg('Save_as'), initialdir='.', filetypes=exts, master = self.master)
        return n

    def ask_settings(self):
        if self.dialoging:
            return

        self.dialoging = True

        if self.mode_record:
            self.events.append({'command': 'settings'})

        zak = Tk()
        zak.iconbitmap(self.ico['config'])
        zak.transient()
        zak.title(lg('meta_informations'))
        zak.resizable(False, False)

        tree = ttk.Treeview(zak, columns = (1, 2), show = 'headings')
        tree.pack()

        tree.column(1, width = 100)
        tree.column(2, width = 200)
        tree.heading(1, text = lg('key'))
        tree.heading(2, text = lg('value'))

        def update(self):
            for x in tree.get_children():
                tree.delete(x)
            for key, value in self.meta.items():
                tree.insert('', 'end', value = (key, value))

        def ask_hash(v):
            rt = Toplevel()
            rt.transient()
            rt.iconbitmap(self.ico['config'])
            rt.title('SHA512')
            rt.resizable(False, False)
            Label(rt, text = lg('text')).place(x = 10, y = 10)
            t = StringVar()
            e = Entry(rt, textvariable = t)
            e.place(x = 10, y = 40)
            e.focus()
            def rtn():
                ha = hashlib.sha512()
                ha.update(t.get().encode())
                v.set(str(ha.hexdigest()))
                rt.focus()
                rt.destroy()

            def cmd(evt):
                rtn()

            e.bind('<Return>', cmd)

            Button(rt, text = lg('ok'), command = rtn).place(x = 10, y = 70)
            rt.geometry('200x110')

        def ask_meta(self, type_):
            assert type_ in ('change', 'append')
            tk = Toplevel()
            tk.iconbitmap(self.ico['config'])
            tk.title(lg('settings'))
            tk.resizable(False, False)
            Label(tk, text = lg('key')).place(x = 10, y = 10)
            k = StringVar()
            k.set(tree.item(tree.selection())['values'][0] if type_ == 'change' else '')
            Entry(tk, textvariable = k, stat = 'disabled' if type_ == 'change' else 'normal').place(x = 10, y = 40)
            Label(tk, text = lg('value')).place(x = 10, y = 70)
            v = StringVar()
            v.set(tree.item(tree.selection())['values'][1] if type_ == 'change' else '')
            Entry(tk, textvariable = v).place(x = 10, y = 100)
            Button(tk, text = 'SHA512', width = 6, command = lambda : ask_hash(v)).place(x = 150, y = 100)
            def valide(self):
                if k.get() in self.meta and type_ == 'append':
                    showerror(lg('settings'), lg('tiaakwtn'))
                else:
                    self.meta[k.get()] = v.get()
                    self.saved = False
                    self.master.title('* ' + self.title + ' - ' + self.path + ' *')
                    update(self)
                    tk.destroy()

            Button(tk, text = lg('ok'), command = lambda : valide(self)).place(x = 10, y = 130)
            tk.bind('<Return>', lambda e: tk.destroy())
            tk.geometry('230x170')

        def append(self):
            ask_meta(self, 'append')

        def change(self):
            ask_meta(self, 'change')

        def remove(self):
            del self.meta[tree.item(tree.selection())['values'][0]]
            self.saved = False
            self.master.title('* ' + self.title + ' - ' + self.path + ' *')
            update(self)

        def popup(evt, self):
            pp = Menu(zak, tearoff = 0)
            pp.add_command(label = lg('delete'), command = lambda : remove(self))
            pp.add_command(label = lg('modifier'), command = lambda : change(self))
            pp.add_command(label = lg('append'), command = lambda : append(self))
            pp.tk_popup(evt.x_root, evt.y_root)

        tree.bind('<Button-3>', lambda evt: popup(evt, self))
        update(self)

        def demander_fermeture(evt = None):
            zak.focus()
            zak.destroy()
            self.text.focus()
            self.dialoging = False

        zak.protocol('WM_DELETE_WINDOW', demander_fermeture)

    def show_info(self):
        if self.mode_record:
            self.events.append({'command': 'meta_info'})

        zak = Toplevel(self.master)
        zak.transient(self.master)
        zak.iconbitmap(self.ico['config'])
        zak.title(lg('Settings'))
        zak.resizable(False, False)
        fnt = ('Consolas', 12)

        Label(zak, text = 'Informations du fichier', font = ('Consolas', 16)).grid(row = 0, column = 0, columnspan = 2, pady = 12, padx = 20)

        dic =  {'Type de fichier :': '',
                'Créateur :': self.title,
                'Mots clé :': '',
                'Variables :': len(self.variables)}

        def tryer(dic, k, v):
            try:
                dic[k] = self.meta[v]
                return dic
            except:
                return dic

        dic = tryer(dic, 'Auteur :', 'author')
        dic = tryer(dic, 'Sujet', 'subject')
        t = ''
        try:
            tps = int(self.meta['time'])
            hours = int(tps // 3600)
            tps -= hours * 3600
            minutes = int(tps // 60)
            tps -= minutes * 60
            secondes = tps
            t = ''
            if hours > 0:
                t += str(hours) + ' Heures '
            if minutes > 0:
                t += str(minutes) + ' Minutes '
            if secondes > 0:
                t += str(secondes) + ' Secondes'

            dic['Temps de travail :'] = t
        except:
            pass

        row = 1
        for k, v in dic.items():
            if v != '':
                Label(zak, text = k, font = fnt).grid(row = row, column = 0, padx = 5, pady = 5, sticky = 'e')
                Label(zak, text = v, font = fnt).grid(row = row, column = 1, padx = 5, pady = 5, sticky = 'w')
                row += 1

    def importer(self, file = None, ask_info = True, forcing = False):
        if not self.dialoging or forcing:
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'import', 'file': file, 'forcing': forcing, 'ask_info': ask_info})

            if not file:
                file = askopenfilename(title = lg('import_pdf'), initialdir = '.', filetypes = [(lg('pdff'), '*.pdf *.pdff'), (lg('imgf'), '*.jpg *.png')], master = self.master)

            if file:
                if ask_info:
                    if askyesno(lg('import_pdf'), lg('warn_import_pdf')):
                        pass#############################################################################################################################################################
                        # Pour la compilation, il est impossible de mettre le module keras_ocr. Donc, pas de reconnaissance de caractères possible !
                        #lunch_ocr(self.master, self.text, file, self.path_prog)
                    else:
                        self.open(name = file, forcing = True, ask_info = False)
                        return
                else:
                    pass#################################################################################################################################################################
                    # Pour la compilation, il est impossible de mettre le module keras_ocr. Donc, pas de reconnaissance de caractères possible !
                    #lunch_ocr(self.master, self.text, file, self.path_prog)

            self.dialoging = False

    def update_time(self, name = None):
        if not name:
            name = self.path

        end = int(time.time())
        temps = end - self.begin_time
        try:
            self.meta['time'] = str(int(self.meta['time']) + temps)
            self.meta['cursor'] = str(self.get_index())
            if self.ext(name) in self.listexta:
                ExForm.write_meta(self)

        except KeyError:
            pass

    def open(self, evt=None, name = None, forcing = False, ask_info = True):
        if not self.dialoging or forcing:
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'open', 'evt': evt, 'name': name, 'forcing': forcing, 'ask_info': ask_info})

            if not name:
                name = self.askopen()

            if not self.nofileopened:
                self.fermer()

            if name:
                try:
                    try:
                        self.events[-1]['name'] = name
                    except:
                        pass

                    self.update_time()
                    self.stat_form_infos(False)
                    self.stat_text(True)
                    self.clear_text()
                    self.meta = {}
                    self.variables = {}
                    self.master.focus()
                    if self.ext(name) in self.listext:
                        ExText.open(self, name)
                        if self.ext(name) == '.bu':
                            self.new(forcing = True, mode_clear = True)
                            self.master.title('* ' + self.title + ' - ' + self.path + ' *')
                            self.saveas(forcing = True)

                    elif self.ext(name) in self.listexta:
                        ExForm.open(self, name)
                        self.begin_time = int(time.time())

                    elif self.ext(name) == '.pdf':
                        if ask_info:
                            if askyesno(lg('import_pdf'), lg('warn_open_pdf')):
                                self.begin_pdf_analyse(name)
                            else:
                                self.importer(name, ask_info = False, forcing = True)
                        else:
                            self.begin_pdf_analyse(name)

                    elif self.ext(name) in ('.jpg', '.png'):
                        self.importer(name)

                except FileNotFoundError:
                    self.saved = False
                    self.savedd = False
                    self.path = 'untitled.x'
                    showerror(self.title, lg('FNF'))

            self.dialoging = False
            self.updateDiscordStatut()

    def save(self, evt=None, forcing = False):
        if not self.dialoging or forcing:
            if self.mode_record:
                self.events.append({'command': 'save', 'evt': evt, 'forcing': forcing})

            if not self.savedd:
                self.saveas()

            elif not self.saved:
                if self.ext(self.path) not in self.listexta:
                    ExText.save(self, self.path, self.get_text(save = True))
                else:
                    ExForm.save(self, self.path, self.get_text(save = True), self.meta, self.variables)

                self.saved = True
                self.master.title(self.title + ' - ' + self.path)
                
    def saveas(self, evt = None, name = None, forcing = False, path = ''):
        if not self.dialoging or forcing:
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'saveas', 'evt': evt, 'name': name, 'forcing': forcing, 'path': path})

            if not name:
                name = self.asksaveas(path = path)

            if name:
                if '.' not in name:
                    name += '.form'

                self.path = name

                if self.ext(self.path) not in self.listexta:
                    ExText.save(self, self.path, self.get_text(save = True))
                else:
                    ExForm.save(self, self.path, self.get_text(save = True), self.meta, self.variables, mode_saveas = True)
                    self.menufichier.entryconfig(lg('settings'), stat = 'normal')

                try:
                    self.events[-1]['name'] = name
                except:
                    pass

                self.saved = True
                self.savedd = True
                self.add_f(self.path)
                self.master.title(self.title + ' - ' + self.path)

            else:
                self.saved = False
                self.savedd = False
                self.path = 'untitled.x'
                self.master.title('* ' + self.title + ' - ' + self.path + ' *')

            self.dialoging = False
            self.updateDiscordStatut()
            
    def savecopyas(self, evt=None, forcing = False, name = None):
        if not self.dialoging or forcing:
            self.dialoging = True
            if self.mode_record:
                self.events.append({'command': 'savecopyas', 'evt': evt, 'forcing': forcing})

            if not name:
                name = asksaveasfilename(title=lg('Save_copy_as'), initialdir='.', filetypes=self.ttext)

            if name:
                if self.ext(name) not in self.listexta:
                    ExText.save(self, name, self.get_text(save = True))
                else:
                    ExForm.save(self, name, self.get_text(save = True), self.meta, self.variables, mode_saveas = True)

            self.dialoging = False
            
    def new(self, evt=None, forcing = False, mode_clear = False):
        if not self.dialoging or forcing:
            if self.mode_record:
                self.events.append({'command': 'new', 'evt': evt, 'forcing': forcing, 'mode_clear': mode_clear})

            if not mode_clear:
                self.fermer()
                self.stat_text(True)
                self.text.delete('0.0', END)

            self.saved = False
            self.begin_time = int(time.time())
            self.savedd = False
            self.nofileopened = False
            self.path = 'Untitled.x'
            self.master.title(self.title + ' - ' + self.path)
            self.update_line_numbers()
            self.meta = {}
            self.variables = {}
            self.updateDiscordStatut()


if __name__ == '__main__':
    from __init__ import *
