#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter.simpledialog import *
from confr import *
import os

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
        data = askstring(self.title, lg('keyword') + ' : ')
        self.dialoging = False
        if data:
            return data.replace(' ', '+')
        else:
            return None

    def open_internet(self, url):
        os.system(self.cmd_nav + ' ' + url)

if __name__ == '__main__':
    from __init__ import *
