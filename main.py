#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################## Fichiers à changer : compilation.iss ####################
__version__ = VERSION = '38.2' ###
GUI_VERSION = '38' ###
FILE_VERSION = '2.3' ##
FORM_VERSION = '5.0' ##
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
URL = 'https://tarino-editor.000webhostapp.com/index.php'
PYTHON_VERSION = '3.10'
ARDUINO_VERSION = '1.16'
COMPILATOR_VERSION = '0.1 - PYTHON BETA'

PATH_PROG = '.'#os.path.abspath(os.getcwd())
'''
Liste des fichiers demandant PATH_PROG :
 - main.py        (path)
 - confr.py       (path)
 - ext_form.py    (path)
 - formviewer.py  (path)
 - lgviewer.py    (path)
 - switchbt.py    (path)
 - tree.py        (path)
 - pswd.py        (path)
 - progress.py    (path + icon)
 - pdfviewer.py   (path + icon)
 - startup.py     (path + icon)
 - counter.py     (path + icon)
 - ai.py          (icon)
'''

wprint('Importing files : ')
wprint('Information de configuration')
from confr import *
wprint('Gestionnaire du contenu')
from content import *
wprint('Pages d\'aides')
from help import *
wprint('I/O Manager, This can take several minutes...')
from iofile import *
wprint('Barre de Menu')
from menubar import *
wprint('Outils de recherche')
from search import *
wprint('Fenêtre principale')
from win import *
wprint('Sécurité')
from security import *
wprint('Archivage')
from archives import *
wprint('Cryptage')
from crypt import *
wprint('Minitel')
from minitel import *
wprint('Page de configuration')
from config import *
wprint('Compatibilité d\'export')
from export import *
wprint('Mise à jour')
from update import *
wprint('Extensions')
from extensions import *
wprint('Gestionnaire des taches')
from tasksviewer import *
wprint('Réseau imprimante')
from printer import *
wprint('Gestionnaire des erreurs')
from errors import *
wprint('Menu Clique Droit')
from clkright import *
wprint('Styles')
from style import *
wprint('Coloration syntaxique')
from autocolor import *
wprint('Fichiers récents')
from recentfile import *
wprint('PI')
from pi import *
wprint('API externe')
from api import *
wprint('Taches de fond')
from bgtask import *
wprint('Macros')
from macros import *
wprint('Gestion du clavier')
from keyb import *
wprint('Images')
from images import *
wprint('Menus')
from iomenu import *
wprint('Interpreter Python')
from runner import *
wprint('Artificial Intelligence')
from ai import *
wprint('Advices and Tips')
from tips import *
wprint('Système de Variables')
from variables import *
wprint('Importation de PyTaskBar')
import PyTaskbar
wprint('Fin des Importations')

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
           AiFinisher,
           Tips,
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
        self.programme_termine = False
        self.mode_record = False
        self.mainlooped = False
        self.recording = False
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
                    'ai': self.path_prog + '/image/icons/ai.ico',
                    'tips': self.path_prog + '/image/icons/question.ico',
                    'todo': self.path_prog + '/image/icons/todo.ico',
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
        wprint('Setting Artificial Intelligence')
        self.__aifinisher__()

        wprint('End of generating')
        self.generating = False
        if get_autosave():
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
        self.start_tips()

        if self.configurating:
            print('Restarting configurator\'s window')
            self.IHM()
            self.configurating = False

        if get_sur():
            wprint('Start "surcharge"')
            self.start_sur()

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
