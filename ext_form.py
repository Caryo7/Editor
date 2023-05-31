#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
import zipfile as zp
<<<<<<< Updated upstream
=======
import os
import hashlib

PATH_PROG = os.path.abspath(os.getcwd())

class ExForm1:
    @classmethod
    def open(self, path_prog, name):
        try:
            f = zp.ZipFile(name, 'r')
            result = f.read('data.txt').decode(get_encode())
            lst_tag = str(f.read('tags.csv').decode(get_encode())).split('\n')
            lst_tags = []
            for i in lst_tag:
                i = i.replace('\r', '')
                if i != '':
                    lst_tags.append(i.split(','))
            f.close()
            return (result, lst_tags)

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [])

    @classmethod
    def save(self, path_prog, file, data, lst_tags):
        try:
            z = zp.ZipFile(file, 'w')
            f = z.open('data.txt', 'w')
            f.write(data)
            f.close()
            f = z.open('tags.csv', 'w')
            for i in lst_tags:
                f.write(str(','.join(i) + '\n').encode())
            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


class ExForm2:
    @classmethod
    def open(self, path_prog, name):
        try:
            f = zp.ZipFile(name, 'r')
            result = f.read('data.txt').decode(get_encode())
            lst_tag = str(f.read('tags.csv').decode(get_encode())).split('\n')
            lst_tags = []
            for i in lst_tag:
                i = i.replace('\r', '')
                if i != '':
                    lst_tags.append(i.split(','))
        
            meta = {}
            meta_data = f.read('meta.ini').decode(get_encode())
            meta_data = meta_data.replace('\r', '\n')
            for i in meta_data.split('\n'):
                if i != '':
                    key, value = i.split('-')
                    key = key.replace('"', '')
                    value = value.replace('"', '')
                    meta[key] = value
        
            f.close()
            return (result, lst_tags, meta)

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [], {})

    @classmethod
    def save(self, path_prog, file, data, lst_tags, meta):
        try:
            z = zp.ZipFile(file, 'w')
            f = z.open('data.txt', 'w') 
            f.write(data)
            f.close()
            f = z.open('tags.csv', 'w')
            for i in lst_tags:
                f.write(str(','.join(i) + '\n').encode())
            f.close()
            f = z.open('meta.ini', 'w')
            if 'version' not in meta.keys():
                meta['version'] = 'Form_2.0'
            if 'time' not in meta.keys():
                meta['time'] = '0'
    
            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"\n').encode(get_encode()))
            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()

    @classmethod
    def write_meta(self, meta, path_prog):
        try:
            z = zp.ZipFile(file, 'w')
            f = z.open('meta.ini', 'w')
            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"\n').encode(get_encode()))
            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


def askpswd(pwdh, cmd, master):
    zak = Toplevel(master)
    zak.iconbitmap(PATH_PROG + '/image/icons/password.ico')
    zak.transient(master)
    zak.title(lg('Password'))
    zak.resizable(False, False)
    Label(zak, text = lg('password')).place(x = 10, y = 10)
    pwd = StringVar(master = master)
    e = Entry(zak, textvariable = pwd, show = '•')
    e.place(x = 10, y = 40)
    zak.wm_attributes('-topmost')
    e.focus()
    
    def command():
        ha = hashlib.sha512()
        ha.update(pwd.get().encode())
        if str(ha.hexdigest()) == pwdh:
            zak.focus()
            zak.destroy()
            cmd()

        else:
            showerror(lg('password'), lg('err_pswd'))
            zak.focus()
            e.focus()

    def commande(evt):
        command()

    e.bind('<Return>', commande)
    Button(zak, text = lg('OK'), command = command).place(x = 10, y = 70)
    zak.geometry('160x120')

>>>>>>> Stashed changes

class ExForm:
    def open(self, name):
        result = None
        f = zp.ZipFile(name, 'r')
        if get_encrypted():
            result = self.decrypt(f.read('data.txt').decode(get_encode()))
        else:
            result = f.read('data.txt').decode(get_encode())
        self.text.insert(END, result)
        lst_tag = str(f.read('tags.csv').decode(get_encode())).split('\n')
        for i in lst_tag:
            self.lst_tags.append(i.split(','))
        self.write_tags()
        f.close()

    def save(self, file, data, cryptage = True):
        z = zp.ZipFile(file, 'w')
        f = z.open('data.txt', 'w')
        if get_encrypted() and cryptage:
            f.write(self.encrypt(data))
        else:
            f.write(data.encode(get_encode()))
        f.close()
        f = z.open('tags.csv', 'w')
        for i in self.lst_tags:
            f.write(str(','.join(i) + '\n').encode())
        f.close()
        z.close()        

if __name__ == '__main__':
    from __init__ import *
