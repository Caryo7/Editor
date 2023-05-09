import winsound as sound
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from threading import Thread

root = Tk()
root.title('Compilation')
root.resizable(False, False)
text = Text(root, stat = 'disabled', font = ('Courier', 8))
text.place(x = 10, y = 40, width = 680, height = 450)
pb = Progressbar(root, mode = 'determinate', orient = 'horizontal', length = 680, value = 0)
pb.place(x = 10, y = 10)
root.geometry('700x500')
root.update()
n = 0
nmax = 18

def printw(txt = ''):
    global n
    n += 1
    text.config(stat = 'normal')
    text.insert('end', txt)
    text.insert('end', '\n')
    text.see('end')
    text.config(stat = 'disabled')
    pb['value'] = int((n * 100) / nmax)
    root.update()

printw('Importation')
import os, datetime, time, keyboard
from main import VERSION, KillStartup
KillStartup()

printw()


chemin = 'G:/USB_TRANSFER_SAUVEGARDE'
dir_7zip = 'C:\\Program Files\\7-Zip\\7z.exe'
dir_inno = 'C:\\Program Files (x86)\\Inno Setup 6\\iscc.exe'

## Versions
version = VERSION.replace('0.', '')
version = version.split('.')
version_zip = '.'.join(version)
version = version[0]

## Date
now = datetime.datetime.now()
today = str(now.year)
today += '0' + str(now.month) if len(str(now.month)) == 1 else '' + str(now.month)
today += '0' + str(now.day) if len(str(now.day)) == 1 else '' + str(now.day)

def folder():
    printw('Mise à jour du dossier de sortie')
    cmd = os.popen('rd "G:/Exe/Edit/" /S /Q')
    printw(cmd.read())
    try:
        os.mkdir('G:/Exe/Edit')
    except FileExistsError:
        pass
    
    cmd = os.popen('xcopy /E /I "G:/Exe/Editor" "G:/Exe/Edit" < v33')
    printw(cmd.read())

def erease():
    printw('Effacement des fichiers temporaires')
    f = open('recent_file_list.log', 'w')
    f.close()
    f = open('log.txt', 'w')
    f.close()

def _zip():
    printw('Création du zip')
    cmd = os.popen(f'"{dir_7zip}" a "{chemin}/source/Edit_' + version_zip + '_' + today + '.zip" "G:/Exe/Edit"')
    printw(cmd.read())

def compil():
    printw('Compilation')
    cmd = os.popen('setup.py build')
    printw(cmd.read())

def mobile():
    printw('version mobile')
    cmd = os.popen(f'"{dir_7zip}" a "{chemin}/mobile/mobile_' + version + '_win.zip" G:/Exe/Edit/build/exe.win-amd64-3.10/*')
    printw(cmd.read())

def inst():
    printw('Installateur')
    cmd = os.popen(f'"{dir_inno}" compilation.iss')
    printw(cmd.read())
    printw('Fichier ZIP De l\'installateur...')
    cmd = os.popen(f'"{dir_7zip}" a "{chemin}/setup/setup_' + version + f'_win.zip" "{chemin}/setup/setup_' + version + '_win.exe"')
    printw(cmd.read())

def last_version():
    printw('Suppression de la dernière version')
    cmd = os.popen(f'rd "{chemin}/last_version" /S /Q')
    printw(cmd.read())
    printw('Ajout de la dernière version (vide -> Dossier)')
    os.mkdir(f'{chemin}/last_version')

    cmd = os.popen(f'copy "{chemin}/setup\\setup_' + version + f'_win.exe" "{chemin}/last_version\\setup_' + version + '_win.exe"')
    printw(cmd.read())
    cmd = os.popen(f'copy "{chemin}/setup\\setup_' + version + f'_win.zip" "{chemin}/last_version\\setup_' + version + '_win.zip"')
    printw(cmd.read())
    cmd = os.popen(f'copy "{chemin}/source\\Edit_' + version_zip + '_' + today + f'.zip" "{chemin}/last_version\\Edit_' + version_zip + '_' + today + '.zip"')
    printw(cmd.read())
    cmd = os.popen(f'copy "{chemin}/mobile\\mobile_' + version + f'_win.zip" "{chemin}/last_version\\mobile_' + version + '_win.zip"')
    printw(cmd.read())

def start(cmd, wait = False):
    cmd()
    #th = Thread(target = cmd)
    #th.daemon = True
    #th.start()
    #if wait:
        #th.join()

    #return th

def lancer():
    start(erease, True)
    start(folder, True)
    start(_zip)
    os.chdir('G:/Exe/Edit')
    start(compil, True)
    a = start(mobile)
    b = start(inst)
    #a.join()
    #b.join()

    start(last_version)

def run(b):
    b.destroy()
    root.update()

    start(lancer, True)

    root.destroy()
    os.popen(f'{chemin}/last_version/setup_' + version + '_win.exe')
    

b = Button(root, text = 'Start', command = lambda : run(b))
b.place(x = 350, y = 250)

root.mainloop()
