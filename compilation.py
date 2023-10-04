
print('MERCI DE SUIVRE LES INDICATIONS !')
print('\n\n\n\n')
print('Récupérarion des méta données')
import os, datetime, time
import keyboard as kb
from main import VERSION, KillStartup
KillStartup()

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


print('1. Compilation complète')
print('2. Sauvegarde ZIP')
mode = int(input('> '))
if mode == 2:
    print('Enregistrement sous fichier ZIP de la version actuelle...')
    os.popen(f'"{dir_7zip}" a "{chemin}/source/Edit_' + version_zip + '_' + today + '.zip" "G:/Exe/Editor"')
    quit()


print('Mise à jour du dossier de sortie')
os.system('rd "G:/Exe/Edit/" /S /Q')
try:
    os.mkdir('G:/Exe/Edit')
except FileExistsError:
    pass

os.system('xcopy /E /I "G:/Exe/Editor" "G:/Exe/Edit"')

print('Effacement des fichiers temporaires')
f = open('G:/Exe/Edit/recent_file_list.log', 'w')
f.close()
f = open('G:/Exe/Edit/log.txt', 'w')
f.close()

print('Création du ZIP')
os.popen(f'"{dir_7zip}" a "{chemin}/source/Edit_' + version_zip + '_' + today + '.zip" "G:/Exe/Edit"')

print()
print('Date :', today)
print('Version :', version_zip)
print('N° de version :', version)

kb.write('setup.py build')
os.system('cmd /K "cd /d G:\Exe\Edit"')

print('version mobile')
os.popen(f'"{dir_7zip}" a "{chemin}/mobile/mobile_' + version + '_win.zip" G:/Exe/Edit/build/exe.win-amd64-3.10/*')


print('Installateur')
os.popen(f'"{dir_inno}" G:\Exe\Edit\compilation.iss')
print('Fichier ZIP De l\'installateur...')
os.popen(f'"{dir_7zip}" a "{chemin}/setup/setup_' + version + f'_win.zip" "{chemin}/setup/setup_' + version + '_win.exe"')


print('Suppression de la dernière version')
os.popen(f'rd "{chemin}/last_version" /S /Q')
print('Ajout de la dernière version (vide -> Dossier)')
os.popen(f'{chemin}/last_version')

os.popen(f'copy "{chemin}/setup\\setup_' + version + f'_win.exe" "{chemin}/last_version\\setup_' + version + '_win.exe"')
os.popen(f'copy "{chemin}/setup\\setup_' + version + f'_win.zip" "{chemin}/last_version\\setup_' + version + '_win.zip"')
os.popen(f'copy "{chemin}/source\\Edit_' + version_zip + '_' + today + f'.zip" "{chemin}/last_version\\Edit_' + version_zip + '_' + today + '.zip"')
os.popen(f'copy "{chemin}/mobile\\mobile_' + version + f'_win.zip" "{chemin}/last_version\\mobile_' + version + '_win.zip"')

os.popen(f'{chemin}/last_version/setup_' + version + '_win.exe')
