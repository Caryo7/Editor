#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter.simpledialog import *
from tkinter.messagebox import *
from confr import *
import os
import sys
import platform
import wmi
import psutil
import cpuinfo

class API:
    def __api__(self):
        self.cmd_nav = get_nav()
        self.url_nav = get_url()

    def internet_research(self):
        data = self.bresearch()
        if data:
            os.system(self.cmd_nav + ' ' + self.url_nav.replace('$', data))

    def bresearch(self):
        if self.dialoging:
            return

        self.dialoging = True
        data = askstring(self.title, lg('keyword') + ' : ', parent = self.master)
        self.dialoging = False
        if data:
            return data.replace(' ', '+')
        else:
            return None

    def open_internet(self, url):
        os.system(self.cmd_nav + ' ' + url)

    def info_sys(self):
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
    API.info_sys(None)
