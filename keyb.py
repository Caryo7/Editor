#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *
from counter import *
from lgviewer import *
from tree import *

from tkinter import *

class KeyB:

    def __keyb__(self):
        self.actions = {'new' :        [lambda evt : self.new(), None, 'self.new()'],
                        'open' :       [lambda evt : self.open(), None, 'self.open()'],
                        'save' :       [lambda evt : self.save(), None, 'self.save()'],
                        'saveas' :     [lambda evt : self.saveas(), None, 'self.saveas()'],
                        'savecopyas' : [lambda evt : self.savecopyas(), None, 'self.savecopyas()'],
                        'print' :      [lambda evt : self.print_window(), None, 'self.print_window()'],
                        'close' :      [lambda evt : self.fermer(), None, 'self.fermer()'],
                        'quit' :       [lambda evt : self.Quitter(), None, 'self.Quitter()'],
                        'undo' :       [lambda evt : self.undo(), None, 'self.undo()'],
                        'redo' :       [lambda evt : self.redo(), None, 'self.redo()'],
                        'goto' :       [lambda evt : self.gotol(), None, 'self.gotol()'],
                        'search' :     [lambda evt : self.search(), None, 'self.search()'],
                        'replace' :    [lambda evt : self.replace(), None, 'self.replace()'],
                        'news' :       [lambda evt : self.ask_new_tag(), None, 'self.ask_new_tag()'], # # -> Nouveau style
                        'cstyle' :     [lambda evt : self.add_tag_here(), None, 'self.add_tag_here()'], # # -> Choisir un style
                        'comment' :    [lambda evt : self.comment(), None, 'self.comment()'], # # -> Commenter la ligne
                        'uncomment' :  [None, None, ''], # # -> Dé commenter la ligne
                        'solve' :      [None, None, ''], # # -> Résoudre (pour compilateur externe)
                        'check' :      [None, None, ''], # # -> Vérifier (pour compilateur externe)
                        'run' :        [None, None, ''], # # -> Executer (pour compilateur externe)
                        'compile' :    [None, None, ''], # # -> Compiler (pour compilateur externe)
                        'expw' :       [lambda evt : self.export_word(), None, 'self.export_word()'], #  -> Exporter en word
                        'expp' :       [lambda evt : self.export_pdf(), None, 'self.export_pdf()'], # # -> Exporter en PDF
                        'key' :        [lambda evt : self.generate_key(), None, 'self.generate_key()'], # # -> Changement de cléf de cryptage
                        'archive' :    [lambda evt : self.create_a(), None, 'self.create_a()'], # # -> Créer une archive
                        'append' :     [lambda evt : self.add_new_version(), None, 'self.add_new_version()'], # # -> Ajouter à l'archive
                        'compare' :    [lambda evt : self.compare(), None, 'self.compare()'], # # -> Comparer l'archive
                        'send' :       [lambda evt : self.send_file(), None, 'self.send_file()'], # # -> Envoyer au minitel
                        'bip' :        [lambda evt : self.bip(), None, 'self.bip()'], # # -> Faire faire au minitel un bip
                        'ulla' :       [lambda evt : self.ulla(), None, 'self.ulla()'], # # -> Affiche l'accueil de ULLA sur le minitel
                        'clear' :      [lambda evt : self.home(), None, 'self.home()'], # # -> Effacer le minitel
                        'update' :     [lambda evt : self.get_update(), None, 'self.get_update()'], # # -> Installer une mise à jour
                        'upgrade' :    [None, None, ''], # # -> Installer une mise à jour depuis internet
                        'macro' :      [lambda evt : self.load_macro(), None, 'self.load_macro()'], # # -> Charger une macro et l'éxécuter
                        'cnf' :        [lambda evt : self.IHM(), None, 'self.IHM()'], # # -> Configurer (IHM)
                        'lnb' :        [lambda evt : self.act_widget_ln(), None, 'self.act_widget_ln()'], # # -> Numéro de lignes
                        'dark' :       [lambda evt : self.act_color_theme(), None, 'self.act_color_theme()'], # # -> Mode sombre
                        'visut' :      [lambda evt : self.show(), None, 'self.show()'], # # -> Visualisateur des taches en cours
                        'lgv' :        [lambda evt : LgViewer(), None, 'LgViewer()'], # # -> Visualisateur des langues
                        'about' :      [lambda evt : self.About(), None, 'self.About()'], # # -> A propos
                        'doc' :        [lambda evt : self.documentation(), None, 'self.documentation()'], # # -> Documentation
                        'todo' :       [lambda evt : self.ToDo(), None, 'self.ToDo()'], # # -> A Faire
                        'lines' :      [lambda evt : act(self.master), None, 'act(self.master)'], # # -> Nombre de lignes
                        'struct' :     [lambda evt : Tkin(), None, 'Tkin()'], # # -> Structure du programme
                        'prog' :       [lambda evt : Code(), None, 'Code()'], # # -> Programme
                        'clear_recent':[lambda evt : self.clear_recent(), None, 'clear_recent()'], # # -> Effacement liste fichiers récents
                        }

        f = open(self.path_prog + '/keys.k', 'r', encoding = get_encode())
        r = f.read()
        f.close()

        for ens in r.split('\n'):
            if ens != '':
                name, event = ens.split(' = ')
                try:
                    self.actions[name][1] = event
                except KeyError:
                    print('Error :', name)
                    pass

    def set_cmds(self):
        for name, _ in self.actions.items():
            self.binderg(name)

    def get_accelerator(self, name):
        try:
            event = self.actions[name][1]
        except KeyError:
            return ''

        if event == '':
            return ''

        if event[0] == 'F':
            return event

        event = str(event.replace('<', '')).replace('>', '')
        event = event.split('-')
        accelerator = ''

        for key in event:
            if key == 'Control':
                accelerator += 'Ctrl + '
            elif key == 'Alt':
                accelerator += 'Alt + '
            elif key[0] == 'F':
                accelerator = key
            elif 64 < ord(key) < 64 + 26:
                accelerator += 'Shift + ' + key.upper()
            elif 96 < ord(key) < 96 + 26:
                accelerator += key.upper()
            else:
                accelerator += key

        return accelerator

    def binderg(self, name):
        print('Définition du raccourcis : Touche', self.actions[name][1], 'à fonction', self.actions[name][2])

        try:
            self.menubar.bind_all(self.actions[name][1], self.actions[name][0])
        except TclError:
            pass

if __name__ == '__main__':
    from __init__ import *
