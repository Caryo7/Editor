#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *
from counter import *
from lgviewer import *
from tree import *

from tkinter import *

class KeyB:

    def __keyb__(self):
        self.actions = {'new' :        [self.new, None, 'self.new()'],
                        'open' :       [self.open, None, 'self.open()'],
                        'save' :       [self.save, None, 'self.save()'],
                        'saveas' :     [self.saveas, None, 'self.saveas()'],
                        'savecopyas' : [self.savecopyas, None, 'self.savecopyas()'],
                        'settings' :   [self.ask_settings, None, 'self.ask_settings()'],
                        'print' :      [self.print_window, None, 'self.print_window()'],
                        'close' :      [self.fermer, None, 'self.fermer()'],
                        'quit' :       [self.Quitter, None, 'self.Quitter()'],
                        'undo' :       [self.undo, None, 'self.undo()'],
                        'redo' :       [self.redo, None, 'self.redo()'],
                        'goto' :       [self.gotol, None, 'self.gotol()'],
                        'search' :     [self.search, None, 'self.search()'],
                        'replace' :    [self.replace, None, 'self.replace()'],
                        'news' :       [self.ask_new_tag, None, 'self.ask_new_tag()'], # # -> Nouveau style
                        'cstyle' :     [self.add_tag_here, None, 'self.add_tag_here()'], # # -> Choisir un style
                        'comment' :    [self.comment, None, 'self.comment()'], # # -> Commenter la ligne
                        'uncomment' :  [None, None, ''], # # -> Dé commenter la ligne
                        'solve' :      [None, None, ''], # # -> Résoudre (pour compilateur externe)
                        'check' :      [None, None, ''], # # -> Vérifier (pour compilateur externe)
                        'run' :        [None, None, ''], # # -> Executer (pour compilateur externe)
                        'compile' :    [None, None, ''], # # -> Compiler (pour compilateur externe)
                        'expw' :       [self.export_word, None, 'self.export_word()'], #  -> Exporter en word
                        'expp' :       [self.export_pdf, None, 'self.export_pdf()'], # # -> Exporter en PDF
                        'key' :        [self.generate_key, None, 'self.generate_key()'], # # -> Changement de cléf de cryptage
                        'archive' :    [self.create_a, None, 'self.create_a()'], # # -> Créer une archive
                        'append' :     [self.add_new_version, None, 'self.add_new_version()'], # # -> Ajouter à l'archive
                        'compare' :    [self.compare, None, 'self.compare()'], # # -> Comparer l'archive
                        'send' :       [self.send_file, None, 'self.send_file()'], # # -> Envoyer au minitel
                        'bip' :        [self.bip, None, 'self.bip()'], # # -> Faire faire au minitel un bip
                        'ulla' :       [self.ulla, None, 'self.ulla()'], # # -> Affiche l'accueil de ULLA sur le minitel
                        'clear' :      [self.home, None, 'self.home()'], # # -> Effacer le minitel
                        'update' :     [self.get_update, None, 'self.get_update()'], # # -> Installer une mise à jour
                        'upgrade' :    [None, None, ''], # # -> Installer une mise à jour depuis internet
                        'macro' :      [self.load_macro, None, 'self.load_macro()'], # # -> Charger une macro et l'éxécuter
                        'cnf' :        [self.IHM, None, 'self.IHM()'], # # -> Configurer (IHM)
                        'lnb' :        [self.act_widget_ln, None, 'self.act_widget_ln()'], # # -> Numéro de lignes
                        'dark' :       [self.act_color_theme, None, 'self.act_color_theme()'], # # -> Mode sombre
                        'visut' :      [self.show, None, 'self.show()'], # # -> Visualisateur des taches en cours
                        'lgv' :        [lambda : LgViewer(self.master), None, 'LgViewer()'], # # -> Visualisateur des langues
                        'about' :      [self.About, None, 'self.About()'], # # -> A propos
                        'doc' :        [self.documentation, None, 'self.documentation()'], # # -> Documentation
                        'todo' :       [self.ToDo, None, 'self.ToDo()'], # # -> A Faire
                        'lines' :      [lambda : act(self.master), None, 'act(self.master)'], # # -> Nombre de lignes
                        'struct' :     [Tkin, None, 'Tkin()'], # # -> Structure du programme
                        'prog' :       [Code, None, 'Code()'], # # -> Programme
                        'clear_recent':[self.clear_recent, None, 'clear_recent()'], # # -> Effacement liste fichiers récents
                        'copy':        [self.copy, None, 'copy'],
                        'cut':         [self.cut, None, 'cut'],
                        'past':        [self.past, None, 'past'],
                        'exit':        [self.Quitter, None, 'self.Quitter()'],
                        'word':        [self.export_word, None, 'self.export_word()'],
                        'pdf':         [self.export_pdf, None, 'self.export_pdf()'],
                        'configs':     [self.config_tags, None, 'self.config_tags()'],

                        '':            [None, None, ''],
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
            self.menubar.bind_all(self.actions[name][1], lambda evt : self.actions[name][0]())
        except TclError:
            pass

if __name__ == '__main__':
    from __init__ import *
