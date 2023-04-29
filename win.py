#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from threading import *
import time, os, sys, time, zroya

from confr import *

class notif_destroy(Thread):
    def __init__(self, icon, title, path, version, url):
        Thread.__init__(self)
        self.icon = icon
        self.title = title
        self.path = path
        self.VERSION = version
        self.url = url

    def run(self):
        #time.sleep(5)
        if zroya.init(self.title, 'a', 'b', 'c', 'd') and get_notifs():
            t = zroya.Template(zroya.TemplateType.ImageAndText4)
            t.setAudio(zroya.Audio.Default) #liste : Default, IM, Mail, Reminder, Call2-10, Call, Alarm, Alarm2-10)
            t.setImage(self.icon)
            t.setFirstLine(lg('back_tasks'))
            t.setSecondLine(lg('doc_notif'))
            t.addAction(lg('_Site'))
            t.addAction(lg('Tasks'))
            t.addAction(lg('dontshowagain'))
            t.setAttribution(self.title + lg('auto_notif'))

            def button(nid, action_id):
                if action_id == 0:
                    os.system('start ' + self.url)
                elif action_id == 1:
                    os.system('taskmgr')
                elif action_id == 2:
                    write('global', 'notifs', '0')

            def clique(nid): # nid pour notification ID
                os.system('taskmgr')

            def onDismissHandler(nid, reason):
                pass ## Quand on ferme la norification

            def onFailHandler(nid):
                pass ## Si erreur lors de la notification (genre : elle est bloquée)

            zroya.show(t, on_action=button, on_fail=onFailHandler, on_dismiss = onDismissHandler, on_click = clique)


class Win:
    def __win__(self):
        try:
            self.master = Tk()
        except TclError:
            os.system('cls' if sys.platform == 'Win32' else 'clear')
            print("##########################################################################################")
            print('##                                                                                      ##')
            print("## Problème de niveau 1 : Le système opérant ne propose pas d'environnement graphique ! ##")
            print("## Veuillez résoudre ce problème selon l'administrateur système !                       ##")
            print('##                                                                                      ##')
            print("##########################################################################################")
            input()
            return False

        self.master.title(self.title + ' - Untitled.x')
        self.master.protocol('WM_DELETE_WINDOW', self.Quitter)
        self.master.iconbitmap(self.ico['win'])
        self.lns = get_ln()
        self.dark = get_dark()
        self.dialoging = False
        self.add_task(code='ClosingAutoAsk', time=time.time(), desc='MAIN_LOOP\nThis short program ask to the user is he want to save his work before closing. If work is already saved, it does not ask anything')
        return True

    def fermer(self, evt = None):
        self.clear_text()
        self.stat_text(False)
        self.update_line_numbers()
        self.menufichier.entryconfig(lg('settings'), stat = 'disabled')
        self.master.title(self.title + ' - ' + lg('NFO'))

    def bloc_try(self, ifnormal, exception = Exception, iferror = None):
        try:
            ifnormal()
        except exception:
            if iferror != None:
                iferror()

    def protocol_dialog(self, tk):
        tk.destroy()
        self.dialoging = False
        
    def Quitter(self, evt=None):
        def destroy():
            self.master.destroy()

            #self.ast._stop = Event()
            #self.check_update._stop = Event()
            #self.bloc_try(self.ast._stop.set)
            #self.bloc_try(self.check_update._stop.set)

            i = notif_destroy(self.ico['win'],
                              self.title,
                              self.path_prog,
                              self.VERSION,
                              self.URL)

            i.start()

        if self.saved == False or self.saved == None or get_askclose:
            dem = askyesnocancel(self.title, lg('DYWTS'))
            if dem == True:
                self.save()
                destroy()
                self.programme_termine = True
                # raise KeyboardInterrupt
                # exit(code='ClosedByUserWithSave')

            elif dem == False:
                destroy()
                self.programme_termine = True
                # raise KeyboardInterrupt
                # exit(code='ClosedByUserWithoutSave')

        else:
            destroy()
            # raise KeyboardInterrupt
            # exit(code='ClosedByUserWithAutoSave')
        
    def Generate(self):
        self.master.focus_force()
        self.text.focus()
        self.master.mainloop()

if __name__ == '__main__':
    from __init__ import *
