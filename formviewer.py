from compress import *
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import os

PATH_PROG = os.getcwd()

class Main:
    file = ''
    files = {}

    def __init__(self):
        self.master = Tk()
        self.master.title('FORM ZIP VIEWER')
        self.master.resizable(False, False)
        self.master.protocol('WM_DELETE_WINDOW', self.Quitter)

        scroll = ttk.Scrollbar(self.master, orient = 'vertical')
        self.tree = ttk.Treeview(self.master, column = ('icon', 'file', 'date', 'crc'), show = 'headings', yscrollcommand = scroll.set, height = 20, selectmode = 'browse')
        self.tree.place(x = 0, y = 0)
        scroll.place(x = self.tree.winfo_reqwidth() - scroll.winfo_reqwidth(), y = 0, height = self.tree.winfo_reqheight())
        scroll.config(command = self.tree.yview)

        self.tree.heading('icon', text = '')
        self.tree.heading('file', text = 'Fichier')
        self.tree.heading('date', text = 'Dernière modification')
        self.tree.heading('crc', text = 'CRC')

        self.tree.column('icon', width = 30)
        self.tree.column('file', width = 400)
        self.tree.column('date', width = 150)
        self.tree.column('crc', width = 200)

        self.master.geometry(str(self.tree.winfo_reqwidth() + scroll.winfo_reqwidth() + 10) + 'x' + str(self.tree.winfo_reqheight()))

        self.menubar = Menu(self.master)
        self.master['menu'] = self.menubar
        menufichier = Menu(self.menubar, tearoff = 0)
        self.menubar.add_cascade(label = 'Fichier', menu = menufichier)
        menufichier.add_command(label = 'Nouveau', stat = 'normal', command = self.new, accelerator = 'Ctrl + N')
        menufichier.add_command(label = 'Ouvrir', stat = 'normal', command = self.open, accelerator = 'Ctrl + O')
        menufichier.add_separator()
        menufichier.add_command(label = 'Enregistrer', stat = 'normal', command = self.save, accelerator = 'Ctrl + S')
        menufichier.add_command(label = 'Enregistrer sous', stat = 'normal', command = self.saveas, accelerator = 'Ctrl + Shift + S')
        menufichier.add_separator()
        menufichier.add_command(label = 'Fermer', stat = 'normal', command = self.close, accelerator = 'Ctrl + W')
        menufichier.add_command(label = 'Quitter', stat = 'normal', command = self.Quitter, accelerator = 'Ctrl + Q ou Alt + F4')

        self.tree.bind('<Control-n>', self.new)
        self.tree.bind('<Control-o>', self.open)
        self.tree.bind('<Control-s>', self.save)
        self.tree.bind('<Control-S>', self.saveas)
        self.tree.bind('<Control-w>', self.close)
        self.tree.bind('<Control-q>', self.Quitter)

        self.tree.bind('<Double-Button-1>', self.edit)

    def edit(self, evt):
        selected = self.tree.item(self.tree.selection())['values']
        os.popen('notepad ' + PATH_PROG + '/temp/' + selected[1])

    def clear(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

    def insert(self, name, data):
        icon = data[1] if isinstance(data[1], str) else data[1].decode()
        date = data[2] if isinstance(data[2], str) else data[2].decode()
        crc = data[3] if isinstance(data[3], str) else data[3].decode()
        self.tree.insert('', 'end', values = [icon, name, date, crc])
        try:
            os.mkdir(PATH_PROG + '/temp')
        except Exception:
            pass

        f = open(PATH_PROG + '/temp/' + name, 'wb')
        f.write(data[0])
        f.close()
        self.files[name] = data

    def new(self, evt = None):
        self.close()

    def open(self, evt = None):
        a = askopenfilename(title = 'Ouvrir', filetypes = [('FORM FILES', '*.FORM')])
        if a:
            try:
                self.clear()
                f = CmpdFile(a, mode = 'r')
                for file in f.namelist():
                    self.insert(file, f.read(file))

                f.close()
                self.file = a

            except Exception as e:
                showerror('VIEWER', str(e))

    def save(self, evt = None):
        z = CmpdFile(self.file, mode = 'w')
        for name, data in self.files.items():
            f = open(PATH_PROG + '/temp/' + name, 'rb')
            z.write(name, f.read())
            f.close()
        z.close()

    def saveas(self, evt = None):
        a = asksaveasfilename(title = 'Enregistrer sous', filetypes = [('FORM FILES', '*.FORM')])
        if a:
            self.file = a
            self.save()

    def close(self, evt = None):
        self.file = ''
        self.files = {}
        self.clear()

    def Generate(self):
        self.master.mainloop()

    def Quitter(self):
        self.master.destroy()

if __name__ == '__main__':
    a = Main()
    a.Generate()
