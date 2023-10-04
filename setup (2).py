from distutils.core import setup
from pathlib import Path
import os
import py2exe

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

setup(
    options = {'py2exe': {'bundle_files': 1,
                          'compressed': True,
                          'icon_resources': [(0, 'image/icons/ico.ico')],
                          'include': includefiles(),
                          'dist_dir': 'build',
                          }
               },
    windows = [{'script': "__init__.pyw"}],
    zipfile = None,
)
