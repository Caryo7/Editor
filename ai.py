# Importations :

from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from configparser import ConfigParser
from threading import Thread
from humanize import  naturalsize
from confr import *
from switchbt import *
from llama_cpp import Llama

class ModelFounder(Thread): # NE MARCHE PAS ENCORE !!!
    def __init__(self, path_prog):
        Thread.__init__(self)
        self.path_prog = path_prog

    def found_list(self):
        self.mode = 'list'
        try:
            return [['a', 'information about a', 123456789, 'network', None],
                    ['a', 'information about a', 123456789, 'network', None],
                    ['a', 'information about a', 123456789, 'network', None],
                    ['a', 'information about a', 123456789, 'network', None],
                    ['a', 'information about a', 123456789, 'network', None],
                    ['a', 'information about a', 123456789, 'network', None],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],
                    ['a', 'information about a', 123456789, 'local', '/models/'],]

        except Exception:
            showerror('Téléchargeur', 'Votre connexion internet est inexistante. Merci de la vérifier puis de recommencer !')
            return []

    def found_model(self, name):
        return ''
        #return PATH_PROG + '/models/.bin'


class ModelAsker: # NE SERT A RIEN
    def __init__(self, master, icon, liste, cmd, act, online):
        self.cmd = cmd
        self.liste = liste
        self.online = online

        self.master = Toplevel(master)
        self.master.transient(master)
        self.master.title(lg('Models'))
        self.master.resizable(False, False)
        self.master.iconbitmap(icon)

        Label(self.master, text = 'Label actuel : ' + act, font = ('Courier', 11, 'italic')).place(x = 5, y = 5)
        self.sw = Switch(self.master, stat = not self.online, bg = '')
        self.sw.place(x = 5, y = 35)
        Label(self.master, text = 'Utiliser en mode hors ligne (télécharger)', font = ('Courier', 11)).place(x = 70, y = 35)

        scroll = ttk.Scrollbar(self.master, orient = 'vertical')
        self.tree = ttk.Treeview(self.master, height = 10, column = ('Name', 'Info', 'Size', 'Mode'), show = 'headings', yscrollcommand = scroll.set)
        scroll.config(command = self.tree.yview)
        self.tree.place(x = 10, y = 75)
        self.tree.column('Name', width = 150)
        self.tree.column('Info', width = 250)
        self.tree.column('Size', width = 50)
        self.tree.column('Mode', width = 65)

        self.tree.heading('Name', text = lg('name'))
        self.tree.heading('Info', text = lg('infos'))
        self.tree.heading('Size', text = lg('size'))
        self.tree.heading('Mode', text = lg('mode'))

        scroll.place(x = 10 + self.tree.winfo_reqwidth(), y = 75, height = self.tree.winfo_reqheight())
        self.master.geometry(str(20 + self.tree.winfo_reqwidth() + scroll.winfo_reqwidth()) + 'x' + str(85 + self.tree.winfo_reqheight()))

        for i in self.liste:
            self.tree.insert('', 'end', values = [i[0], i[1], naturalsize(i[2]), i[3]])


class AiFinisher: # Class sur l'IA du programme
    def __aifinisher__(self): # Défini les paramètres par défauts
        self.model = ''
        self.online = False
        self.mf = ModelFounder(self.path_prog)
        self.list_models = self.mf.found_list()

    def askModel(self): # Demande un modèle à utiliser (INCATIF)
        ma = ModelAsker(self.master, self.ico['ai'], self.list_models, lambda a: print(x), act = self.model, online = self.online)

    def invente_fin(self): # A partir du modèle de base, écrit la fin du texte
        llm = Llama(model_path = self.path_prog + "/models/Wizard-Vicuna-7B-Uncensored.ggmlv3.q8_0.bin") # Charge le modèle

        input_text = self.get_text() # Récupère le contenue de la zone de texte (sans l'influencer)
        output_text = llm(input_text, max_tokens=32, stop=["\n"], echo=True) # Lance la requette au modèle
        self.insert_text(output_text, with_vars = False) # Ajoute à la zone de texte le texte ainsi généré


if __name__ == '__main__':
    ""#from __init__ import *

    ## importing the main object of the binding library
    #from llama_cpp import Llama

    # creating a variable wich will contain the model runtime
    #llm = Llama(model_path="./models/Wizard-Vicuna-7B-Uncensored.ggmlv3.q8_0.bin")

    # creating an output variable with an input prompt & given settings for the llm
    #output = llm("Q: Name the planets in the solar system? A: ", max_tokens=32, stop=["Q:", "\n"], echo=True)

    # printing the output
    #print(output)
