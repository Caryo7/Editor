from tkinter import *
from confr import *
import time

class Python: # Couleurs pour le langage python :
    colors = {'#FF8000':['await', 'async', 'nonlocal', 'and', 'as', 'assert', 'break',
                         'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
                         'exec', 'finally', 'for', 'from', 'global', 'if', 'import',
                         'in', 'is', 'lambda', 'not', 'or', 'pass', 'raise', 'return',
                         'try', 'while', 'with', 'yield', 'None', 'True', 'False'], # Mots clefs

              '#FF00FF':['open', 'isinstance', 'range', 'len', 'str', 'int', 'bool',
                         'float', 'char', 'method', 'type', 'print', 'input', 'eval',
                         'list', 'set', 'bin', 'bytes', 'exit', 'quit', 'Exception'], # Mots clefs 2
              }

    chains = {'"""': '#02FF02',
              "'''": "#02FF02",
              '"': '#02FF02',
              "'": "#02FF02"} # Chaines de caractères

    names = {'class': ('#5E5EFF', ':'),
             'def': ('#5E5EFF', '(')} # Couleurs des noms de fonctions/classes

class Cpp: # Couleurs pour le langage C++
    colors = {'yellow':['void', 'int', 'char', 'float', 'long', 'double', 'byte', 'class', 'if', 'while', 'do', 'switch'],
              'green':['endl', 'cout', 'cin'],
              }

    chains = {'"""': 'yellow',
              "'''": "yellow", 
              '"': 'yellow', 
              "'": "yellow",
              '< >': 'grey'}

    names = {'void': ('blue', '('),
             'class': ('blue', '{')}

class Json: # Couleurs pour les fichiers JSON
    colors = {}

    chains = {'"': 'green',}

    names = {}


class Colors(Python): # Permet de retrouver les couleurs selon le langage
    def get_deck_name(self):
        if not self.act_color:
            if not self.act_colorc:
                deck = get_deck()
            else:
                deck = self.act_colorc
        else:
            deck = self.act_color

        return deck

    def get_colors(self):
        deck = self.get_deck_name()
        if deck == 'Python':
            return Python.colors
        elif deck == 'C++':
            return Cpp.colors
        elif deck == 'Json':
            return Json.colors
        else:
            return {} # Si pas de langage

    def get_strings(self):
        deck = self.get_deck_name()
        if deck == 'Python':
            return Python.chains
        elif deck == 'C++':
            return Cpp.chains
        elif deck == 'Json':
            return Json.chains
        else:
            return {}

    def get_names(self):
        deck = self.get_deck_name()
        if deck == 'Python':
            return Python.names
        elif deck == 'C++':
            return Cpp.names
        elif deck == 'Json':
            return Json.names
        else:
            return {}


class AutoColor(Colors):
    def __ac__(self): # Ajoute la tache en cours au gestionnaire
        self.mode_colors = get_modecolor() # Demande si les couleurs sont présentes
        self.act_color = None
        self.act_colorc = None
        self.add_task(code='AutoColor', time=time.time(), desc='MAIN_LOOP\nRead every word on the text and put colors in case of word is on the data base (Actually, it work on python and C++ keywords) Caution : Can\'t be unstart in this version !', fnct = 'autocolor')

    def autocolorwords(self): # Met à jour l'affichage des couleurs
        if self.lst_fnct['autocolor'] or not(self.mode_colors):
            return # Si fonctions pas demandé (pas activée ou tué par le gestionnaire)

        mots_reserves = self.get_colors() # Reprend les couleurs et mots
        chains = self.get_strings()
        names = self.get_names()

        for tag in self.text.tag_names(): # Supprime toutes les anciennes couleurs
            self.text.tag_delete(tag)

        for color, mots in mots_reserves.items(): # Met les mots clef en couleurs
            for mot in mots:
                start = "1.0"
                while True:
                    start = self.text.search(mot, start, END)
                    if not start:
                        break

                    end = "{0}+{1}c".format(start, len(mot))

                    prev_false = self.text.get("{}-1c".format(start)).lower() in self.letters
                    index_0 = self.text.index('{}'.format(start)) == '1.0'
                    next_false = self.text.get('{}'.format(end))  in self.letters

                    if index_0:
                        prev_false = False

                    if prev_false or next_false:
                        start = "{0}+{1}c".format(start, len(mot))
                        continue

                    self.text.tag_add(mot, start, end)
                    self.text.tag_configure(mot, foreground=color)
                    start = end

        for gui, color in chains.items(): # Met les chaines de caractères en couleur
            start = '1.0'
            dep = start
            mode = False
            while True:
                if ' ' in gui:
                    index = self.text.search(gui[0] if not mode else gui[-1], dep, END) # Trouve les guillemets
                else:
                    index = self.text.search(gui, dep, END) # Trouve les guillemets

                if not index:
                    break # Si plus de guillemets, casse la boucle

                if not mode: # Si mode ouverture
                    start = index # Index du début du guillemet (inclu)
                    dep = '{0}+{1}c'.format(start, len(gui))
                    mode = True # Passage en mode fermeture de guillemet
                else: # Si mode fermeture
                    end = '{0}+{1}c'.format(index, len(gui))
                    self.text.tag_add(gui, start, end)
                    self.text.tag_configure(gui, foreground=color)
                    mode = False # Repasse en mode ouverture
                    dep = '{0}+1c'.format(end) # Décalle d'index de départ de la recherche (évite while True)

        for kw, (color, close) in names.items(): # Met les noms de fonctions/classes en couleurs
            start = '1.0'
            dep = start
            mode = False
            while True:
                if not mode:
                    index = self.text.search(kw, dep, END)
                else:
                    index = self.text.search(close, dep, END)

                if not index:
                    break

                if not mode:
                    start = self.text.index('{0}+{1}c'.format(index, len(kw)))
                    dep = start
                    mode = True
                else:
                    end = index
                    self.text.tag_add('_' + kw, start, end)
                    self.text.tag_configure('_' + kw, foreground = color)
                    dep = self.text.index('{0}+1c'.format(end))
                    mode = False


if __name__ == '__main__':
    from __init__ import *
