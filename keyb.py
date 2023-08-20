#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *
from counter import *
from lgviewer import *
from tree import *

from tkinter import *

class KeyB:
    def __keyb__(self):
        self.actions = {'new' :         [self.new, '', 'self.new()', {'evt': None, 'forcing': False, 'mode_clear': False}],
                        'open' :        [self.open, '', 'self.open()', {'evt': None, 'name': None, 'forcing': False, 'ask_info': True}],
                        'save' :        [self.save, '', 'self.save()', {'evt': None, 'forcing': False}],
                        'saveas' :      [self.saveas, '', 'self.saveas()', {'evt': None, 'name': None, 'forcing': False, 'path': ''}],
                        'savecopyas' :  [self.savecopyas, '', 'self.savecopyas()', {'evt': None, 'forcing': False}],
                        'settings' :    [self.ask_settings, '', 'self.ask_settings()', {}],
                        'print' :       [self.print_window, '', 'self.print_window()', {'evt': None}],
                        'close' :       [self.fermer, '', 'self.fermer()', {'evt': None}],
                        'quit' :        [self.Quitter, '', 'self.Quitter()', {'evt': None}],
                        'undo' :        [self.undo, '', 'self.undo()', {'evt': None}],
                        'redo' :        [self.redo, '', 'self.redo()', {'evt': None}],
                        'goto' :        [self.gotol, '', 'self.gotol()', {'evt': None, 'line': None}],
                        'search' :      [self.search, '', 'self.search()', {'evt': None}],
                        'replace' :     [self.replace, '', 'self.replace()', {'evt': None}],
                        'news' :        [self.ask_new_tag, '', 'self.ask_new_tag()', {'values': [None, None, None], 'mode_pre': False, 'forcing': False}], # # -> Nouveau style
                        'cstyle' :      [self.add_tag_here, '', 'self.add_tag_here()', {}], # # -> Choisir un style
                        'comment' :     [self.comment, '', 'self.comment()', {}], # # -> Commenter la ligne
                        'uncomment' :   ['', '', '', {}], # # -> Dé commenter la ligne
                        'run_python':   [self.run_python, '', 'self.run_python()', {}],
                        'python':       [self.python_exe, '', 'self.python_exe()', {}],
                        'solve' :       ['', '', '', {}], # # -> Résoudre (pour compilateur externe)
                        'check' :       ['', '', '', {}], # # -> Vérifier (pour compilateur externe)
                        'run' :         ['', '', '', {}], # # -> Executer (pour compilateur externe)
                        'compile' :     ['', '', '', {}], # # -> Compiler (pour compilateur externe)
                        'expw' :        [self.export_word, '', 'self.export_word()', {}], #  -> Exporter en word
                        'expp' :        [self.export_pdf, '', 'self.export_pdf()', {'mode_print': False, 'cmd_print': None}], # # -> Exporter en PDF
                        'key' :         [self.generate_key, '', 'self.generate_key()', {}], # # -> Changement de cléf de cryptage
                        'archive' :     [self.create_a, '', 'self.create_a()', {}], # # -> Créer une archive
                        'append' :      [self.add_new_version, '', 'self.add_new_version()', {}], # # -> Ajouter à l'archive
                        'compare' :     [self.compare, '', 'self.compare()', {}], # # -> Comparer l'archive
                        'send' :        [self.send_file, '', 'self.send_file()', {}], # # -> Envoyer au minitel
                        'bip' :         [self.bip, '', 'self.bip()', {}], # # -> Faire faire au minitel un bip
                        'ulla' :        [self.ulla, '', 'self.ulla()', {}], # # -> Affiche l'accueil de ULLA sur le minitel
                        'clear' :       [self.home, '', 'self.home()', {}], # # -> Effacer le minitel
                        'update' :      [self.get_update, '', 'self.get_update()', {}], # # -> Installer une mise à jour
                        'upgrade' :     ['', '', '', {}], # # -> Installer une mise à jour depuis internet
                        'macro' :       [self.load_macro, '', 'self.load_macro()', {}], # # -> Charger une macro et l'éxécuter
                        'cnf' :         [self.IHM, '', 'self.IHM()', {}], # # -> Configurer (IHM)
                        'lnb' :         [self.act_widget_ln, '', 'self.act_widget_ln()', {}], # # -> Numéro de lignes
                        'dark' :        [self.act_color_theme, '', 'self.act_color_theme()', {}], # # -> Mode sombre
                        'visut' :       [self.show, '', 'self.show()', {}], # # -> Visualisateur des taches en cours
                        'lgv' :         [lambda : LgViewer(self.master), '', 'LgViewer()', {}], # # -> Visualisateur des langues
                        'about' :       [self.About, '', 'self.About()', {}], # # -> A propos
                        'doc' :         [self.documentation, '', 'self.documentation()', {}], # # -> Documentation
                        'todo' :        [self.ToDo, '', 'self.ToDo()', {}], # # -> A Faire
                        'lines' :       [lambda : act(self), '', 'act(self.master)', {}], # # -> Nombre de lignes
                        'struct' :      [Tkin, '', 'Tkin()', {}], # # -> Structure du programme
                        'prog' :        [Code, '', 'Code()', {}], # # -> Programme
                        'clear_recent': [self.clear_recent, '', 'clear_recent()', {}], # # -> Effacement liste fichiers récents
                        'copy':         [self.copy, '', 'copy', {}],
                        'cut':          [self.cut, '', 'cut', {}],
                        'past':         [self.past, '', 'past', {}],
                        'exit':         [self.Quitter, '', 'self.Quitter()', {}],
                        'word':         [self.export_word, '', 'self.export_word()', {}],
                        'pdf':          [self.export_pdf, '', 'self.export_pdf()', {'mode_print': False, 'cmd_print': None}],
                        'configs':      [self.config_tags, '', 'self.config_tags()', {}],
                        'import':       [self.importer, '', 'self.importer()', {'file': None, 'ask_info': True, 'forcing': False}],
                        'meta_info':    [self.show_info, '', 'self.show_info()', {}],
                        'lst_vars':     [lambda : self.start_vars(mode = 'gestion'), '', 'self.start_vars()', {}],
                        'add_var':      [self.append_var, '', 'self.append_var()', {}],
                        'place_var':    [self.place_variable, '', 'self.place_variable()', {}],
                        'record_macro': [self.record_macro, '', 'self.record_macro()', {}],
                        'switch_record':[self.switch_record, '', 'self.switch_macro()', {}],
                        'finish_record':[self.finish_record, '', 'self.finish_macro()', {}],

                        '':             ['', '', '', {}],
                        }

        f = open(self.path_prog + '/keys.k', 'r', encoding = get_encode())
        r = f.read()
        f.close()

        self.argsPerLine = {}

        for ens in r.split('\n'):
            if ens != '':
                name, event = ens.split(' = ')
                try:
                    self.actions[name][1] = event
                    self.argsPerLine[name] = self.actions[name][-1]
                except KeyError:
                    print('Error :', name)
                    pass

    def reset_tableactions(self):
        ## devrait remettre dans le dernier dictionnaire de chaque action sa valeur de départ...
        for k, _ in self.actions.items():
            self.actions[k][-1] = self.argsPerLine[k]

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
        print('Définition du raccourcis : Touche', self.actions[name][1], 'à la fonction', self.actions[name][2])

        if self.actions[name][2] == '':
            return

        try:
            self.menubar.bind_all(self.actions[name][1], lambda evt : self.actions[name][0]())
        except TclError:
            pass

if __name__ == '__main__':
    from __init__ import *
