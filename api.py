from tkinter.simpledialog import *
from tkinter.messagebox import *
from confr import *
from pypresence import Presence
import os
import sys
import platform
import wmi
import psutil
import cpuinfo
import time

class API: # Gère les interactions avec les autres interfaces
    def updateDiscordStatut(self, first = False): # Actualise le profile sur l'application Discord
        if not get_discord_mode():
            return

        try:
            n = 1
            name_file = '' # Nom du fichier en cours (sans son arborescence)
            if self.path == '':
                name_file = ''
            elif self.path.count('/') + self.path.count('\\') == 0:
                name_file = self.path
            else:
                while self.path[-n] not in ('/', '\\'):
                    n += 1
                n -= 1
                name_file = self.path[-n:]

            if first:
                self.begin_time_RPC = time.time()
                stat = 'Program just began...' # Si pas de fichiers ouverts, affiche ce message
            else:
                stat = 'In ' + name_file

            self.RPC.update(
                state = stat,
                large_image = 'icon', # Grand icone Editor
                buttons = [{'label': lg('foundus'), 'url': self.URL}], # Bouton d'accès au site internet
                pid = os.getpid(), # PID Du process Python
                start = self.begin_time_RPC, # Temps de démarrage depuis la connexion au RPC
                large_text = 'Editor', # Texte de la grande image
                small_image = 'tarino', # Petite image : logo de Tarino Inc.
                small_text = lg('Builttar'), # Petit texte de la petite image
                details = lg('editor_infos'), # Informations sur l'Editor
                )

        except:
            pass # Si pas de connexion, ou pas de discord sur la machine, ne fait rien

    def __api__(self):
        self.cmd_nav = get_nav() # Trouve le navigateur à utiliser (confr.py)
        self.url_nav = get_url() # Trouve l'URL de recherche type (confr.py)
        if not get_discord_mode():
            return

        client_id = '1150423743546523720' # Client d'application Discord
        try:
            self.RPC = Presence(client_id) # Démarre la présence sur Discord
            self.RPC.connect()
            self.updateDiscordStatut(True) # Met à jour le statut (voir au dessus)
        except Exception:
            pass

    def internet_research(self): # Fait une recherche internet, depuis la commande type et le navigateur
        data = self.bresearch() # Récupère le/les mots clefs
        if data:
            os.popen(self.cmd_nav + ' ' + self.url_nav.replace('$', data)) # Lance la commande

    def bresearch(self): # Demande un ou plusieurs mots clef à l'utilisateur
        if self.dialoging:
            return

        self.dialoging = True
        data = askstring(self.title, lg('keyword') + ' : ', parent = self.master)
        self.dialoging = False
        if data:
            return data.replace(' ', '+')
        else:
            return None # Si pas de données

    def open_internet(self, url): # Ouvre le navigateur
        os.system(self.cmd_nav + ' ' + url)

    def info_sys(self): # Renvoie les informations du système
        pc = wmi.WMI()
        sm = pc.Win32_ComputerSystem()[0]
        os_info = pc.Win32_operatingSystem()[0]
        pf = platform.uname()
        cpu = cpuinfo.get_cpu_info()
        cm = pc.Win32_Processor()[0]
        vdc = pc.Win32_VideoController()[0]

        showinfo(lg('info'), 'Caractéristiques Système :' +
                 '\n\n\nEnsemble HARDWARE :\n' +
                 f'\nMémoire RAM : {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} Go' +
                 '\nNombre de processeurs : ' + str(sm.NumberOfProcessors) + ' ' +
                 '\nMachine : ' + str(pf.machine) + ' ' +
                 '\nMarque : ' + str(sm.Manufacturer) + ' ' +
                 '\nModèle : ' + str(sm.Model) + ' ' +
                 
                 '\n\n\nProcesseurs :\n' + 
                 '\nProcesseur : ' + str(cm.Caption) + ' ' +
                 '\nMarque : ' + str(cm.Manufacturer) + '' +
                 '\nNom du CPU : ' + str(cpu['brand_raw']) + ' ' +
                 '\nNombre de coeurs physiques : ' + str(cm.NumberOfCores) +
                 '\nNombre de coeurs Logiques : ' + str(cm.NumberOfLogicalProcessors) + ' ' +
                 '\nArchitecture processeur : ' + str(cpu['arch']) + ' ' +
                 '\nFréquence Maximale : ' + str(psutil.cpu_freq().max / 1000) + ' GHz' +
                 '\nTaille du cache L2 : ' + str(cm.L2CacheSize) + ' Ko' +
                 '\nTaille du cache L3 : ' + str(cm.L3CacheSize) + ' Ko' +

                 '\n\n\nCarte Graphique :\n' +
                 '\nModèle : ' + str(vdc.VideoProcessor) + ' ' +
                 '\nMarque : ' + str(vdc.AdapterCompatibility) + ' ' +
                 '\nRésolution : ' + str(vdc.CurrentHorizontalResolution) + ' x ' + str(vdc.CurrentVerticalResolution) + ' Pixels' +
                 f'\nCouleurs : {int(vdc.CurrentNumberOfColors)/1024/1024/1024:.2f} Milliards' +
                 '\nOcters par Pixels : ' + str(vdc.CurrentBitsPerPixel) + ' ' +
                 '\nTaux de rafraichissement : ' + str(vdc.CurrentRefreshRate) + ' Hz' +
                 '\nVersion du Driver : ' + str(vdc.DriverVersion) + ' ' + 
                 
                 '\n\n\nSystème d\'exploitation :\n' + 
                 '\nSystème d\'explotaition : ' + str(pf.system) + ' ' +
                 '\nRelease : ' + str(pf.release) + ' ' +
                 '\nVersion : ' + str(pf.version) + ' ' +
                 '\nNom du noeud : ' + str(pf.node) + ' ' +
                 '\nType de système : ' + str(sm.SystemType) + ' ' +
                 '\nFamille de système : ' + str(sm.SystemFamily) + ' ' +
                 '\nUtilisateur : ' + str(sm.Name) + ' ' +
                 '\nNuméro de Série : ' + str(os_info.SerialNumber) + ' ')
                 #'\n : ' + str() + ' ' + 

if __name__ == '__main__':
    from __init__ import *
