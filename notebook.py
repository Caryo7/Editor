from tkinter import *
from tkinter.ttk import *
from PIL import *
from pathlib import Path

class FileList:
    def __init__(self,
                 parent,
                 width = 300,
                 height=30,
                 imgs = ('./image/16x16/close.png', './image/16x16/rightarrow.png', './image/16x16/leftarrow.png', './image/16x16/unsaved.png', './image/16x16/saved.png'),
                 onglets = [{'title': 'G:\\Untitled.x', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°1.form', 'stat': True},
                            {'title': 'G:\\Exe\\Test n°2.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°3.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°4.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°5.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°6.form', 'stat': True},
                            {'title': 'G:\\Exe\\Test n°7.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°8.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°9.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°10.form', 'stat': True},
                            {'title': 'G:\\Exe\\Test n°11.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°12.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°13.form', 'stat': True},
                            {'title': 'G:\\Exe\\Test n°14.form', 'stat': False},
                            {'title': 'G:\\Exe\\Test n°15.form', 'stat': False},],
                 cmd = lambda item: print('Vous voulez fermer :', item)):

        self.parent = parent
        
        self.master = Canvas(parent, width = width, height = height+1, bd=0, highlightthickness=0)
        self.x = 0
        self.y = 0
        self.width, self.height = width, height
        self.onglets = onglets
        self.img = imgs
        self.image = PhotoImage(file = imgs[0], master = parent)
        self.next_img = PhotoImage(file = imgs[1], master = parent)
        self.prev_img = PhotoImage(file = imgs[2], master = parent)
        self.usd_img = PhotoImage(file = imgs[3], master = parent)
        self.sd_img = PhotoImage(file = imgs[4], master = parent)
        self.cmd = cmd
        self.size = (130+20, 5)
        self.parent.minsize(self.size[0] + 80, 100)
        self.master.bind('<Button-1>', self.close)
        self.deb = 1

        self.draw()

    def draw(self):
        self.master.delete('all')
        x = 5
        b = False
        self.size_maxi = int((self.size[0] - 20) / 10)

        n = 0
        ps = 0
        for file in self.onglets:
            n += 1
            if n >= self.deb and (ps + 1) * (self.size[0] + 5) < self.width - 60:
                ps += 1
                p = Path(file['title'])
                name = file['title'].replace(str(p.parent), '')
                name = name.replace('\\', '')
                name = name.replace('/', '')
                if len(name) > self.size_maxi:
                    name = name[:self.size_maxi - 3] + '...'
    
                self.master.create_rectangle(x, self.height, x+self.size[0], self.size[1])
                self.master.create_image(x + 12, (self.size[1] + self.height) / 2, image = self.image)
                self.master.create_image(x + 33, (self.size[1] + self.height) / 2, image = self.sd_img if file['stat'] else self.usd_img)
                self.master.create_text((x + 30 + x + self.size[0])/2, (self.size[1] + self.height) / 2, text = name, font = ('Consolas', 10))
                x += self.size[0] + 5
            else:
                b = True

        if b:
            nx = Button(self.master, image = self.next_img, command = self.page_next)
            pv = Button(self.master, image = self.prev_img, command = self.page_prev)
            nx.config(width = 20)
            pv.config(width = 20)

            self.master.create_window(self.width - 20, (self.height + self.size[1])/2, window = nx)
            self.master.create_window(self.width - 45, (self.height + self.size[1])/2, window = pv)

        self.parent.update()

    def page_next(self):
        self.deb += 1
        self.draw()

    def page_prev(self):
        if self.deb > 1:
            self.deb -= 1
            self.draw()

    def add(self, file, stat = False):
        self.onglets.append({'title': file, 'stat': stat})
        self.draw()

    def change(self, item, file = None, stat = None):
        it = self.onglets[item]
        if file:
            it['file'] = file
        if stat != None:
            it['stat'] = stat

        self.onglets[item] = it
        self.draw()

    def remove(self, item):
        self.onglets.pop(item)
        self.draw()

    def config(self, img = None, cmd = None):
        if img:
            self.img = img
            self.image = PhotoImage(file = img[0], master = self.parent)
            self.next_img = PhotoImage(file = img[1], master = parent)
            self.prev_img = PhotoImage(file = img[2], master = parent)
            self.usd_img = PhotoImage(file = imgs[3], master = parent)
            self.sd_img = PhotoImage(file = imgs[4], master = parent)
        if cmd:
            self.cmd = cmd

    def close(self, evt):
        x = evt.x
        y = evt.y
        if self.size[1] <= y <= self.height:
            x -= 5
            item = int(x / (self.size[0] + 5))
            x -= item * (self.size[0] + 5)
            x -= 5
            item += (self.deb - 1)
            if 0 <= x <= 16 and item < len(self.onglets):
                self.cmd(item)

    def place(self, x = -1, y = -1, height = -1, width = -1):
        if x != self.x and x >= 0:
            self.master.place(x = x)
            self.x = x
        if y != self.y and y >= 0:
            self.master.place(y = y)
            self.y = y
        if height != self.height and height  >= 0:
            self.master.config(height = height)
            self.height = height
            self.master.place(height = height)
        if width != self.width and width >= 0:
            self.master.config(width = width)
            self.width = width
            self.master.place(width = width)

        self.draw()

    def grid(self, *arg, **kwargs):
        self.master.grid(*arg, **kwargs)

    def pack(self, *arg, **kwargs):
        self.master.pack(*arg, **kwargs)


o = 0
def htest():
    global o
    root = Tk()
    root.title('Test des onglets de fichier')
    root.geometry('1000x300')
    root.minsize(200, 300)
    nb = FileList(root, width = 1000)
    def rm(item):
        nb.remove(item)

    nb.config(cmd = rm)
    nb.place(x = 0, y = 30)
    o = root.winfo_width()

    def conf(evt):
        global o
        w = evt.widget.winfo_width()
        rap = o/w
        if rap > 1:
            rap = 1 - (rap-1)

        if w != o and 1 >= rap >= 0.8:
            o = w
            nb.place(width = w)
        elif w == root.winfo_screenwidth():
            nb.place(width = w)

    root.bind('<Configure>', conf)
    import time
    time.sleep(2)
    nb.change(0, stat = True)
    root.mainloop()


if __name__ == '__main__':
    htest()
