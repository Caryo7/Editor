from cx_Freeze import setup, Executable
from pathlib import Path
from main import *
KillStartup()
import os.path, sys, os, datetime

modules = [#'inspect', 'glob',
           #'hashlib', 'keras_ocr',
           #'docx', 'reportlab',
           #'serial', 'PyTaskbar',
           ]

def includefiles():
    p = Path('')
    files = list(p.glob('**/*'))
    i = 0
    while True:
        try:
            if '/' in list(str(files[i])) or '\\' in list(str(files[i])):
                files.pop(i)
            else:
                files[i] = str(files[i])
                print(files[i])
                i += 1
        except IndexError:
            break
    return files



PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

options_exe = {'include_files': [os.path.join(PYTHON_INSTALL_DIR,  'DLLs', 'tk86t.dll'),
                                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')],
               #'include_files': includefiles(),
               'include_msvcr': True,
               }


options = {'build_exe': options_exe,
           }

target = Executable(script = 'G:\\Exe\\Edit\\__init__.pyw',
                    copyright= 'Copyright © ' + str(datetime.datetime.now().year) + ' ' + AUTHOR,
                    icon = 'image/icons/ico.ico',
                    base = 'Win32GUI' if sys.platform == 'win32' else 'Console',
                    shortcut_name = 'Editor',
                    shortcut_dir = 'TARINO',)

setup(name = NAME,
      version = VERSION,
      description = DESC,
      options = options,
      executables = [target])
