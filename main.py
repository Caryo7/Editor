#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################## Fichiers à changer : compilation.iss ####################
__version__ = VERSION = '37.0' ###
GUI_VERSION = '38' ###
FILE_VERSION = '2.2' ##
FORM_VERSION = '4.1' ##
LANGS_VERSION = '1.6' ##

# Partie 1 - Importation de tous les fichiers

class StartUp_Console:
    nb = 0
    i = 0

    def add(self, text):
        self.i += 1
        print(int((self.i / self.nb) * 100), '% :', text, end='\r')

    def finish(self):
        print('Initialing done !')

    def kill(self):
        pass

########## psutil :
    ## for proc in psutil.process_iter():
    ##     print(proc.name())
    ##     print(proc.pid())


print('Démarrage...')
from startup import *

if True:
    startup = Startup()
    startup.nb = 100 # Nombre de wprint
else:
    startup = StartUp_Console()
    startup.nb = 100 # Nombre de wprint

def wprint(*args):
    global startup
    try:
        startup.add(*args)
    except TclError:
        startup = StartUp_Console()
        startup.nb = 100 # Nombre de wprint
        startup.add(*args)

import time, inspect, os

NAME = 'Editor'
DESC = NAME
URL = 'https://bgtarino.wixsite.com/Editor'
PYTHON_VERSION = '3.10'
ARDUINO_VERSION = '1.16'
COMPILATOR_VERSION = '0.1 - PYTHON BETA'
AUTHOR = 'Benoit CHARREYRON'

PATH_PROG = os.path.abspath(os.getcwd())
'''
Liste des fichiers demandant PATH_PROG :
 - main.py (path)
 - confr.py (path)
 - lgviewer.py (path)
 - pswd.py (path)
 - update.py (path)
 - tree.py (path)
 - counter.py (path)
 - ext_form.py (path)
 - runner.py (path)
 - startup.py (icon)
 - progress.py (icon)
 - pdfviewer.py (icon + path)
 - counter.py (icon)
 - variables.py (icon)
'''

wprint('Importing files : ')
wprint('content')
from content import *
wprint('help')
from help import *
wprint('iofile')
from iofile import *
wprint('menubar')
from menubar import *
wprint('search')
from search import *
wprint('win')
from win import *
wprint('security')
from security import *
wprint('archives')
from archives import *
wprint('confr')
from confr import *
wprint('crypt')
from crypt import *
wprint('minitel')
from minitel import *
wprint('config')
from config import *
wprint('export')
from export import *
wprint('update')
from update import *
wprint('extensions')
from extensions import *
wprint('tasksviewer')
from tasksviewer import *
wprint('printer')
from printer import *
wprint('errors')
from errors import *
wprint('clkright')
from clkright import *
wprint('style')
from style import *
wprint('autocolor')
from autocolor import *
wprint('recentfile')
from recentfile import *
wprint('pi')
from pi import *
wprint('api')
from api import *
wprint('bgtask')
from bgtask import *
wprint('macros')
from macros import *
wprint('keyboard')
from keyb import *
wprint('images')
from images import *
wprint('Menus')
from iomenu import *
wprint('Python interpreter')
from runner import *
wprint('Importation of PyTaskBar')
import PyTaskbar
wprint('Importation of Variables system')
from variables import *
wprint('End of importation')

# 2 - Création de la class et importation de toute la hiérarchie

wprint('Importing classes')
class Main(Win,
           File,
           Search,
           help_,
           Content,
           MenuBar,
           Archives,
           Crypt,
           Minitel,
           Configurator,
           Export,
           Update,
           Extensions,
           TasksViewer,
           Printer,
           Errors,
           ClkRight,
           AutoColor,
           RecentFileList,
           Styles,
           Surcharge,
           API,
           Certify,
           Macro,
           KeyB,
           Images,
           IOMenu,
           RunPython,
           PDFTraitement,
           TableGUI,
           ):
    
# Partie 3 - Informations de base du logiciel

    def __init__(self, sys_args = None, **args):
        self.NAME = NAME
        self.DESC = DESC
        self.URL = URL
        self.VERSION = VERSION
        self.PYTHON_VERSION = PYTHON_VERSION
        self.ARDUINO_VERSION = ARDUINO_VERSION
        self.GUI_VERSION = GUI_VERSION
        self.COMPILATOR_VERSION = COMPILATOR_VERSION
        self.LANGS_VERSION = LANGS_VERSION
        self.FILE_VERSION = FILE_VERSION
        self.FORM_VERSION = FORM_VERSION
        self.AUTHOR = AUTHOR
        self.programme_termine = False
        self.sys_args = sys_args
        wprint('Définition du répertoire de travail...')
        self.path_prog = PATH_PROG
        wprint('Defining configurating mode...')
        self.configurating = False
        wprint('Importing version')
        self.version = self.__ver__ = VERSION
        wprint('Loading application ico')
        self.ico = {'win': self.path_prog + '/image/icons/ico.ico',
                    'search': self.path_prog + '/image/icons/search.ico',
                    'replace': self.path_prog + '/image/icons/replace.ico',
                    'printer': self.path_prog + '/image/icons/printer.ico',
                    'tree': self.path_prog + '/image/icons/tree.ico',
                    'security': self.path_prog + '/image/icons/security.ico',
                    'password': self.path_prog + '/image/icons/password.ico',
                    'error': self.path_prog + '/image/icons/error.ico',
                    'help': self.path_prog + '/image/icons/help.ico',
                    'config': self.path_prog + '/image/icons/config.ico',
                    'archive': self.path_prog + '/image/icons/archive.ico',
                    'style': self.path_prog + '/image/icons/style.ico',
                    'task': self.path_prog + '/image/icons/task.ico',
                    'progress': self.path_prog + '/image/icons/progress.ico',
                    'file': self.path_prog + '/image/icons/file.ico',
                    'pdf': self.path_prog + '/image/icons/pdf.ico',
                    'python': self.path_prog + '/image/icons/python.ico',
                    }

        wprint('Loading application name')
        self.title = NAME
        wprint('Saving arguments')
        self.args = args
        wprint('Begining process')
        self.__start__()
        
