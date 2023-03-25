#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *

class ToolTip(object):
    id = None
    tw = None

    def __init__(self, widget, text='widget info', color = '#FFFFEA', waittime = 500, wraplength = 270, relief = 'solid', borderwidth = 1, justify = 'left'):
        self.relief = relief
        self.borderwidth = borderwidth
        self.justify = justify
        self.color = color
        self.widget = widget
        self.text = text
        self.waittime = waittime
        self.wraplength = wraplength
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify=self.justify, background=self.color, relief=self.relief, borderwidth=self.borderwidth, wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()

"""class CallTip:
    id = None
    tw = None

    def __init__(self, widget, text = 'widget prefixe auto completition', color = 'white', waittime = 500, wraplength = 180, relief = 'solid', borderwidth = 1, justify = 'left'):
        self.relief = relief
        self.borderwidth = borderwidth
        self.justify = justify
        self.color = color
        self.widget = widget
        self.text = text
        self.waittime = waittime
        self.wraplength = wraplength
        self.widget.bind("<Leave>", self.leave)

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        self.tw = Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(self.tw, text=self.text, justify=self.justify, background=self.color, relief=self.relief, borderwidth=self.borderwidth, wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()"""

if __name__ == '__main__':
    root = Tk()
    btn1 = Button(root, text="button 1")
    btn1.pack(padx=10, pady=5)
    button1_ttp = ToolTip(btn1, \
    'Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, '
    'consectetur, adipisci velit. Neque porro quisquam est qui dolorem ipsum '
    'quia dolor sit amet, consectetur, adipisci velit. Neque porro quisquam '
    'est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit.', color = '#FFFFEA')

    btn2 = Button(root, text="button 2")
    btn2.pack(padx=10, pady=5)
    button2_ttp = ToolTip(btn2, \
    "First thing's first, I'm the realest. Drop this and let the whole world "
    "feel it. And I'm still in the Murda Bizness. I could hold you down, like "
    "I'm givin' lessons in  physics. You should want a bad Vic like this.", color = '#FFFFEA')
    #CallTip(btn2)
    root.mainloop()

