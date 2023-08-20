#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from confr import *
import zipfile as zp
import compress as cp
import os
import hashlib

PATH_PROG = os.path.abspath(os.getcwd())

class NoExForm:
    @classmethod
    def open(self, *args):
        return (result, lst_tags, {}, {})

    @classmethod
    def save(self, *args):
        pass

    @classmethod
    def write_meta(self, *args):
        pass

class ExForm1: ####################################################################################################### EXTENSION FORM V° 1 ##############################################
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
            return (result, lst_tags, {}, {})

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [], {}, {})

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


class ExForm2: ####################################################################################################### EXTENSION FORM V° 2 ##############################################
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
            return (result, lst_tags, meta, {})

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [], {}, {})

    @classmethod
    def save(self, path_prog, file, data, lst_tags, meta, force = False):
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
            if 'version' in meta.keys() and force:
                meta['version'] = 'Form_2.0'
    
            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"\n').encode(get_encode()))
            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()

    @classmethod
    def write_meta(self, file, meta, path_prog):
        try:
            z = zp.ZipFile(file, 'r')
            files = {}
            for fle in z.namelist():
                if fle == 'meta.ini':
                    continue
                files[fle] = z.read(fle)

            z.close()

            z = zp.ZipFile(file, 'w')
            for file, value in files.items():
                f = z.open(file, 'w')
                f.write(value)
                f.close()

            f = z.open('meta.ini', 'w')
            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"\n').encode(get_encode()))

            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


class ExForm3: ####################################################################################################### EXTENSION FORM V° 3 ##############################################
    @classmethod
    def open(self, path_prog, name):
        try:
            f = cp.CmpdFile(name, 'r')
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
            return (result, lst_tags, meta, {})

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [], {}, {})

    @classmethod
    def save(self, path_prog, file, data, lst_tags, meta, force = False):
        try:
            z = cp.CmpdFile(file, 'w')
            z.write('data.txt', data)
            r = b''
            for i in lst_tags:
                r += str(','.join(i) + '\n').encode()
            z.write('tags.csv', r)

            if 'version' not in meta.keys():
                meta['version'] = 'Form_3.0'
            if 'time' not in meta.keys():
                meta['time'] = '0'
            if 'version' in meta.keys() and force:
                meta['version'] = 'Form_3.0'

            r = b''
            for key, value in meta.items():
                r += str('"' + key + '"-"' + value + '"\n').encode(get_encode())
            z.write('meta.ini', r)
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()

    @classmethod
    def write_meta(self, file, meta, path_prog):
        try:
            z = cp.CmpdFile(file, 'a')
            r = b''
            for key, value in meta.items():
                r += str('"' + key + '"-"' + value + '"\n').encode(get_encode())
            z.write('meta.ini', r)
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


class ExForm4: ####################################################################################################### EXTENSION FORM V° 4 ##############################################
    spliter = b'\x01'.decode(get_encode())

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

            var = {}
            variables = f.read('variables.csv').decode(get_encode())
            variables = variables.replace('\r', '\n')
            for i in variables.split('\n'):
                if i == '':
                    continue

                key, value = i.split(self.spliter)
                var[key] = value
        
            f.close()
            return (result, lst_tags, meta, var)

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()
            return ('', [], {}, {})

    @classmethod
    def save(self, path_prog, file, data, lst_tags, meta, variables, force = False):
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
                meta['version'] = 'Form_4.0'
            if 'time' not in meta.keys():
                meta['time'] = '0'
            if 'version' in meta.keys() and force:
                meta['version'] = 'Form_4.0'

            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"\n').encode(get_encode()))
            f.close()
            f = z.open('variables.csv', 'w')
            for k, v in variables.items():
                f.write(k.encode(get_encode()) + b'\x01' + v.encode(get_encode()))

            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()

    @classmethod
    def write_meta(self, file, meta, path_prog):
        try:
            z = zp.ZipFile(file, 'r')
            files = {}
            for fle in z.namelist():
                if fle == 'meta.ini':
                    continue
                files[fle] = z.read(fle)

            z.close()

            z = zp.ZipFile(file, 'w')
            for file, value in files.items():
                f = z.open(file, 'w')
                f.write(value)
                f.close()

            f = z.open('meta.ini', 'w')
            for key, value in meta.items():
                f.write(str('"' + key + '"-"' + value + '"\n').encode(get_encode()))

            f.close()
            z.close()

        except Exception as e:
            log = open(path_prog + '/log.txt', 'a')
            log.write(str(e) + '\n')
            log.close()


