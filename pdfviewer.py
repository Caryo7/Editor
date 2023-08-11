from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import os
import math
import fitz
from tkinter import PhotoImage

PATH_PROG = os.path.abspath(os.getcwd())

class PDFMiner:
    def __init__(self, filepath):
        self.filepath = filepath
        self.pdf = fitz.open(self.filepath)
        self.first_page = self.pdf.load_page(0)
        self.width, self.height = self.first_page.rect.width, self.first_page.rect.height
        zoomdict = {800:0.8, 700:0.6, 600:1.0, 500:1.0}
        width = int(math.floor(self.width / 100.0) * 100)
        self.zoom = zoomdict[width]

    def get_metadata(self):
        metadata = self.pdf.metadata
        numPages = self.pdf.page_count
        return metadata, numPages
    
    def get_page(self, page_num):
        page = self.pdf.load_page(page_num)
        if self.zoom:
            mat = fitz.Matrix(self.zoom, self.zoom)
            pix = page.get_pixmap(matrix=mat)
        else:
            pix = page.get_pixmap()
        px1 = fitz.Pixmap(pix, 0) if pix.alpha else pix
        imgdata = px1.tobytes("ppm")
        return PhotoImage(data=imgdata)
    
    def get_text(self, page_num):
        page = self.pdf.load_page(page_num)
        text = page.getText('text')
        return text


class PDFViewer:
    def __init__(self, root = None):
        self.path = None
        self.fileisopen = None
        self.author = None
        self.name = None
        self.current_page = 0
        self.numPages = None
        if root:
            self.master = Toplevel(root)
            self.master.transient(root)
        else:
            self.master = Tk()

        self.master.title('PDF Viewer')
        self.master.geometry('580x520+440+180')
        #self.master.resizable(width = 0, height = 0)
        self.master.iconbitmap(self.master, PATH_PROG + '/image/icons/pdf_file_icon.ico')
        self.menu = Menu(self.master)
        self.master.config(menu=self.menu)
        self.filemenu = Menu(self.menu, tearoff = 0)
        self.menu.add_cascade(label="File", menu=self.filemenu)
        self.filemenu.add_command(label="Open File", command=self.open_file)
        self.filemenu.add_command(label="Exit", command=self.master.destroy)
        self.top_frame = ttk.Frame(self.master, width=580, height=460)
        self.top_frame.grid(row=0, column=0)
        self.top_frame.grid_propagate(False)
        self.bottom_frame = ttk.Frame(self.master, width=580, height=50)
        self.bottom_frame.grid(row=1, column=0)
        self.bottom_frame.grid_propagate(False)
        self.scrolly = Scrollbar(self.top_frame, orient=VERTICAL)
        self.scrolly.grid(row=0, column=1, sticky=(N,S))
        self.scrollx = Scrollbar(self.top_frame, orient=HORIZONTAL)
        self.scrollx.grid(row=1, column=0, sticky=(W, E))
        self.output = Canvas(self.top_frame, bg='#ECE8F3', width=560, height=435)
        self.output.configure(yscrollcommand=self.scrolly.set, xscrollcommand=self.scrollx.set)
        self.output.grid(row=0, column=0)
        self.scrolly.configure(command=self.output.yview)
        self.scrollx.configure(command=self.output.xview)
        self.uparrow_icon = PhotoImage(file=PATH_PROG + '/image/48x48/uparrow.png')
        self.downarrow_icon = PhotoImage(file=PATH_PROG + '/image/48x48/downarrow.png')
        self.uparrow = self.uparrow_icon.subsample(3, 3)
        self.downarrow = self.downarrow_icon.subsample(3, 3)
        self.upbutton = ttk.Button(self.bottom_frame, image=self.uparrow, command=self.previous_page)
        self.upbutton.grid(row=0, column=1, padx=(270, 5), pady=8)
        self.downbutton = ttk.Button(self.bottom_frame, image=self.downarrow, command=self.next_page)
        self.downbutton.grid(row=0, column=3, pady=8)
        self.page_label = ttk.Label(self.bottom_frame, text='page')
        self.page_label.grid(row=0, column=4, padx=5)

        if not root:
            self.master.mainloop()

    def open_file(self, filepath = None):
        if not filepath:
            filepath = fd.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(), filetypes=(('PDF', '*.pdf'), ))

        if filepath:
            self.path = filepath
            filename = os.path.basename(self.path)
            self.miner = PDFMiner(self.path)
            data, numPages = self.miner.get_metadata()
            self.current_page = 0
            if numPages:
                self.name = data.get('title', filename[:-4])
                self.author = data.get('author', None)
                self.numPages = numPages
                self.fileisopen = True
                self.display_page()
                self.master.title(self.name)
    
    def display_page(self):
        if 0 <= self.current_page < self.numPages:
            self.img_file = self.miner.get_page(self.current_page)
            self.output.create_image(0, 0, anchor='nw', image=self.img_file)
            self.stringified_current_page = self.current_page + 1
            self.page_label['text'] = str(self.stringified_current_page) + ' of ' + str(self.numPages)
            region = self.output.bbox(ALL)
            self.output.configure(scrollregion=region)         

    def next_page(self):
        if self.fileisopen:
            if self.current_page <= self.numPages - 1:
                self.current_page += 1
                self.display_page()
   
    def previous_page(self):
        if self.fileisopen:
            if self.current_page > 0:
                self.current_page -= 1
                self.display_page()

PDFViewer()
