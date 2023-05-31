#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from confr import *

class Macro:
    def __macro__(self):
        self.file = ''
        self.inst = []
        self.instructions = {
            # API
            "internet_research":[self.internet_research],
            "bresearch":[self.bresearch],

            # Archive
            "create_a":[self.create_a],
            "add_new_version":[self.add_new_version],
            "start_analyse":[self.start_analyse],
            "compare":[self.compare],

            # Auto Color
            "tryword":[self.tryword],
            "autocolorwords":[self.autocolorwords],

            # bg task

            # Clique droit

            # Content
            "act_puces":[self.act_puces],
            "conf_win":[self.conf_win],
            "act_widget_ln":[self.act_widget_ln],
            "act_color_theme":[self.act_color_theme],
            "update_line_numbers":[self.update_line_numbers],
            "split":[self.split, 'value'],

            # Cryptage
            "encrypt":[self.encrypt, 'data'],
            "decrypt":[self.decrypt, 'data'],
            "generate_key":[self.generate_key],

            # Export
            "export_word":[self.export_word],
            "export_pdf":[self.export_pdf],

            # Extensions

            # Help
            "About":[self.About],
            "insert":[self.insert, 'title', 'data'],
            "documentation":[self.documentation],

            # Fichier
            "open_recent":[self.open_recent, 'pos'],
            "ext":[self.ext, 'name'],
            "open":[self.open],
            "save":[self.save],
            "saveas":[self.saveas],
            "savecopyas":[self.savecopyas],
            "new":[self.new],

            # Minitel
            "send_file":[self.send_file],

            # Surcharge
            "start_sur":[self.start_sur],

            # Imprimer
            "print_window":[self.print_window],

            # Recent File List
            "get_rfl":[self.get_rfl],
            "add_f":[self.add_f, 'name'],

            # Recherche
            "search":[self.search],
            "_search":[self._search],
            "replace":[self.replace],
            "gotol":[self.gotol],
            "comment":[self.comment],
            "copy":[self.copy],
            "past":[self.past],
            "cut":[self.cut],
            "undo":[self.undo],
            "redo":[self.redo],

            # Style
            "new_tag":[self.new_tag, 'bg', 'fg', 'name', 'i', 'r'],
            "add_tag_here":[self.add_tag_here],
            "write_tags":[self.write_tags],
            "ask_new_tag":[self.ask_new_tag],
            "nt":[self.nt],

            # Lecteur de taches
            "show":[self.show],
            "kill":[self.kill],
            "add_task":[self.add_task, 'code', 'time'],
            "finish_task":[self.finish_task, 'code'],
            }
        self.args = {'args':{}}

    def load_macro(self):
        n = askopenfilename(title=lg('open'), initialdir='.', filetypes=[(lg('mf'), '*.macro'), (lg('alf'), '*.*')])
        if n:
            try:
                f = open(n, 'r', encoding='UTF-8')
                ins = f.read().split('\n')
                f.close()
                self.file = n
                for i in ins:
                    ar = []
                    self.args['args'] = {}
                    self.inst = []
                    if i:
                        self.inst.append(i.split(';')[0])
                        if len(i.split(';')) > 1:
                            ar += i.split(';')[1].split(',')
                            for j in ar:
                                self.args['args'][j.split('=')[0]] = j.split('=')[1]
                    self.run_macro(**self.args)
            except FileNotFoundError:
                ""

    def run_macro(self, prog=None, **args):
        if not prog:
            for prog in self.inst:
                n = 0
                t = []
                for key, value in args['args'].items():
                    t = self.instructions[prog].copy()
                    t.pop(0)
                    if key in t:
                        n += 1
                if n == len(t):
                    self.instructions[prog][0](**args['args'])
                else:
                    self.error(10)

        else:
            n = 0
            for key, value in args['args'].items():
                t = self.instructions[prog].copy()
                t.pop(0)
                if key in t:
                    n += 1

            if n == len(t):
                self.instructions[prog][0](**args['args'])
            else:
                self.error(10)

if __name__ == '__main__':
    from __init__ import *
