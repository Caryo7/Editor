from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
import sqlite3

class Bugs:
    def __init__(self):
        self.conn = sqlite3.connect('bugs_table.db')
        self.cur = self.conn.cursor()
        self.create_ifnotexists()
        self.read()

    def read(self):
        self.data = []
        for row in self.cur.execute('select * from bugs'):
            self.data.append(row)

    def create_ifnotexists(self):
        self.cur.execute('CREATE TABLE IF NOT EXISTS bugs(id INTEGER PRIMARY KEY AUTOINCREMENT, function TEXT, normal TEXT, error TEXT, idea TEXT)')
        self.conn.commit()

    def write(self, dic):
        self.cur.execute('INSERT INTO bugs(function, normal, error, idea) VALUES (?, ?, ?, ?)', (dic['fnct'], dic['normal'], dic['error'], dic['idea']))
        self.conn.commit()

    def get(self, item):
        self.read()
        return self.data[item]

    def table(self):
        self.read()
        return self.data

    def delete(self, item):
        self.read()
        try:
            nb = str(self.data[item][0])
            self.cur.execute('DELETE FROM bugs WHERE id == ?', nb)
            self.conn.commit()
        except IndexError:
            pass

    def remove(self, dic):
        try:
            self.cur.execute('DELETE FROM bugs WHERE id == ?', (str(dic['id'])))
            self.conn.commit()
        except IndexError:
            pass

    def close(self):
        self.conn.commit()
        self.conn.close()


class Win:
    def __init__(self):
        self.root = Tk()
        self.root.title('Gestionnaire de bugs')
        self.root.resizable(False, False)

        self.b = Bugs()

        self.bt_lst = ttk.Button(self.root, text = 'Liste', command = self.frame_lst)
        self.bt_lst.grid(row = 0, column = 0, padx = 5, pady = 5)

        self.bt_new = ttk.Button(self.root, text = 'Nouveau Bug', command = self.frame_new)
        self.bt_new.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.new_frame()

    def new_frame(self):
        try:
            self.master.destroy()
        except AttributeError:
            pass

        self.master = Frame(self.root)
        self.master.grid(row = 1, columnspan = 3, column = 0, padx = 0, pady = 0)
        self.bt_lst.config(stat = 'normal')
        self.bt_new.config(stat = 'normal')

    def frame_lst(self):
        self.new_frame()
        self.bt_lst.config(stat = 'disabled')

        scroll = ttk.Scrollbar(self.master, orient = 'vertical')
        tree = ttk.Treeview(self.master, columns = ('Id', 'Fonction', 'Normal', 'Erreur', 'Idées'), show = 'headings', height = 15, yscrollcommand = scroll.set, selectmode = 'browse')
        scroll.config(command = tree.yview)
        tree.place(x = 0, y = 0)

        tree.heading('Id', text = 'Id')
        tree.heading('Fonction', text = 'Fonction')
        tree.heading('Normal', text = 'Normal')
        tree.heading('Erreur', text = 'Erreur')
        tree.heading('Idées', text = 'Idées')

        tree.column('Id', width = 30)
        tree.column('Fonction', width = 250)
        tree.column('Normal', width = 250)
        tree.column('Erreur', width = 250)
        tree.column('Idées', width = 250)

        scroll.place(x = tree.winfo_reqwidth(), y = 0, height = tree.winfo_reqheight())
        self.master.config(width = tree.winfo_reqwidth() + scroll.winfo_reqwidth(), height = tree.winfo_reqheight())

        def clear():
            for x in tree.get_children():
                tree.delete(x)

        def insert():
            clear()
            for e in self.b.table():
                tree.insert('', 'end', values = e)

        def change(evt):
            s = tree.item(tree.selection())['values']
            dic = {'fnct': s[1], 'norm': s[2], 'prbm': s[3], 'idea': s[4], 'id': s[0]}
            self.frame_new(dic)

        def suppr(evt):
            s = tree.item(tree.selection())['values']
            self.b.remove({'id': s[0]})
            insert()

        insert()
        tree.bind('<Double-Button-1>', change)
        tree.bind('<Delete>', suppr)

    def frame_new(self, dic = {}):
        self.new_frame()
        self.bt_new.config(stat = 'disabled')
        font = ('Consolas', 12)

        Label(self.master, text = 'Fonction :', font = font).grid(row = 0, column = 0, padx = 5, pady = 5)
        Label(self.master, text = 'Temps normal :', font = font).grid(row = 1, column = 0, padx = 5, pady = 5)
        Label(self.master, text = 'Erreur :', font = font).grid(row = 2, column = 0, padx = 5, pady = 5)
        Label(self.master, text = 'Idées :', font = font).grid(row = 3, column = 0, padx = 5, pady = 5)

        fnct = Text(self.master, width = 30, height = 2, font = font)
        fnct.grid(row = 0, column = 1, padx = 5, pady = 5)
        if 'fnct' in dic:
            fnct.insert('end', dic['fnct'])

        norm = Text(self.master, width = 30, height = 4, font = font)
        norm.grid(row = 1, column = 1, padx = 5, pady = 5)
        if 'norm' in dic:
            norm.insert('end', dic['norm'])

        prbm = Text(self.master, width = 30, height = 4, font = font)
        prbm.grid(row = 2, column = 1, padx = 5, pady = 5)
        if 'prbm' in dic:
            prbm.insert('end', dic['prbm'])

        idea = Text(self.master, width = 30, height = 3, font = font)
        idea.grid(row = 3, column = 1, padx = 5, pady = 5)
        if 'idea' in dic:
            idea.insert('end', dic['idea'])

        def add():
            _dic = {'fnct': fnct.get('1.0', 'end'),
                   'normal': norm.get('1.0', 'end'),
                   'error': prbm.get('1.0', 'end'),
                   'idea': idea.get('1.0', 'end')}

            try:
                if dic != {}:
                    self.b.remove(dic)
    
                self.b.write(_dic)
    
                if dic == {}:
                    fnct.delete('1.0', 'end')
                    prbm.delete('1.0', 'end')
                    norm.delete('1.0', 'end')
                    idea.delete('1.0', 'end')
            except:
                showerror('Sauvegarde', 'Une erreur s\'est produite !')

        Button(self.master, text = 'Valider', command = add).grid(row = 4, column = 0, padx = 5, pady = 5, columnspan = 2)

    def Generate(self):
        self.master.mainloop()


if __name__ == '__main__':
    w = Win()
    w.Generate()
