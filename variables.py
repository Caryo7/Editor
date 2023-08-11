from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.simpledialog import *

from confr import *

class TableGUI:
    spliter = b'\x01'.decode(get_encode())

    def start_vars(self, mode = 'gestion'):
        assert mode in ('gestion', 'choix')
        self.mode = mode

        self.tvars = Toplevel(self.master)
        self.tvars.transient(self.master)
        self.tvars.title('Table des variables') ###############################
        self.tvars.resizable(False, False)
        try:
            self.tvars.iconbitmap(self.ico['settings'])
        except:
            pass

        scroll = ttk.Scrollbar(self.tvars, orient = 'vertical')
        self.tree = ttk.Treeview(self.tvars, columns = ('name', 'data'), show = 'headings', height = 20, yscrollcommand = scroll.set, selectmode = 'browse')
        scroll.config(command = self.tree.yview)
        scroll.place(x = 10 + self.tree.winfo_reqwidth(), y = 40, height = self.tree.winfo_reqheight())
        self.tree.place(x = 10, y = 40)
        self.tree.heading('name', text = 'Name') ##############
        self.tree.heading('data', text = 'Data') ##############
        self.tree.column('name', width = 100)
        self.tree.column('data', width = 300)
        self.tree.bind('<<TreeviewSelect>>', self.itemSelected)
        if mode == 'choix':
            self.tree.bind('<Double-Button-1>', self.choix)

        self.tvars.geometry(str(self.tree.winfo_reqwidth() + scroll.winfo_reqwidth() + 10) + 'x' + str(50 + self.tree.winfo_reqheight()))
        Button(self.tvars, text = 'Ajouter', command = self.append).place(x = 10, y = 10) ################
        self.bpop = Button(self.tvars, text = 'Enlever', command = self.remove, stat = 'disabled') #################
        self.bpop.place(x = 120, y = 10)
        self.bconf = Button(self.tvars, text = 'Configurer', command = self.config, stat = 'disabled') #################
        self.bconf.place(x = 200, y = 10)
        self.buns = Button(self.tvars, text = 'Déséléctionner', command = self.unselect, stat = 'disabled') ##################
        self.buns.place(x = 320, y = 10)

        self.update()

    def unselect(self):
        self.tree.selection_remove(*self.tree.selection())

    def choix(self, evt = None):
        valeur = self.tree.item(self.tree.selection())['values'][1]
        self.text.insert('insert', b'\x01'.decode(get_encode()) + valeur + b'\x01'.decode(get_encode()))
        self.tvars.destroy()

    def append(self):
        zak = Toplevel(self.tvars)
        zak.transient(self.tvars)
        zak.title('Ajouter') #################
        zak.resizable(False, False)

        Label(zak, text = 'Nom', font = ('Consolas', 14)).grid(row = 0, column = 0, sticky = 'e', padx = 5, pady = 5) #################
        Label(zak, text = 'Valeur', font = ('Consolas', 14)).grid(row = 1, column = 0, sticky = 'e', padx = 5, pady = 5) ############
        name = StringVar(master = zak)
        value = StringVar(master = zak)
        Entry(zak, textvariable = name, width = 15, font = ('Courier', 13)).grid(row = 0, column = 1, sticky = 'w', padx = 5, pady = 5)
        e = Entry(zak, textvariable = value, width = 15, font = ('Courier', 13))
        e.grid(row = 1, column = 1, sticky = 'w', padx = 5, pady = 5)

        def add(evt = None):
            if name.get() != '':
                self.variables[name.get()] = value.get()
                zak.destroy()
                self.update()
                last = self.tree.get_children()[-1]
                self.tree.selection_add(last)

            else:
                showerror('', 'Merci de mettre un nom pour la variable !') #############################

        e.bind('<Return>', add)
        Button(zak, text = 'OK', command = add, width = 30).grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 7) #######################

    def getTextValueVars(self, text):
        data = text.split(self.spliter)
        i = 1
        while True:
            try:
                data[i] = self.variables[data[i]]
            except IndexError:
                break
            except KeyError:
                showerror('', 'Pas de variable au nom de ' + str(data[i])) #######################

            i += 2

        return self.spliter.join(data)

    def getBrutValueVars(self, text):
        data = text.split(self.spliter)
        i = 1
        while True:
            try:
                for k, v in self.variables.items():
                    if data[i] == v:
                        data[i] = k
                        break

            except IndexError:
                break

            i += 2

        return self.spliter.join(data)

    def append_var(self):
        self.start_vars(mode = 'choix')
        self.append()

    def place_variable(self):
        if self.variables != {}:
            self.start_vars(mode = 'choix')
        else:
            showinfo('', 'No variables created !') ###################

    def remove(self):
        index = self.tree.selection()
        selected = self.tree.item(index)['values']
        self.variables.pop(selected[0])

        self.tree.delete(index)

    def config(self):
        index = self.tree.selection()
        selected = self.tree.item(index)['values']
        new_data = askstring('Définition', 'Quelle valeur voulez vous donner à la variable ' + str(selected[0]) + ' ?') #####################
        self.variables[selected[0]] = new_data

        self.update()

    def itemSelected(self, evt = None):
        if self.tree.selection():
            self.bpop.config(stat = 'normal')
            self.bconf.config(stat = 'normal')
            self.buns.config(stat = 'normal')
        else:
            self.bpop.config(stat = 'disabled')
            self.bconf.config(stat = 'disabled')
            self.buns.config(stat = 'disabled')

    def clear(self):
        for x in self.tree.get_children():
            self.tree.delete(x)

    def update(self):
        self.clear()
        for name, value in self.variables.items():
            self.tree.insert('', 'end', values = [name, value])

        self.itemSelected()
        
if __name__ == '__main__':
    from __init__ import *
