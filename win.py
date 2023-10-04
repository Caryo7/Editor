#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.simpledialog import *
from tkinterdnd2 import *
from threading import *
import time
import os
import sys
import time
import zroya
import signal

from confr import *

class notif_destroy(Thread):
    def __init__(self, icon, title, path, version, url):
        Thread.__init__(self)
        self.icon = icon
        self.title = title
        self.path = path
        self.VERSION = version
        self.url = url

    def EOP(self):
        os.kill(os.getpid(), signal.SIGINT)#signal.SIGKILL

    def run(self):
        if zroya.init(self.title, 'a', 'b', 'c', 'd') and get_notifs():
            time.sleep(60)

            t = zroya.Template(zroya.TemplateType.ImageAndText4)
            t.setAudio(zroya.Audio.Default) # liste : Default, IM, Mail, Reminder, Call2-10, Call, Alarm, Alarm2-10)
            t.setImage(self.icon)
            t.setFirstLine(lg('back_tasks'))
            t.setSecondLine(lg('doc_notif'))
            t.addAction(lg('_Site'))
            t.addAction(lg('Tasks'))
            t.addAction(lg('dontshowagain'))
            t.setExpiration(3)
            t.setAttribution(self.title + lg('auto_notif'))

            def button(nid, action_id):
                if action_id == 0:
                    os.system('start ' + self.url)
                    self.EOP()
                elif action_id == 1:
                    os.system('taskmgr')
                    self.EOP()
                elif action_id == 2:
                    write('global', 'notifs', '0')
                    self.EOP()

            def clique(nid): # nid pour notification ID
                os.popen('taskmgr')
                self.EOP()

            def onDismissHandler(nid, reason):
                self.EOP()
                ## Quand on ferme la norification

            def onFailHandler(nid):
                self.EOP()
                ## Si erreur lors de la notification (genre : elle est bloquée)

            zroya.show(t, on_action=button, on_fail=onFailHandler, on_dismiss = onDismissHandler, on_click = clique)

        else:
            self.EOP()


class Win:
    def __win__(self):
        try:
            self.master = TkinterDnD.Tk()
        except TclError:
            os.system('cls' if sys.platform == 'Win32' else 'clear')
            os.system('color a' if sys.platform == 'Win32' else '')
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
        if sys.platform == 'win32':
            self.master.iconbitmap(self.ico['win'])

        self.lns = get_ln()
        self.dark = get_dark()
        self.dialoging = False
        self.add_task(code='ClosingAutoAsk', time=time.time(), desc='MAIN_LOOP\nThis short program ask to the user is he want to save his work before closing. If work is already saved, it does not ask anything')
        return True

    def fermer(self, evt = None):
        if (self.saved == False or self.saved == None) and get_askclose():
            dem = askyesnocancel(self.title, lg('DYWTS'))
            if dem == True:
                self.save()
            elif dem == None:
                return 'cancel'

        if self.mode_record:
            self.events.append({'command': 'close', 'evt': evt})

        self.update_time()

        self.clear_text()
        self.stat_text(False)
        self.update_line_numbers()
        self.stat_form_infos(False)
        self.act_color = None
        self.path = ''
        self.master.title(self.title + ' - ' + lg('NFO'))
        self.saved = None
        self.savedd = False
        self.nofileopened = True
        self.meta = {}
        self.variables = {}
        return 'exit'

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
            i = notif_destroy(self.ico['win'],
                              self.title,
                              self.path_prog,
                              self.VERSION,
                              self.URL)
            i.start()
            #i.EOP()

        f = self.fermer()
        
        if self.mode_record:
            self.events.append({'command': 'quit', 'evt': evt})

        if f == 'exit':
            destroy()
            self.programme_termine = True
            # raise KeyboardInterrupt
            # exit(code='ClosedByUserWithoutSave')

        self.dialoging = False
        
    def Generate(self):
        if not self.mainlooped:
            self.mainlooped = True
            self.master.focus_force()
            self.text.focus()
            self.conf_win(generate = True)
            self.master.mainloop()


if __name__ == '__main__':
    from __init__ import *

