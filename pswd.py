#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.simpledialog import *
import sqlite3, hashlib, inspect, os

PATH_PROG = os.path.abspath(os.getcwd())

from tooltip import *
from confr import *

class Password:
    askpwd = False

    def __init__(self, cmd = None, tk = None):
        if not tk:
            self.master = Tk()
        else:
            self.master = Toplevel(tk)
            self.master.transient(tk)

        self.master.focus()

        self.cmd = cmd
        self.master.iconbitmap(PATH_PROG + '/image/password.ico')
        self.master.title(lg('Administrator'))
        menu = Menu(self.master)
        self.master['menu'] = menu
        menu.add_command(label = lg('add'), command = self.append)
        ToolTip(menu, '''En pressant ce bouton, vous activez la demande de nouveau compte administrateur.
Voici les étapes pour la création d\'un nouveau compte :
1. Entrez les données de connexion pour un compte administrateur déjà existant
2. Avant d'appuyer sur Entrée ou de cliquer sur Connexion, cliquez sur le bouton Ajouter du menu
3. Connectez vous
4. Une fenêtre apparaitera et vous demandera un identifiant ainsi que le mot de passe
5. Une fois que vous aurez tout valider, en cliquant sur Valider, le nouvel utilisateur sera ajouté''')
        Label(self.master, text = lg('username')).grid(row = 0, column = 0)
        Label(self.master, text = lg('password')).grid(row = 1, column = 0)
        self.usern = StringVar(master = self.master)
        self.usern.set('ADMIN')
        e = Entry(self.master, textvariable = self.usern, width = 20)
        e.grid(row = 0, column = 1)
        ToolTip(e, lg('type_username'), wraplength = 270)
        self.pswd = StringVar(master = self.master)
        p = Entry(self.master, textvariable = self.pswd, width = 20, show = '*')
        p.grid(row = 1, column = 1)
        p.focus()
        ToolTip(p, lg('type_pswd'), wraplength = 270)
        b = Button(self.master, text = lg('Connexion'), command = self.connect)
        b.grid(row = 2, column = 0)
        ToolTip(b, lg('click_connect'), wraplength = 270)
        self.master.bind_all('<Return>', self.connect)

        self.master.protocol('WM_DELETE_WINDOW', self.Quitter)
        if not tk:
            self.master.mainloop()

    def append(self):
        self.askpwd = True
        self.master.unbind_all('<Return>')
        showinfo(lg('Administrator'), lg('window_newuser'))
        self.master.bind_all('<Return>', self.connect)

    def Quitter(self):
        self.master.destroy()

    def connect(self, evt = None):
        if self.get_users():
            if self.askpwd:
                self.append_password()
            else:
                self.master.destroy()
            self.cmd()
        else:
            self.master.unbind_all('<Return>')
            showerror(lg('Administrator'), lg('err_usn_pswd'))
            self.master.bind_all('<Return>', self.connect)

    def get_users(self):
        user = self.usern.get()
        pswd = self.pswd.get().encode()
        ha = hashlib.sha512()
        ha.update(pswd)
        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        r = cur.execute('select * from password')
        for row in r:
            if row[1] == user and row[2] == str(ha.hexdigest()) and row[3] == 0:
                conn.close()
                return True
        conn.close()
        return False

    def append_password(self):
        self.zak = Toplevel(master = self.master)
        self.zak.transient(self.master)
        self.zak.title(lg('New_User'))
        
        self.username = StringVar(master = self.master)
        self.password = StringVar(master = self.master)
        self.passwordc = StringVar(master = self.master)

        Label(self.zak, text = lg('new_compte'), font = ('Consolas', 16, 'bold')).place(x = 50, y = 10)
        Label(self.zak, text = lg('username'), font = ('Consolas', 14)).place(x = 10, y = 60)
        Label(self.zak, text = lg('password'), font = ('Consolas', 14)).place(x = 10, y = 90)
        Label(self.zak, text = lg('confirmation'), font = ('Consolas', 14)).place(x = 10, y = 120)
        Entry(self.zak, textvariable = self.username, width = 20, font = ('Consolas', 14)).place(x = 175, y = 60)
        Entry(self.zak, textvariable = self.password, width = 20, font = ('Consolas', 14), show = '*').place(x = 175, y = 90)
        Entry(self.zak, textvariable = self.passwordc, width = 20, font = ('Consolas', 14), show = '*').place(x = 175, y = 120)
        Button(self.zak, text = lg('OK'), command = self.validate).place(x = 50, y = 160)
        self.zak.bind_all('<Return>', lambda evt: self.validate())
        self.zak.geometry('425x200')
        self.zak.mainloop()

    def validate(self):
        if self.password.get() != self.passwordc.get():
            showerror(lg('new_user'), lg('pswd_nomatch'))
            return

        ha = hashlib.sha512()
        ha.update(self.password.get().encode())
        password = str(ha.hexdigest())

        conn = sqlite3.connect('users.db')
        cur = conn.cursor()
        cur.execute('INSERT INTO password(username, password, allow) VALUES (?, ?, ?)', (self.username.get(), password, 0))
        conn.commit()
        conn.close()

        self.zak.destroy()
        self.master.destroy()
            

if __name__ == '__main__':
    Password()