# Partie 4 - Création de la fenêtre et démarrage des fonctions

    def __start__(self):
        try: ## CODE DE CONTENT.PY !!!
            del self.frame_boutons
        except:
            pass

        wprint('Initialing stat = True')
        self.generating = True
        wprint('Starting tasks viewer background threads')
        self.__viewer__()
        wprint('Adding initial tasks')
        self.add_task(code='InitializeSystemSoftware', time=time.time()-20, desc='INIT_LOOP\nShow a simple window ith list of program and statement of that. Draw on the window lines with total random')
        self.finish_task(code='InitializeSystemSoftware')
        wprint('Begin connexion if necessary')
        if get_conn():
            self.add_task(code='ConnectSecurityProtocol', time=time.time()-7, desc='INIT_LOOP\nAsk for username and password to user. He has 3 possibilities.')
            self.finish_task(code='ConnectSecurityProtocol')

        wprint('Loading main process')
        self.add_task(code='MAIN_LOOP', time=time.time(), desc='MAIN Program Loop', killable = False)
        wprint('Creating window')
        if not self.__win__():
            return

        wprint('Importing images')
        self.__images__()
        wprint('Calling errors functions')
        self.__errors__()
        wprint('Begining update analyse')
        self.__update__()
        wprint('Text creation')
        self.__content__()
        wprint('Reading recent file list and adding to list of menubar')
        self.__recentfl__()
        wprint('Configuring keyboard links events')
        self.__keyb__()
        wprint('Drawing menubar')
        self.__menu__()
        wprint('Loading file manager and files\'s extensions')
        self.__file__()
        wprint('Configurating archives program')
        self.__arch__()
        wprint('Connecting to minitel')
        self.__min__()
        wprint('Loading keys of cipher unit')
        self.__crypt__()
        wprint('Connecting to printers')
        self.__printer__()
        wprint('Analyse content for styles')
        self.__style__()
        wprint('Loading settings for differents menu')
        self.__load_menus__()
        wprint('Adding click right menu to text widget')
        self.__clk__()
        wprint('Set "surcharge" process on stat ABLE')
        self.__sur__()
        wprint('Connecting to the world wide web for researchs')
        self.__api__()
        wprint('Configuring certify process')
        self.__cert__()
        wprint('Loading macros')
        self.__macro__()
        wprint('Loading python runner')
        self.__runner__()

        if self.configurating:
            wprint('Restart configurate window')
            self.IHM()
            self.configurating = False

        if get_sur():
            wprint('Start "surcharge"')
            self.start_sur()

        wprint('End of generating')
        self.generating = False
        wprint('Begining of the AutoSave protocol')
        self.ast.start()
        wprint('Run macro')

        try:
            wprint('Reading macro to invoke an error if empty')
            self.args['macro']
            try:
                wprint('Run macro with arguments')
                self.run_macro(prog=self.args['inst'], args=self.args['args'])
            except KeyError:
                wprint('Run macro without arguments')
                self.run_macro(prog=self.args['inst'])
        except KeyError:
            ""

        self.conf_win(evt = None, generate = True)

        if not self.configurating:
            wprint('Openning file asked with argument in command...')
            self.open_this(self.sys_args)

        wprint('Raising errors of initialing stat')
        self.runErrors()
        wprint('Iconning in task bar')
        self.tb = PyTaskbar.Progress(self.master.winfo_id())
        self.tb.init()
        self.tb.setState("normal")
        wprint('Begin the main process of the window')
        startup.finish()
        print('Démarrage fini avec succès !')
        self.Generate()

# Partie 5 - Execution de la class avec la connexion si demandée

def RunProg(debug=True, sys_args = ['']):
    wprint('Test startup stat')
    if get_startup() and debug:
        wprint('Start startup')
        Startup()

    wprint('Run main program')
    Main(sys_args)

# Partie 6 - Uniquement pour les tests : lors de l'éxécution de ce fichier, tout ce lance.
#            Si non, c'est le fichier __init__.py qui fait tout. __init__.py étant compilé en .exe pour windows, ...

def RunTestMacro(**args):
    args['macro'] = True
    m = Main(**args)

def KillStartup():
    startup.kill()

if __name__ == '__main__':
    wprint('Run main program')
    RunProg(False)

