#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from confr import *

class RecentFileList:
    def __recentfl__(self):
        ""

    def get_rfl(self):
        f = open(self.path_prog + '/recent_file_list.log', 'r', encoding = get_encode())
        r = f.readlines()
        f.close()
        l = []
        for i in range(len(r)):r[i] = r[i].replace('\n', '')
        for i in range(10):
            try:
                l.append((i, r[len(r) - i - 1]))
            except IndexError:
                break
        return l

    def add_f(self, name):
        f = open(self.path_prog + '/recent_file_list.log', 'a', encoding = get_encode())
        f.write(name + '\n')
        f.close()

    def clear_recent(self):
        if self.mode_record:
            self.events.append({'command': 'clear_recent'})

        f = open(self.path_prog + '/recent_file_list.log', 'w', encoding = get_encode())
        f.close()

if __name__ == '__main__':
    from __init__ import *
