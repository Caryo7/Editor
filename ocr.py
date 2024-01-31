from progress import *
from threading import Thread
from tkinter import *
from confr import *
from pathlib import Path
from PIL import Image
from zipfile import *
from PyPDF2 import PdfReader
import os

try:
    print('Importing Keras OCR')
    import keras_ocr
    print('End importing')
except:
    print('no module keras_ocr !')

PATH_PROG = os.path.abspath(os.getcwd())

class Fichier:
    def __init__(self, name):
        n = len(name) - 1
        while name[n] != '.':
            n -= 1
        self.ext = name[n:]


class Traitement:
    kbt = ('azertyuiop qsdfghjklm wxcvbn',
           'qwertyuiop asdfghjkl zxcvbnm',
           'bépoè!vdljzw auie;ctsrnmç êàyx:k?qghf')

    sim = {'a': ('e', 'o'),
           'b': ('', ''),
           'c': ('', ''),
           'd': ('', ''),
           'e': ('o', 'a'),
           'f': ('', ''),
           'g': (',', ''),
           'h': ('n', ''),
           'i': ('l', 't', 'j', 'r'),
           'j': ('i', 'l', 't', 'r'),
           'k': ('', ''),
           'l': ('i', 't', 'j', 'r'),
           'm': ('', ''),
           'n': ('h', ''),
           'o': ('e', 'a'),
           'p': ('', ''),
           'q': ('', ''),
           'r': ('i', 'l', 't', 'j'),
           's': ('', ''),
           't': ('l', 'i', 'j', 'r'),
           'u': ('v', ''),
           'v': ('u', ''),
           'w': ('', ''),
           'x': ('', ''),
           'y': ('', ''),
           'z': ('', ''),}

    words = []
    words_sa = []

    def __init__(self, path_prog):
        self.path_prog = path_prog

    def set(self, lang, keyboard):
        if lang == lg('francais'):
            lf = 'fr_words.txt'
        elif lang == lg('anglais'):
            lf = 'en_words.txt'
        elif lang == lg('allemand'):
            lf = 'al_words.txt'
        elif lang == lg('italien'):
            lf = 'it_words.txt'
        elif lang == lg('espagnol'):
            lf = 'es_words.txt'
        else:
            return

        z_path = os.path.join(self.path_prog, 'dicos.zip')
        z = ZipFile(z_path, 'r')
        f = z.open(lf, 'r')
        self.words = f.read().decode('utf-8').lower().split('\n')
        f.close()
        z.close()
        self.words_sa = []
        for i in self.words:
            if i:
                self.words_sa.append(self.sa(i))

        if keyboard == 'AZERTY':
            self.kb = self.kbt[0]
        elif keyboard == 'QWERTY':
            self.kb = self.kbt[1]
        else:
            self.kb = self.kbt[2]

    def mots_proches(self, mot):
        def ic(w1, w2):
            corr = 0
            for i in range(len(w1)):
                if w1[i] == w2[i]:
                    corr += 1
            return (corr / len(w1)) * 100
                    
        for w in self.words:
            if w:
                if len(w) == len(mot):
                    if ic(w, mot) > 80.0:
                        return w
        return ''

    def sa(self, mot):
        mot = mot.replace('é', 'e')
        mot = mot.replace('è', 'e')
        mot = mot.replace('ê', 'e')
        mot = mot.replace('ë', 'e')
        mot = mot.replace('à', 'a')
        mot = mot.replace('ô', 'o')
        mot = mot.replace('û', 'u')
        mot = mot.replace('ç', 'c')
        mot = mot.replace('î', 'i')
        mot = mot.replace('ï', 'i')
        mot = mot.replace('ñ', 'n')
        return mot

    def analyse(self, line, e):
        self.line = line
        del line

        for i in range(len(self.line)):
            line, h = self.line[i]
            j = -1
            while j < len(line) - 1:
                if line[j][0] not in self.words_sa or line[j+1][0] not in self.words_sa:
                    if line[j][0] + line[j+1][0] in self.words_sa:
                        e += 1
                        line[j][0] = line[j][0] + line[j+1][0]
                        line.pop(j+1)
                    else:
                        j += 1
                else:
                    j += 1

            self.line[i] = [line, h]

        for i in range(len(self.line)):
            line, h = self.line[i]
            for j in range(len(line)):
                mot = line[j][0]
                s = False
                if mot[-1] == 's':
                    mot = mot[:-1]
                    s = True

                w = self.mots_proches(mot)
                if w:
                    mot += 's' if s else ''
                    w += 's' if s else ''
                    line[j][0] = w
                    e += 1

            self.line[i] = [line, h]

        return self.line, e


