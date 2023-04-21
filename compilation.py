import os, datetime, time, keyboard
os.system('color a')
from main import *
import winsound as sound

dir_7zip = 'C:\\Program Files\\7-Zip\\7z.exe'
dir_inno = 'C:\\Program Files (x86)\\Inno Setup 6\\iscc.exe'

keyboard.press_and_release('Alt + Return')
#print('Dimensions du terminal :', os.get_terminal_size()[0], 'par', os.get_terminal_size()[1])

version = VERSION.split('.')
if len(version) == 1:
    version_zip = version[0]
    version = version[0]
else:
    version_zip = '.'.join(version[1:])
    version = version[1]

os.system('rd "G:/Exe/Edit/" /S /Q')
try:os.mkdir('G:/Exe/Edit')
except FileExistsError:pass
os.system('xcopy /E /I "G:/Exe/Editor" "G:/Exe/Edit" < v33')
if not input('Confirmation? ') == 'yes':
    exit()

auto = True if input('ModeAuto? ') == 'yes' else False
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
    cmd = os.popen(f'"{dir_7zip}" a "N:/source/Edit_' + version_zip + '_' + today + '.zip" "G:/Exe/Edit"')
    print(cmd.read())

if pause:
    os.system('explorer "N:/source/"')
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
    cmd = os.popen(f'"{dir_7zip}" a "N:/mobile/mobile_' + version + '_win.zip" G:/Exe/Edit/build/exe.win-amd64-3.10/*')
    print(cmd.read())

if pause:
    os.system('explorer "N:/mobile/"')
    os.system('pause')

if inst:
    print('Installateur')
    cmd = os.popen(f'"{dir_inno}" compilation.iss')
    print(cmd.read())
    print('Fichier ZIP De l\'installateur...')
    cmd = os.popen(f'"{dir_7zip}" a "N:/setup/setup_' + version + '_win.zip" "N:/setup/setup_' + version + '_win.exe"')
    print(cmd.read())

if pause:
    os.system('explorer "N:/setup//"')
    os.system('pause')

print('Suppression de la dernière version')
os.system('rd "N:/last_version" /S /Q')
print('Ajout de la dernière version (vide -> Dossier)')
os.mkdir('N:/last_version')

cmd = os.popen('copy N:\\setup\\setup_' + version + '_win.exe N:\\last_version\\setup_' + version + '_win.exe')
print(cmd.read())
cmd = os.popen('copy N:\\setup\\setup_' + version + '_win.zip N:\\last_version\\setup_' + version + '_win.zip')
print(cmd.read())
cmd = os.popen('copy N:\\source\\Edit_' + version_zip + '_' + today + '.zip N:\\last_version\\Edit_' + version_zip + '_' + today + '.zip')
print(cmd.read())
cmd = os.popen('copy N:\\mobile\\mobile_' + version + '_win.zip N:\\last_version\\mobile_' + version + '_win.zip')
print(cmd.read())

if _open:
    os.system('explorer N:\\last_version')

sound.Beep(440, 500)
time.sleep(0.5)
sound.Beep(440, 500)
time.sleep(0.5)
sound.Beep(440, 500)
time.sleep(0.5)
input()
