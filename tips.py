from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import ImageTk
from tooltip import *
from confr import *
import json


class TipsWin:
    def __init__(self, master, icon, title, nb, text, next_cmd, prev_cmd, dam_cmd, path_prog):
        self.next_cmd, self.prev_cmd, self.dam_cmd = next_cmd, prev_cmd, dam_cmd
        self.path_prog = path_prog
        self.root = Toplevel(master)
        self.root.transient(master)
        self.root.title(title)
        self.root.resizable(False, False)
        self.root.protocol('WM_DELETE_WINDOW', self.destroy)
        self.root.iconbitmap(icon)

        wrap = 300

        self.next_img = ImageTk.PhotoImage(master = master, file = self.path_prog + '/image/16x16/RightArrowIcon.png')
        self.close_img = ImageTk.PhotoImage(master = master, file = self.path_prog + '/image/16x16/CloseIcon.png')
        self.prev_img = ImageTk.PhotoImage(master = master, file = self.path_prog + '/image/16x16/LeftArrowIcon.png')

        self.label = Label(self.root, text = text, font = ('Consolas', 10), wraplength = wrap)
        self.label.grid(row = 0, column = 1, padx = 5, pady = 5, rowspan = 3)
        b1 = Button(self.root, image = self.next_img, command = self.up, relief = FLAT)
        b1.grid(row = 0, column = 0, padx = 1, pady = 1)
        b2 = Button(self.root, image = self.close_img, command = self.destroy, relief = FLAT)
        b2.grid(row = 1, column = 0, padx = 1, pady = 1)
        b3 = Button(self.root, image = self.prev_img, command = self.down, relief = FLAT)
        b3.grid(row = 2, column = 0, padx = 1, pady = 1)
        ToolTip(b1, text = lg('next_tip'))
        ToolTip(b2, text = lg('close'))
        ToolTip(b3, text = lg('prev_tip'))

        b4 = Button(self.root, text = lg('dontshowagain'), command = self.dontShowMore, width = 20)
        b4.grid(row = 3, column = 1, padx = 5, pady = 1)
        ToolTip(b4, text = lg('nomoretips'))

    def up(self):
        self.next_cmd()

    def down(self):
        self.prev_cmd()

    def destroy(self):
        self.root.destroy()

    def dontShowMore(self):
        self.root.destroy()
        self.dam_cmd()

    def change(self, value, title):
        self.label.config(text = value)
        self.root.title(title)


class JSon:
    def __init__(self, path, encoding = 'utf-8'):
        self.file = open(path, mode = 'r', encoding = encoding)
        self.data = json.load(self.file)

    def close(self):
        self.file.close()

    def tips_list(self):
        return list(self.data.keys())

    def infos(self, name):
        return self.data[name]


def OpenTips(path_prog):
    js = JSon(path_prog + '/tips.json')
    advices = []
    n = 0
    for tip in js.tips_list():
        n += 1
        advices.append((str(n) + '. ' + js.infos(tip)['title'], js.infos(tip)['content']))

    js.close()

    return advices


class Tips:
    tips_index = 0

    def start_tips(self):
        self.advices = OpenTips(self.path_prog)

        if not get_startTips():
            return
        if self.configurating:
            return

        self.start_tips_index(0)

    def start_tips_index(self, index):
        master = self.master
        title, text = self.advices[index]
        nb = self.tips_index
        next_cmd = lambda: self.next_tip()
        prev_cmd = lambda: self.prev_tip()
        dam_cmd = lambda: self.donotaskagain_tip()
        icon = self.ico['tips']
        
        self.tip_window = TipsWin(master, icon, title, nb, text, next_cmd, prev_cmd, dam_cmd, self.path_prog)

    def tip_update(self, index):
        title, text = self.advices[index]
        self.tip_window.change(text, title)

    def next_tip(self):
        self.tips_index += 1
        self.tips_index %= len(self.advices)
        self.tip_update(self.tips_index)

    def prev_tip(self):
        if self.tips_index < 0:
            self.tips_index = len(self.advices) - 1

        self.tips_index -= 1
        self.tip_update(self.tips_index)

    def donotaskagain_tip(self):
        write('global', 'tips', '0')


if __name__ == '__main__':
    from __init__ import *
