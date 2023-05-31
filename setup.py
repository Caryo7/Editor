from cx_Freeze import setup, Executable
from pathlib import Path
from main import *
import os.path, sys, os

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
options = {'build_exe': {'include_files': [os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll')]}}
base = None

## Modules requis :
# - hashlib
# - sqlite3
# - python-docx
# - reportlab
# - serial / pyserial
# - glob

if sys.platform == 'win32':
    base = 'Win32GUI'
    print('Récupération des fichiers...')
    p = Path('')
    includefiles = list(p.glob('**/*'))
    i = 0
    while True:
        try:
            if '/' in list(str(includefiles[i])) or '\\' in list(str(includefiles[i])):
                includefiles.pop(i)
            else:
                includefiles[i] = str(includefiles[i])
                i += 1
        except IndexError:
            break

    print('Chemin de l\'éxécutable...')
    target = Executable(script = 'G:\\Exe\\Edit\\__init__.py',
                        copyright= 'Copyright © 2023 Benoit CHARREYRON',
                        icon = 'image/ico.ico',
                        base = base)

<<<<<<< Updated upstream
    print('Définition des paramètres...')
    setup(name = NAME,
          version = VERSION,
          description = DESC,
          options = {'build_exe': {'include_files': includefiles}},
          executables = [target])
=======
##options_msi = {#'add_to_path': True,
##               #'all_users': True,
##               'data': msi_data,
##               'summary_data': msi_summary,
##               'install_icon': 'image/ico.ico',
##               'product_code': '1000000000',
##               'upgrade_code': '{10000000-0000-0000-0000-000000000000}',
##               #'extensions': ,
##               }

options = {'build_exe': options_exe,
           #'bdist_msi': options_msi,
           }

target = Executable(script = 'G:\\Exe\\Edit\\__init__.py',
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
>>>>>>> Stashed changes