class OCR(Thread):
    MARGE_DESSUS = 10
    MARGE_DESSOUS = 20

    def __init__(self, master, widget, lang, keyboard, path_prog):
        self.path_prog = path_prog
        self.outputdir = self.path_prog + '/temp/'
        Thread.__init__(self)
        self.master = master
        self.widget = widget
        self.t = Traitement(path_prog)
        self.t.set(lang, keyboard)

    def run(self):
        if self.imgs == []:
            self.w.stop()
            showerror(lg('error'), lg('no_images'), master = self.master)
            return

        pipeline = keras_ocr.pipeline.Pipeline()
        self.widget.delete('0.0', 'end')
        self.w.step(first = True)
        e = 0
        for img in self.imgs:
            try:
                self.images = [keras_ocr.tools.read(img)]
            except AssertionError as e:
                self.w.stop()
                showerror(lg('importer'), lg('FNF'), master = self.master)
                return

            self.line = [] # = [[[], 0]] # 1. (texte de la ligne, largeur)  2. Hauteur de la ligne
            prediction_groups = pipeline.recognize(self.images)

            for img in prediction_groups:
                for w, d in img:
                    self.add_line(w, d[0])

            for i in range(len(self.line)):
                self.line[i] = self.sort_line(self.line[i])

            mini = [99999.9, 0]
            i = 0
            for l, _ in self.line:
                t, w = l[0]
                if len(l) < 2:
                    continue

                if w < mini[0]:
                    mini = [w, i]
                i += 1
            begin_at = mini[0]

            larg_space = self.line[mini[1]][0][1][1] - self.line[mini[1]][0][0][1]
            larg_space /= len(self.line[mini[1]][0][0][0])
            for i in range(len(self.line)):
                line, h = self.line[i]
                spaces = ' ' * (int((line[0][1] - begin_at) / larg_space) - 1)
                if spaces != '':
                    line.insert(0, [spaces, begin_at])
                    self.line[i] = [line, h]

            self.line, e = self.t.analyse(self.line, e)

            self.text = ''
            for l, _ in self.line:
                for w, _ in l:
                    self.text += w + ' '
                self.text += '\n'

            self.widget.insert('end', self.text)
            self.widget.see('end')
            self.w.step()

        if self.mode == 'pdf':
            for file in self.imgs:
                os.remove(file)

        self.w.stop()
        showinfo(lg('error'), lg('error_part1') + str(e) + lg('error_part2'), master = self.master)

    def begin(self, file):
        self.w = Waiter(master = self.master, double = True, title = lg('analyse'), text = lg('can_take_time'), autostart = False)
        self.w.start()
        if Fichier(file).ext == '.pdf':
            self.mode = 'pdf'
            self.document = PdfReader(open(file, 'rb'))
            self.readImages()
        elif Fichier(file).ext == '.jpg':
            self.mode = 'image'
            self.imgs = [file]
        else:
            return

        self.w.set(len(self.imgs) + 1, with_first = True)
        self.start()

    def get(self):
        return self.text

    def add_line(self, word, coords):
        width, height = coords
        for i in range(len(self.line)):
            text, h = self.line[i]
            if height - self.MARGE_DESSOUS < h < height + self.MARGE_DESSUS:
                self.line[i][0].insert(len(self.line[i][0]) - 1, (word, width))
                return

        self.line.append([[(word, width)], height])

    def sort_line(self, ln):
        text = []
        for word, pos in ln[0]:
            a = False
            for i in range(len(text)):
                if text[i][1] > pos:
                    text.insert(i, [word, pos])
                    a = True
                    break
            if not a:
                text.append([word, pos])
    
        
        return [text, ln[1]]

    def readImages(self):
        self.imgs = []
        for page in range(len(self.document.pages)):
            page_reading = self.document.pages[page]
            if '/XObject' in page_reading['/Resources']:
                xObject = page_reading['/Resources']['/XObject'].get_object()
            
                for obj in xObject:
                    if xObject[obj]['/Subtype'] == '/Image':
                        size = (xObject[obj]['/Width'], xObject[obj]['/Height'])
                        data = xObject[obj].get_data()
    
                        if xObject[obj]['/ColorSpace'] == '/DeviceRGB':
                            mode = "RGB"
                        else:
                            mode = "P"

                        if '/DCTDecode' in xObject[obj]['/Filter']:
                            img = open(self.outputdir + obj[1:] + ".jpg", "wb")
                            img.write(data)
                            img.close()
                            self.imgs.append(self.outputdir + obj[1:] + '.jpg')
                            continue

                        elif '/FlateDecode' in xObject[obj]['/Filter']:
                            img = Image.frombytes(mode, size, data)
                            img.save(self.outputdir + obj[1:] + ".png")
                            self.imgs.append(self.outputdir + obj[1:] + '.png')
                            continue
    
                        elif '/JPXDecode' in xObject[obj]['/Filter']:
                            img = open(self.outputdir + obj[1:] + ".jp2", "wb")
                            img.write(data)
                            img.close()
                            self.imgs.append(self.outputdir + obj[1:] + '.jp2')
                            continue


