#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from ext.prog import *
#from ext.compta import *
#from ext.temps import *

class Extensions(Program):
    def load_ext(self, menu):
        self.import_ext()
        self.draw_ext(menu)
        ""

if __name__ == '__main__':
    from __init__ import *