def found_vers(file, rcl = True):
    try:
        z = zp.ZipFile(file, 'r')
        lst = z.namelist()
        if 'meta.ini' not in lst:
            z.close()
            if rcl:
                return ExForm1
            else:
                return '1'
        else:
            f = z.open('meta.ini', 'r')
            r = f.read().decode(get_encode()).split('\n')
            f.close()
            z.close()
            for i in r:
                if i != '':
                    key, value = i.split('-')
                    key = key.replace('"', '')
                    value = value.replace('"', '')
                    if key == 'version':
                        if value == 'Form_2.0':
                            if rcl:
                                return ExForm2
                            else:
                                return '2'

                        elif value == 'Form_4.0':
                            if rcl:
                                return ExForm4
                            else:
                                return '4'

    except zp.BadZipFile:
        f = cp.CmpdFile(file, 'r')
        if 'meta.ini' in f.namelist():
            r = f.read('meta.ini', True).split('\n')
            f.close()
            for i in r:
                if i != '':
                    key, value = i.split('-')
                    key = key.replace('"', '')
                    value = value.replace('"', '')
                    if key == 'version':
                        if value == 'Form_3.0':
                            if rcl:
                                return ExForm3
                            else:
                                return '3'
        else:
            f.close()
            if rcl:
                return NoExForm
            else:
                return 0


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


class ExForm:
    def open(self, name):
        pop_deck()
        Extension = found_vers(name)
        data, lst_tags, meta, variables = Extension.open(self.path_prog, name)

        if meta != {}:
            self.stat_form_infos(True)

        try:
            askpswd(meta['password'], lambda : self.begin_openning(data, lst_tags, meta, name, variables), self.master)
        except Exception:
            self.begin_openning(data, lst_tags, meta, name, variables)

    def begin_openning(self, data, lst_tags, meta, name, variables):
        self.meta = meta
        self.variables = variables

        self.insert_text(data)

        try:
            set_deck(meta['lang'])
        except:
            pass

        for tag in lst_tags:
            self.lst_tags.append(tag)

        self.write_tags()
        try:
            meta['cursor']
            self.move_to(meta['cursor'])
        except:
            pass

        self.saved = True
        self.savedd = True
        self.path = name
        self.add_f(self.path)
        self.autocolorwords()
        self.master.title(self.title + ' - ' + self.path)
        self.update_line_numbers(fforbid = True)
        self.text.focus()

    def save(self, file, data, meta, variables):
        data = data.encode(get_encode())

        def write_form(path_prog, file, data, lst_tags, meta, variables):
            if v_form == 1:
                ExForm1.save(path_prog, file, data, lst_tags)
            elif v_form == 2:
                ExForm2.save(path_prog, file, data, lst_tags, meta, force = True)
            elif v_form == 3:
                ExForm3.save(path_prog, file, data, lst_tags, meta, force = True)
            elif v_form == 4:
                ExForm4.save(path_prog, file, data, lst_tags, meta, variables, force = True)

        def write_file(path_prog, file, data, lst_tags, meta, variables):
            if v_file == 1:
                ExForm1.save(path_prog, file, data, lst_tags)
            elif v_file == 2:
                ExForm2.save(path_prog, file, data, lst_tags, meta)
            elif v_file == 3:
                ExForm3.save(path_prog, file, data, lst_tags, meta)
            elif v_file == 4:
                ExForm4.save(path_prog, file, data, lst_tags, meta, variables)

        v_form = int(self.FORM_VERSION[0])
        v_file = int(found_vers(file, False))
        if v_form == v_file:
            write_form(self.path_prog, file, data, self.lst_tags, meta, variables)

        elif v_form > v_file:
            convert = askyesno(lg('formf'), lg('warn_old_form'))
            if convert:
                write_form(self.path_prog, file, data, self.lst_tags, meta, variables)
            else:
                write_file(self.path_prog, file, data, self.lst_tags, meta, variables)

        elif v_form < v_file:
            convert = askyesno(lg('formf'), lg('new_form'))
            if convert:
                write_form(self.path_prog, file, data, self.lst_tags, meta, variables)
            else:
                write_file(self.path_prog, file, data, self.lst_tags, meta, variables)

    def write_meta(self):
        v_form = int(self.FORM_VERSION[0])
        v_file = int(found_vers(self.path, False))
        if v_file == 2:
            ExForm2.write_meta(self.path, self.meta, self.path_prog)
        elif v_file == 3:
            ExForm3.write_meta(self.path, self.meta, self.path_prog)
        elif v_file == 4:
            ExForm4.write_meta(self.path, self.meta, self.path_prog)
        else:
            showerror(lg('formf'), lg('cant_meta'))

if __name__ == '__main__':
    from __init__ import *
