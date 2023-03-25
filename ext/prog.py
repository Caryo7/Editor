from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from confr import *
#import ext.compta as compta
#import ext.temps as temps

class File_Ext:
    def __init__(self, text):
        self.epath = ''
        self.esave = False
        self.text = text

    def ouvrir(self, titre='Ouvrir', fichier=['.txt', '.log'], repertoire='.'):
        fle = []
        for i in range(len(fichier)):fle.append(('', fichier[i]))
        n = askopenfilename(title=titre, initialdir=repertoire, filetypes=fle)
        if n:
            nb = len(n)-1
            while n[nb] != '.':nb -= 1
            assert n[nb:] in fichier
            try:
                f = open(n, 'r', encoding='UTF-8')
                self.text.delete('0.0', END)
                self.text.insert(END, f.read())
                f.close()
                self.epath = n
                self.esave = True
            except Exception as e:
                showerror(titre, e)
                self.esave = False
        else:
            self.esave = False

    def enregistrer(self):
        if not self.esave:self.enregistrer_sous()
        else:
            f = open(self.epath, 'w', encoding='UTF-8')
            f.write(self.text.get('0.0', END))
            f.close()
            self.esave = True

    def enregistrer_sous(self, titre='Enregistrer Sous', repertoire='.', fichier=['.txt', '.log']):
        fle = []
        for i in range(len(fichier)):fle.append(('', fichier[i]))
        n = askopenfilename(title=titre, initialdir=repertoire, filetypes=fle)
        if n:
            nb = len(n)-1
            while n[nb] != '.':nb -= 1
            assert n[nb:] in fichier
            try:
                f = open(n, 'w', encoding='UTF-8')
                f.write(self.text.get('0.0', END))
                f.close()
                self.epath = n
                self.esave = True
            except Exception as e:
                showerror(titre, e)
                self.esave = False
        else:
            self.esave = False

    def nouveau(self):
        self.text.delete('0.0', END)
        self.epath = ''
        self.esave = False

class Program:
    def import_ext(self):
        self.dict = {}
        self.exts = []#'compta']#, 'temps']

        #for i in self.exts:
        #self.dict['compta'] = {}
        #self.dict['compta']['module'] = compta
        #self.dict['compta']['file'] = File_Ext(self.text)

        #self.dict['temps'] = {}
        #self.dict['temps']['module'] = temps
        #self.dict['temps']['file'] = File_Ext(self.text)
        
    def draw_ext(self, bmenu):
        if bmenu:
            for j in self.exts:
                menu = Menu(self.menuext, tearoff=0)
                self.menuext.add_cascade(label=self.dict[j]['module'].menu[0], menu=menu)
                self.dict[j]['module'].menu.pop(0)
                for i in self.dict[j]['module'].menu:
                    if i == None:
                        menu.add_separator()
                    elif len(i) == 2:
                        menu.add_command(label=i[0], command=i[1])
                    else:
                        if i == 'Nouveau':menu.add_command(label=i, command=self.dict[j]['file'].nouveau)
                        elif i == 'Ouvrir':menu.add_command(label=i, command=self.dict[j]['file'].ouvrir)
                        elif i == 'Enregistrer':menu.add_command(label=i, command=self.dict[j]['file'].enregistrer)
                        elif i == 'Enregistrer sous':menu.add_command(label=i, command=self.dict[j]['file'].enregistrer_sous)
            self.menuext.add_separator()
        self.menuext.add_command(label=lg('AddExt'), command=self.add_ext)

    def add_ext(self):
        n = askopenfilename(title=lg('AddExt'), filetypes=[(lg('Extension'), '.ext')], initialdir='.')
        if n:
            n = n.replace('\\', '/')
            nb = len(n) - 1
            while n[nb] != '/':
                nb -= 1
            f1 = open(n, 'r', encoding='UTF-8')
            f2 = open('ext/' + n[nb:].replace('.ext', '.py'), 'w', encoding='UTF-8')
            f2.write(f1.read())
            f1.close()
            f2.close()
            showinfo(self.title, lg('MWSNS'))
