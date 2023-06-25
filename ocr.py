from progress import *
from threading import Thread
from tkinter import *
from confr import *
from pathlib import Path
from PyPDF2 import PdfReader
from PIL import Image
import os
try:
    import keras_ocr
except:
    print('no module keras_ocr !')

PATH_PROG = os.path.abspath(os.getcwd())

class OCR(Thread):
    MARGE_DESSUS = 10
    MARGE_DESSOUS = 20
    outputdir = PATH_PROG + '/temp/'

    def __init__(self, master, widget):
        Thread.__init__(self)
        self.master = master
        self.widget = widget

    def run(self):
        if self.imgs == []:
            return

        pipeline = keras_ocr.pipeline.Pipeline()
        self.widget.delete('0.0', 'end')
        for img in self.imgs:
            self.images = [keras_ocr.tools.read(img)]
            self.line = [[[], 0]] # 1. (texte de la ligne, largeur)  2. Hauteur de la ligne
            prediction_groups = pipeline.recognize(self.images)
            for img in prediction_groups:
                for w, d in img:
                    self.add_line(w, d[0])
    
            self.text = ''
            for l, _ in self.line:
                self.text += self.sort_line(l) + '\n'

            self.widget.insert('end', self.text)
            self.widget.see('end')
            self.w.step()

        for file in self.imgs:
            os.remove(file)

        self.w.stop()

    def begin(self, file):
        self.w = Waiter(master = self.master, double = True, title = lg('analyse'), text = lg('can_take_time'), autostart = False)
        self.w.start()
        self.document = PdfReader(open(file, 'rb'))
        self.readImages()
        self.w.set(len(self.imgs))
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
        for word, pos in ln:
            a = False
            for i in range(len(text)):
                if text[i][1] > pos:
                    text.insert(i, [word, pos])
                    a = True
                    break
            if not a:
                text.append([word, pos])
    
        t = ''
        for w, _ in text:
            t += w + ' '
        return t

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

if __name__ == '__main__':
    from tkinter.filedialog import *
    root = Tk()
    text = Text(root)
    text.pack()
    def beg():
        b.config(stat = 'disabled')
        file = askopenfilename(filetypes = [('PDF files', '*.pdf')], initialdir = PATH_PROG + '/temp/')
        if file:
            o = OCR(root, text)
            o.begin(file)
        
    b = Button(root, command = beg, text = 'Démarrer le test')
    b.pack()
    root.mainloop()
