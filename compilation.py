import os, datetime, time, keyboard
from main import VERSION, KillStartup
KillStartup()
import winsound as sound

print()

f = open('recent_file_list.log', 'w')
f.close()
f = open('log.txt', 'w')
f.close()

chemin = 'G:/USB_TRANSFER_SAUVEGARDE'

dir_7zip = 'C:\\Program Files\\7-Zip\\7z.exe'
dir_inno = 'C:\\Program Files (x86)\\Inno Setup 6\\iscc.exe'

keyboard.press_and_release('Alt + Return')
#print('Dimensions du terminal :', os.get_terminal_size()[0], 'par', os.get_terminal_size()[1])

version = VERSION.replace('0.', '')
version = version.split('.')
version_zip = '.'.join(version)
version = version[0]

os.system('rd "G:/Exe/Edit/" /S /Q')
try:os.mkdir('G:/Exe/Edit')
except FileExistsError:pass
os.system('xcopy /E /I "G:/Exe/Editor" "G:/Exe/Edit" < v33')

auto = True #if input('ModeAuto? ') == 'yes' else False
if auto:
    _zip=True
    comp=True
    inst=True
    _open=True
    pause=False
    mobile=True

else:
    _zip=True if input('Zip? ') == 'yes' else False
    comp=True if input('Compilation? ') == 'yes' else False
    inst=True if input('Installer? ') == 'yes' else False
    mobile=True if input('versionMobile? ') == 'yes' else False
    _open=True if input('Ouvrir? ') == 'yes' else False
    pause=True if input('Pauses? ') == 'yes' else False

now = datetime.datetime.now()
today = str(now.year)
today += '0' + str(now.month) if len(str(now.month)) == 1 else '' + str(now.month)
today += '0' + str(now.day) if len(str(now.day)) == 1 else '' + str(now.day)

if _zip:
    print('Création du zip')
    cmd = os.popen(f'"{dir_7zip}" a "{chemin}/source/Edit_' + version_zip + '_' + today + '.zip" "G:/Exe/Edit"')
    print(cmd.read())

if pause:
    os.system(f'explorer "{chemin}/source/"')
    os.system('pause')

os.chdir('G:/Exe/Edit')
if comp:
    print('Compilation')
    cmd = os.popen('setup.py build')
    print(cmd.read())

if pause:
    os.system('explorer "G:/Exe/Edit/build/exe.win-amd64-3.10/"')
    os.system('pause')

if mobile:
    print('version mobile')
    cmd = os.popen(f'"{dir_7zip}" a "{chemin}/mobile/mobile_' + version + '_win.zip" G:/Exe/Edit/build/exe.win-amd64-3.10/*')
    print(cmd.read())

if pause:
    os.system(f'explorer "{chemin}/mobile/"')
    os.system('pause')

if inst:
    print('Installateur')
    cmd = os.popen(f'"{dir_inno}" compilation.iss')
    print(cmd.read())
    print('Fichier ZIP De l\'installateur...')
    cmd = os.popen(f'"{dir_7zip}" a "{chemin}/setup/setup_' + version + f'_win.zip" "{chemin}/setup/setup_' + version + '_win.exe"')
    print(cmd.read())

if pause:
    os.system(f'explorer "{chemin}/setup/"')
    os.system('pause')

print('Suppression de la dernière version')
os.system(f'rd "{chemin}/last_version" /S /Q')
print('Ajout de la dernière version (vide -> Dossier)')
os.mkdir(f'{chemin}/last_version')

cmd = os.popen(f'copy "{chemin}/setup\\setup_' + version + f'_win.exe" "{chemin}/last_version\\setup_' + version + '_win.exe"')
print(cmd.read())
cmd = os.popen(f'copy "{chemin}/setup\\setup_' + version + f'_win.zip" "{chemin}/last_version\\setup_' + version + '_win.zip"')
print(cmd.read())
cmd = os.popen(f'copy "{chemin}/source\\Edit_' + version_zip + '_' + today + f'.zip" "{chemin}/last_version\\Edit_' + version_zip + '_' + today + '.zip"')
print(cmd.read())
cmd = os.popen(f'copy "{chemin}/mobile\\mobile_' + version + f'_win.zip" "{chemin}/last_version\\mobile_' + version + '_win.zip"')
print(cmd.read())

if _open:
    os.system(f'explorer "{chemin}/last_version"')

sound.Beep(440, 500)
time.sleep(0.5)
sound.Beep(440, 500)
time.sleep(0.5)
sound.Beep(440, 500)
time.sleep(0.5)
