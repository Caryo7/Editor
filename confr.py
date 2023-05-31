#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from configparser import ConfigParser
from lg import *
import os, inspect
from tkinter.messagebox import *

PATH_PROG = os.path.abspath(os.getcwd())

p = ConfigParser()
p.read(PATH_PROG + '/config.ini', encoding = 'UTF-8')

def get_ln():
    if p.get('global', 'line_number') == '1':return True
    else:return False

def get_askclose():
    if p.get('global', 'askclose') == '1':return True
    else:return False

def get_url():
     return p.get('global', 'url')

def get_nav():
    return p.get('global', 'browser')

def get_sur():
    if p.get('global', 'surcharge') == '1':return True
    else:return False

def get_notifs():
    if p.get('global', 'notifs') == '1':return True
    else:return False

def get_update_test():
    if p.get('global', 'look_update') == '1':return True
    else:return False

def get_startup():
    if p.get('global', 'startup') == '1':return True
    else:return False

def get_dark():
    if p.get('global', 'mode_dark') == '1':return True
    else:return False

def get_conn():
    if p.get('global', 'conn') == '1':return True
    else:return False

def get_menuarch():
    if p.get('menu', 'arch') == '1':return True
    else:return False

def get_menuopt():
    if p.get('menu', 'opt') == '1':return True
    else:return False

def get_menufile():
    if p.get('menu', 'file') == '1':return True
    else:return False

def get_menuedit():
    if p.get('menu', 'edit') == '1':return True
    else:return False

def get_menuhelp():
    if p.get('menu', 'help') == '1':return True
    else:return False
    
def get_menuformat():
    if p.get('menu', 'format') == '1':return True
    else:return False

def get_menurun():
    if p.get('menu', 'run') == '1':return True
    else:return False

def get_menuview():
    if p.get('menu', 'view') == '1':return True
    else:return False

def get_menucrypt():
    if p.get('menu', 'crypt') == '1':return True
    else:return False

def get_menumacro():
    if p.get('menu', 'macro') == '1':return True
    else:return False

def get_menuexport():
    if p.get('menu', 'export') == '1':return True
    else:return False

def get_menumin():
    if p.get('menu', 'minitel') == '1':return True
    else:return False
    
def get_menustyle():
    if p.get('menu', 'style') == '1':return True
    else:return False

def get_menuupd():
    if p.get('menu', 'update') == '1':return True
    else:return False

def get_menuext():
    if p.get('menu', 'extension') == '1':return True
    else:return False

def get_puces():
    if p.get('text', 'puces') == '1':return True
    else:return False

def get_berror():
    if p.get('global', 'errors') == '1':return True
    else:return False

def get_installed():
    if p.get('installer', 'installed') == '1':return True
    else:return False

def get_alerte_min():
    if p.get('minitel', 'alerte') == '1':return True
    else:return False

def get_ruban():
    print('oui')
    if p.get('view', 'ruban') == '1':return True
    else:return False

def get_boutons():
    if p.get('view', 'bar_buttons') == '1':return True
    else:return False

def get_infobar():
    if p.get('view', 'bar_info') == '1':return True
    else:return False

def get_bgd():
    return p.get('text', 'bgd')

def get_bgl():
    return p.get('text', 'bgl')

def get_fgd():
    return p.get('text', 'fgd')

def get_fgl():
    return p.get('text', 'fgl')

def get_font():
    return p.get('text', 'font')

def get_encode():
    return p.get('crypt', 'code')

def get_font_size():
    return p.get('text', 'size')

def get_tabs():
    return int(p.get('text', 'tab'))

def get_dims():
    return p.get('text', 'dims').split(',')

def get_spacing1():
    return int(p.get('text', 'dessus'))

def get_spacing2():
    return int(p.get('text', 'dessous'))

def get_spacing3():
    return int(p.get('text', 'spacing3'))

def get_pwd():
    return p.get('security', 'password')

def get_usn():
    return p.get('security', 'username')

def get_inter_time():
    return p.get('auto_save', 'delay')

def get_autosave_path():
    return p.get('auto_save', 'path')

def get_mode():
    return get_deck()

def get_key():
    try:
        return int(str(p.get('crypt', 'key')).replace('\n', ''))
    except c.ParsingError:
        return 1

deck_color = p.get('global', 'lang')
old_deck = deck_color
def get_deck():
    return deck_color

def set_deck(deck):
    deck_color = deck
def pop_deck():
    deck_color = old_deck

def get_min_info():
    return {'dev': p.get('minitel', 'dev'),
            'speed': int(p.get('minitel', 'speed')),
            'bs': int(p.get('minitel', 'bytesize')),
            'to': int(p.get('minitel', 'timeout'))}

def get_encrypted():
    if p.get('global', 'encrypt') == '1':return True
    else:return False

def write_key(key):
    f = open(PATH_PROG + '/config.ini', 'r+', encoding = get_encode())
    p.read(PATH_PROG + '/config.ini', encoding = get_encode())
    print(str(key))
    p.set('crypt', 'key', str(key))
    p.write(f)
    f.close()

def write(section, option, value):
    f = open(PATH_PROG + '/config.ini', 'r+', encoding = get_encode())
    p.read(PATH_PROG + '/config.ini', encoding = get_encode())
    p.set(section, option, str(value))
    p.write(f)
    f.close()

def read(section, option):
    return p.get(section, option)

def sel_lg():
    return p.get('gen', 'lg')

def set_n_lg(val):
    write('gen', 'lg', val)


varlg = sel_lg()
l = Lg(varlg, get_encode(), PATH_PROG)
langue = l.get()

prefixe = {'saveas': 'save_as',
           'word': 'export_word',
           'pdf': 'export_pdf',
           'gotol': 'goto_line',
           'savecopyas': 'save_copy_as',
           }

def lg(data):
    if data.lower() not in langue:
        data = prefixe[data]
    return langue[data.lower()]

if __name__ == '__main__':
    from __init__ import *