def get_lg_pos(data, langs):
    try:
        return list(langs.values()).index(data)
    except:
        return 0


class AskParaOCR:
    kbt = ['azerty', 'qwerty', 'bépo']
    lgs = {lg('anglais') : 'an',
           lg('francais') : 'fr',
           lg('allemand') : 'al',
           lg('espagnol') : 'es',
           lg('italien') : 'it',}

    def __init__(self, master, text, file, path_prog):
        for i in range(len(self.kbt)):
            self.kbt[i] = self.kbt[i].upper()

        self.root, self.text, self.file, self.path_prog = master, text, file, path_prog
        self.master = Toplevel(master)
        self.master.transient(master)
        self.master.iconbitmap(PATH_PROG + '/image/icons/pdf.ico')
        self.master.title(lg('importer'))
        self.master.resizable(False, False)
        Label(self.master, text = file, font = ('Consolas', 10, 'italic')).place(x = 10, y = 10)
        Label(self.master, text = lg('langage')).place(x = 10, y = 40)
        Label(self.master, text = lg('clavier')).place(x = 10, y = 70)
        self.lg = ttk.Combobox(self.master, value = list(self.lgs.keys()))
        self.lg.place(x = 100, y = 40)
        self.lg.current(get_lg_pos(sel_lg(), self.lgs))
        self.kb = ttk.Combobox(self.master, value = self.kbt)
        self.kb.place(x = 100, y = 70)
        self.kb.current(0 if sel_lg() in ('fr') else 1 if sel_lf() in ('an', 'ch', 'al') else 2)
        Button(self.master, text = lg('ok'), command = self.lunch).place(x = 10, y = 100)
        Button(self.master, text = lg('cancel'), command = self.master.destroy).place(x = 100, y = 100)
        self.master.geometry('250x140')

    def lunch(self):
        lgs, kbs = self.lg.get(), self.kb.get()
        self.master.destroy()
        o = OCR(self.root, self.text, lgs, kbs, self.path_prog)
        o.begin(self.file)


def lunch_ocr(root, text, file, path_prog):
    a = AskParaOCR(root, text, file, path_prog)


class PDFTraitement:
    def begin_pdf_analyse(self, name):
        PDF = PdfReader(open(name, 'rb'))
        texte = ''
        pb = Progress(self.master,
                      title = lg('import_pdf'),
                      double = True)
        pages = PDF.pages
        pb.set(len(pages), bar = 1)
        for page in pages:
            l = page.extract_text().replace('\n', '')
            pb.reset(0)
            pb.set(len(l), 0)
            for c in list(l):
                pb.step()
                if c[0] == ' ' and len(c) == 2:
                    texte += '\n' + c[1]
                else:
                    texte += c
            pb.step(bar = 1)
        pb.stop()

        self.text.insert(END, texte)
        self.autocolorwords()
        self.update_line_numbers(fforbid = True)
        self.text.focus()
        self.saveas(path = name, forcing = True)


if __name__ == '__main__':
    from tkinter.filedialog import *
    root = Tk()
    root.iconbitmap('./image/icons/file.ico')
    text = Text(root)
    text.pack()
    def beg(file = None):
        if not file:
            file = askopenfilename(filetypes = [('PDF files', '*.pdf'), ('Image Files', '*.jpg')], initialdir = PATH_PROG + '/temp/')

        lunch_ocr(root, text, file)
        
    b = Button(root, command = beg, text = 'Démarrer le test')
    b.pack()
    beg(file = '.\\temp\\Obj97.jpg')
    root.mainloop()
