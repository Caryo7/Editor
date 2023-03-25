from tkinter import *
from tkinter.messagebox import *
from threading import Thread
import time

main_self = None
def new_self(self):
    main_self = self

class GUI:
    # Boîtes de dialogue
    @classmethod
    def afficher(self, titre, texte):
        showinfo(titre, texte)

    # Créé une tache de fond :
    @classmethod
    def Tache(self, **args):
        class Task(Thread):
            def __init__(self, args):
                Thread.__init__(self)
                if args['self']:args['self'].add_task(args['titre'], time.time(), desc=args['description'])
                self.args = args
            def run(self):self.args['fonction']()

        args['self'] = main_self
        t = Task(args)
        t.start()

    @classmethod
    def Fenetre(self, **args):
        master = Tk()
        try:master.title(args['titre'])
        except KeyError:""
        try:master.resizable(args['agr_haut'], args['agr_larg'])
        except KeyError:""
        try:master.geometry(args['geometry'])
        except KeyError:""
        return master

if __name__ == '__main__':
    GUI.Fenetre()
