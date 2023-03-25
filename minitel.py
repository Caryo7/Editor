#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
from errors import *
try:
    import serial # serial ou pyserial ?
except ImportError:
    ERROR(6)
    
from tkinter import *
from confr import *
from ulla import *

class Pynitel:
    def __pynitel__(self, port='/dev/ttyACM0', vitesse=4800, bytesize=7, timeout=2):
        self.ecrans = {'last': None}
        try:
            self.conn = serial.Serial(port, vitesse, parity=serial.PARITY_EVEN, bytesize=bytesize, timeout=timeout)
        except Exception:
            if get_alerte_min():
                ERROR(9)

            self.conn = None

        self.lastkey = 0
        self.lastscreen = ''
        self.laststar = False
        self.zones = []
        self.zonenumber = 0
        self.noir = 0
        self.rouge = 1
        self.vert = 2
        self.jaune = 3
        self.bleu = 4
        self.magenta = 5
        self.cyan = 6
        self.blanc = 7
        self.envoi = 1
        self.retour = 2
        self.repetition = 3
        self.guide = 4
        self.annulation = 5
        self.sommaire = 6
        self.correction = 7
        self.suite = 8
        self.connexionfin = 9
        self.PRO1 = '\x1b\x39'
        self.PRO2 = '\x1b\x3a'
        self.PRO3 = '\x1b\x3b'
        
    def wait(self):
        if self.conn is not None:
            while self.conn.read(1) != b' ':time.sleep(1)
            
    def end(self):
        if self.conn is not None:self.conn.write(b'\x1b9g')

    def _if(self):
        if self.conn is not None:
            data = self.conn.read()
            if not data:return None
            else:return data

    def clear(self):
        if self.conn is not None:
            self.conn.settimeout(0)
            self.conn.recv(10000)

    def home(self):
        if self.conn is not None:
            self._del(0, 1)
            self.sendchr(12)
            self.cursor(False)

    def vtab(self, ligne):self.pos(ligne, 1)
    
    def pos(self, ligne, colonne=1):
        if ligne == 1 and colonne == 1:self.sendchr(30)
        else:
            self.sendchr(31)
            self.sendchr(64+ligne)
            self.sendchr(64+colonne)
            
    def _del(self, ligne, colonne):
        self.pos(ligne, colonne)
        self.sendchr(24)
        
    def normal(self):self.sendesc('I')
    
    def backcolor(self, couleur):self.sendesc(chr(80+couleur))
    
    def canblock(self, debut, fin, colonne, inverse=False):
        if inverse is False:
            self.pos(debut, colonne)
            self.sendchr(24)
            for ligne in range(debut, fin):
                self.sendchr(10)
                self.sendchr(24)
        else:
            self.pos(fin, colonne)
            self.sendchr(24)
            for ligne in range(debut, fin):
                self.sendchr(11)
                self.sendchr(24)
                
    def caneol(self, ligne, colonne):
        self.pos(ligne, colonne)
        self.sendchr(24)
        
    def cls(self):self.home()
    
    def color(self, couleur):self.sendesc(chr(64+couleur))
    
    def cursor(self, visible):
        if visible == 1 or visible is True:self.sendchr(17)
        else:self.sendchr(20)
        
    def draw(self, num=0):
        if self.conn is not None:
            if num is None:num = self.ecrans['last']
            self.ecrans['last'] = num
            if num is not None:self.conn.write(self.ecrans[num])
        
    def drawscreen(self, fichier):
        if self.conn is not None:
            with open(fichier, 'rb') as f:self.conn.write(f.read())
    def flash(self, clignote=True):
        if clignote is None or clignote is True or clignote == 1:self.sendesc('\x48')
        else:self.sendesc('\x49')
        
    def forecolor(self, couleur):self.color(couleur)
    
    def get(self):
        if self.conn is not None:
            return(self.conn.read(self.conn.in_waiting).decode())

    def getid(self):
        print("getid: non implémenté...")
        return
    def hcolor(self, couleur):self.sendesc(chr(80+couleur))
    
    def input(self, ligne, colonne, longueur, data='', caractere='.', redraw=True):
        if self.conn is not None:
            if redraw:
                self.sendchr(20)
                self.pos(ligne, colonne)
                self._print(data)
                self.plot(caractere, longueur-len(data))
            self.pos(ligne, colonne+len(data))
            self.sendchr(17)
            while True:
                c = self.conn.read(1).decode()
                if c == '':continue
                elif c == '\x13':
                    c = self.conn.read(1).decode()
                    if c == '\x45' and data != '':
                        data = ''
                        self.sendchr(20)
                        self.pos(ligne, colonne)
                        self._print(data)
                        self.plot(caractere, longueur-len(data))
                        self.pos(ligne, colonne)
                        self.sendchr(17)
                    elif c == '\x47' and data != '':
                        self.send(chr(8)+caractere+chr(8))
                        data = data[:len(data)-1]
                    else:
                        self.lastkey = ord(c)-64
                        self.laststar = (data != '' and data[:-1] == '*')
                        return(data, ord(c)-64)
                elif c == '\x1b':
                    c = c + self.conn.read(1).decode()
                    if c == self.PRO1:self.conn.read(1)
                    elif c == self.PRO2:self.conn.read(2)
                    elif c == self.PRO3:self.conn.read(3)
                elif c >= ' ' and len(data) >= longueur:self.bip()
                elif c >= ' ':data = data + c
            
    def inverse(self, inverse=1):
        if inverse is None or inverse == 1 or inverse is True:self.sendesc('\x5D')
        else:self.sendesc('\x5C')
        
    def locate(self, ligne, colonne):self.pos(ligne, colonne)
    
    def lower(self, islower=True):
        if islower or islower == 1:self.send(self.PRO2+'\x69\x45')
        else:self.send(self.PRO2+'\x6a\x45')
        
    def message(self, ligne, colonne, delai, message, bip=False):
        if bip:self.bip()
        self.pos(ligne, colonne)
        self._print(message)
        self.conn.flush()
        time.sleep(delai)
        self.pos(ligne, colonne)
        self.plot(' ', len(message))
        
    def printscreen(self, fichier):self.drawscreen(fichier)
    
    def resetzones(self):
        while len(self.zones) > 0:self.zones.pop()
        
    def starflag(self):return(self.laststar)
    
    def underline(self, souligne=True):
        if souligne is None or souligne is True or souligne == 1:self.sendesc(chr(90))
        else:self.sendesc(chr(89))
        
    def waitzones(self, zone):
        if len(self.zones) == 0:return (0, 0)
        zone = -zone
        while True:
            if zone <= 0:
                self.cursor(False)
                for z in self.zones:
                    self.pos(z['ligne'], z['colonne'])
                    if z['couleur'] != self.blanc:self.forecolor(z['couleur'])
                    self._print(z['texte'])
                if zone < 0:zone = -zone
            (self.zones[zone-1]['texte'], touche) = self.input(self.zones[zone-1]['ligne'], self.zones[zone-1]['colonne'], self.zones[zone-1]['longueur'], data=self.zones[zone-1]['texte'], caractere='.', redraw=False)
            if touche == self.suite:
                if zone < len(self.zones):zone = zone+1
                else:zone = 1
            elif touche == self.retour:
                if zone > 1:zone = zone-1
                else:zone = len(self.zones)
            else:
                self.zonenumber = zone
                self.cursor(False)
                return(zone, touche)
            
    def zone(self, ligne, colonne, longueur, texte, couleur):self.zones.append({"ligne": ligne, "colonne": colonne, "longueur": longueur, "texte": texte, "couleur": couleur})
    
    def key(self):return self.lastkey
    
    def scale(self, taille):self.sendesc(chr(76+taille))
    
    def notrace(self):self.sendesc(chr(89))
    
    def trace(self):self.sendesc(chr(90))
    
    def plot(self, car, nombre):
        if nombre > 1:self._print(car)
        if nombre == 2:self._print(car)
        elif nombre > 2:
            while nombre > 63:
                self.sendchr(18)
                self.sendchr(64+63)
                nombre = nombre-63
            self.sendchr(18)
            self.sendchr(64+nombre-1)
            
    def text(self):self.sendchr(15)
    
    def gr(self):self.sendchr(14)
    
    def step(self, scroll):
        self.sendesc(':')
        self.sendchr(ord('j')-scroll)
        self.send('C')
        
    def xdraw(self, fichier):
        if self.conn is not None:
            with open(fichier, 'rb') as f:self.conn.write(f.read())
            
    def load(self, num, fichier):
        with open(fichier, 'rb') as f:
            data = f.read()
            self.ecrans[num] = data
            
    def read(self):print('read: non implémenté')
    
    def _print(self, texte):self.send(self.accents(texte))
    
    def send(self, text):
        if self.conn is not None:
            if self.conn is not None:self.conn.write(text.encode())
            else:print('conn = None')
            
    def sendchr(self, ascii):self.send(chr(ascii))
    
    def sendesc(self, text):
        self.sendchr(27)
        self.send(text)
        
    def bip(self):self.sendchr(7)
    
    def accents(self, text):
        text = text.replace('à', '\x19\x41a')
        text = text.replace('â', '\x19\x43a')
        text = text.replace('ä', '\x19\x48a')
        text = text.replace('è', '\x19\x41e')
        text = text.replace('é', '\x19\x42e')
        text = text.replace('ê', '\x19\x43e')
        text = text.replace('ë', '\x19\x48e')
        text = text.replace('î', '\x19\x43i')
        text = text.replace('ï', '\x19\x48i')
        text = text.replace('ô', '\x19\x43o')
        text = text.replace('ö', '\x19\x48o')
        text = text.replace('ù', '\x19\x43u')
        text = text.replace('û', '\x19\x43u')
        text = text.replace('ü', '\x19\x48u')
        text = text.replace('ç', '\x19\x4Bc')
        text = text.replace('°', '\x19\x30')
        text = text.replace('£', '\x19\x23')
        text = text.replace('Œ', '\x19\x6A').replace('œ', '\x19\x7A')
        text = text.replace('ß', '\x19\x7B')
        text = text.replace('¼', '\x19\x3C')
        text = text.replace('½', '\x19\x3D')
        text = text.replace('¾', '\x19\x3E')
        text = text.replace('←', '\x19\x2C')
        text = text.replace('↑', '\x19\x2D')
        text = text.replace('→', '\x19\x2E')
        text = text.replace('↓', '\x19\x2F')
        text = text.replace('̶', '\x60')
        text = text.replace('|', '\x7C')
        text = text.replace('À', 'A').replace('Â', 'A').replace('Ä', 'A')
        text = text.replace('È', 'E').replace('É', 'E')
        text = text.replace('Ê', 'E').replace('Ë', 'E')
        text = text.replace('Ï', 'I').replace('Î', 'I')
        text = text.replace('Ô', 'O').replace('Ö', 'O')
        text = text.replace('Ù', 'U').replace('Û', 'U').replace('Ü', 'U')
        text = text.replace('Ç', 'C')
        return(text)

class Minitel(Pynitel, Ulla):
    def __min__(self):
        inf = get_min_info()
        self.__pynitel__(port=inf['dev'], vitesse=inf['speed'], bytesize=inf['bs'], timeout=inf['to'])
        
    def send_file(self):
        self._print(self.text.get('0.0', END))

if __name__ == '__main__':
    t = Minitel()
    t.__pynitel__()
    t.home()
    t.ulla()

if __name__ == '__main__':
    from __init__ import *
