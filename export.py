#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from confr import *

try: # reportlab
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.lib.units import cm, inch
    from reportlab.lib import pdfencrypt
    export_pdf = True

except ImportError:
    from errors import *
    ERROR(4)
    export_pdf = False
    
try:
    import docx # python-docx
    export_word = True

except ImportError:
    from errors import *
    ERROR(5)
    export_word = False

class AskMargins:
    margin_left = 2 * cm
    margin_right = 2 * cm
    margin_top = 2 * cm
    margin_bottom = 2 * cm
    inter_ligne = 0 * cm
    decimals = 1
    title_pdf = ''
    subject_pdf = ''
    pdf_strength = 40
    pdf_password = None

    def askpiedtete(self):
        self.pt = Toplevel()
        self.pt.transient(self.am)
        self.pt.title(lg('piedtete'))
        self.pt.resizable(False, False)
        c1 = ttk.Checkbutton(self.pt, text = 'Entêtes'      , onvalue = 1, offvalue = 0, variable = self.entetes).place(x = 10, y = 10) ###############################################
        r1 = ttk.Radiobutton(self.pt, text = 'Numéros de page', value = 'h', variable = self.nb_pages).place(x = 200, y = 10)###################################################
        txt_ent = ttk.Entry(self.pt, textvariable = self.text_entete, font = ('courier', 10, 'italic'), width = 45).place(x = 20, y = 40)

        c2 = ttk.Checkbutton(self.pt, text = 'Pieds de page', onvalue = 1, offvalue = 0, variable = self.pieds).place(x = 10, y = 80) #####
        r1 = ttk.Radiobutton(self.pt, text = 'Numéros de page', value = 'b', variable = self.nb_pages).place(x = 200, y = 80)###################################################
        txt_pied = ttk.Entry(self.pt, textvariable = self.text_pieds, font = ('courier', 10, 'italic'), width = 45).place(x = 20, y = 110)

        def validate(self):
            self.pt.destroy()

        def cancel(self):
            self.entetes.set(0)
            self.text_entete.set('')
            self.pieds.set(1)
            self.text_pieds.set('')
            self.nb_pages.set('b')
            validate(self)

        Button(self.pt, text = lg('OK'), command = lambda : validate(self)).place(x = 50, y = 150)
        Button(self.pt, text = lg('cancel'), command = lambda : cancel(self)).place(x = 200, y = 150)
        self.pt.geometry('400x200')

    def protect_pdf(self):
        self.pp = Toplevel()
        self.pp.transient(self.am)
        self.pp.title(lg('security'))
        self.pp.resizable(False, False)
        Label(self.pp, text = lg('password')).place(x = 15, y = 15)
        Label(self.pp, text = lg('confirmation')).place(x = 15, y = 45)
        self.password_pdf = StringVar()
        pwd = ttk.Entry(self.pp, textvariable = self.password_pdf, show = '*')
        pwd.place(x = 150, y = 15)
        self.password_pdf_conf = StringVar()
        pwdc = ttk.Entry(self.pp, textvariable = self.password_pdf_conf, show = '*')
        pwdc.place(x = 150, y = 45)
        pr = ttk.Checkbutton(self.pp, variable = self.pdf_can_print, text = lg('cprint'), onvalue = 1, offvalue = 0).place(x = 15, y = 80)
        mo = ttk.Checkbutton(self.pp, variable = self.pdf_can_modify, text = lg('cmodify'), onvalue = 1, offvalue = 0).place(x = 15, y = 110)
        co = ttk.Checkbutton(self.pp, variable = self.pdf_can_copy, text = lg('ccopy'), onvalue = 1, offvalue = 0).place(x = 15, y = 140)
        an = ttk.Checkbutton(self.pp, variable = self.pdf_can_annotate, text = lg('cannotate'), onvalue = 1, offvalue = 0).place(x = 15, y = 170)

        def validate(self):
            if self.password_pdf.get() == self.password_pdf_conf.get():
                self.pdf_password = self.password_pdf.get()
                self.pp.destroy()
                self.password_for_pdf = True if self.pdf_password != '' else False
            else:
                showerror(lg('security'), lg('nmwp'))

        Button(self.pp, command = lambda : validate(self), text = 'OK').place(x = 15, y = 200)
        self.pp.geometry('300x240')

    def ask_margins(self, name):
        self.nom_pdf = name
        self.am = Toplevel()
        self.am.transient(self.master)
        self.am.title(lg('Marges'))
        Label(self.am, text=lg('haut')).place(x = 100, y = 25)
        Label(self.am, text=lg('bas')).place(x = 100, y = 220)
        Label(self.am, text=lg('gauche')).place(x = 10, y = 100)
        Label(self.am, text=lg('right')).place(x = 250, y = 100)
        self.marg_top = ttk.Spinbox(self.am, from_ = 0, to = 50, width = 7 + self.decimals, increment = 10 ** (0 - self.decimals))
        self.marg_top.place(x = 100, y = 55)
        self.marg_top.set(int((self.margin_top / cm) * (10**self.decimals)) / (10**self.decimals))
        self.marg_bot = ttk.Spinbox(self.am, from_ = 0, to = 50, width = 7 + self.decimals, increment = 10 ** (0 - self.decimals))
        self.marg_bot.place(x = 100, y = 250)
        self.marg_bot.set(int((self.margin_bottom / cm) * (10**self.decimals)) / (10**self.decimals))
        self.marg_lef = ttk.Spinbox(self.am, from_ = 0, to = 50, width = 7 + self.decimals, increment = 10 ** (0 - self.decimals))
        self.marg_lef.place(x = 10, y = 130)
        self.marg_lef.set(int((self.margin_left / cm) * (10**self.decimals)) / (10**self.decimals))
        self.marg_rig = ttk.Spinbox(self.am, from_ = 0, to = 50, width = 7 + self.decimals, increment = 10 ** (0 - self.decimals))
        self.marg_rig.place(x = 250, y = 130)
        self.marg_rig.set(int((self.margin_right / cm) * (10**self.decimals)) / (10**self.decimals))
        Label(self.am, text = lg('title')).place(x = 100, y = 90)
        self._title_pdf_s = StringVar()
        self._title_pdf = ttk.Entry(self.am, width = 20, textvariable = self._title_pdf_s, stat = 'normal' if not self.mode_print else 'disabled')
        self._title_pdf.place(x = 100, y = 120)
        Label(self.am, text = lg('subject')).place(x = 100, y = 150)
        self._subject_pdf_s = StringVar()
        self._subject_pdf = ttk.Entry(self.am, width = 20, textvariable = self._subject_pdf_s, stat = 'normal' if not self.mode_print else 'disabled')
        self._subject_pdf.place(x = 100, y = 180)
        kps = ttk.Checkbutton(self.am, text = lg('kpstyles'), variable = self.keep_styles).place(x = 100, y = 280)

        r1 = ttk.Radiobutton(self.am, text = lg('paysage'), value = 'P', variable = self.orient_paper).place(x = 150, y = 310)
        r2 = ttk.Radiobutton(self.am, text = lg('portrait'), value = 'p', variable = self.orient_paper).place(x = 15, y = 310)

        Label(self.am, text = lg('int_line')).place(x = 75, y = 340)
        self.inter_lines = ttk.Spinbox(self.am, from_ = 0, to = 50, width = 7 + self.decimals, increment = 10 ** (0 - self.decimals))
        self.inter_lines.place(x = 175, y = 340)
        self.inter_lines.set(int((self.inter_ligne / cm) * (10**self.decimals)) / (10**self.decimals))

        Button(self.am, text = lg('security'), command = self.protect_pdf, stat = 'normal' if not self.mode_print else 'disabled').place(x = 100, y = 370)
        Button(self.am, text = lg('piedtete'), command = self.askpiedtete).place(x = 190, y = 370)####################################################################################
        
        Button(self.am, text = lg('OK'), command = self.lunch_export_pdf).place(x = 10, y = 370)
        self.am.geometry('350x410')
        self.am.resizable(False, False)

        def fermer(self):
            self.am.destroy()
            del self.am
            self.dialoging = False

        self.am.protocol('WM_DELETE_WINDOW', lambda : fermer(self))

    def lunch_export_pdf(self):
        self.margin_left = float(self.marg_lef.get()) * cm
        self.margin_right = float(self.marg_rig.get()) * cm
        self.margin_top = float(self.marg_top.get()) * cm
        self.margin_bottom = float(self.marg_bot.get()) * cm
        self.inter_ligne = float(self.inter_lines.get()) * cm
        self.title_pdf = self._title_pdf_s.get()
        self.subject_pdf = self._subject_pdf_s.get()
        self.am.destroy()
        del self.am
        self.begin_export_pdf(self.nom_pdf)


class Export(AskMargins):
    def export_word(self):
        if not(self.dialoging):
            self.dialoging = True
            name = asksaveasfilename(title=lg('Export_Word'), filetypes=[(lg('WF'), '*.docx *.doc')])
            self.dialoging = False
            if name and export_word:
                if name[-5:] != '.docx' and name[-4:] != '.doc':name += '.docx'
                doc = docx.Document()
                for para in self.get_text().split('\n'):
                    doc.add_paragraph(para)

                doc.save(name)

    def export_pdf(self, mode_print = False, cmd_print = None):
        if not self.dialoging or mode_print:
            self.dialoging = True
            if not mode_print:
                name = asksaveasfilename(title=lg('Export_PDF'), filetypes=[(lg('pdff'), '*.pdf *.pdff')])
                self.dialoging = False
            else:
                name = self.path_prog + '/temp/temp_pdf.pdf'

            self.mode_print = mode_print
            self.cmd_print = cmd_print
            if name and export_pdf:
                if name[-4:] != '.pdf' and name[-5:] != '.pdff':name += '.pdf'
                self.pdf_can_print = IntVar()
                self.pdf_can_modify = IntVar()
                self.pdf_can_copy = IntVar()
                self.pdf_can_annotate = IntVar()
                self.keep_styles = IntVar()
                self.orient_paper = StringVar()
                self.text_entete = StringVar()
                self.text_pieds = StringVar()
                self.nb_pages = StringVar()
                self.entetes = IntVar()
                self.pieds = IntVar()

                self.pdf_can_print.set(1)
                self.pdf_can_modify.set(1)
                self.pdf_can_copy.set(1)
                self.pdf_can_annotate.set(1)
                self.keep_styles.set(1)
                self.orient_paper.set('p')
                self.password_for_pdf = False
                self.nb_pages.set('b')
                self.pieds.set(1)
                self.entetes.set(0)
                self.ask_margins(name)

    def begin_export_pdf(self, name):
        enc = pdfencrypt.StandardEncryption(userPassword = self.pdf_password,
                                            ownerPassword = self.pdf_password,
                                            canPrint = self.pdf_can_print.get(),
                                            canModify = self.pdf_can_modify.get(),
                                            canCopy = self.pdf_can_copy.get(),
                                            canAnnotate = self.pdf_can_annotate.get(),)
                                            #strength = self.pdf_strength)

        if self.orient_paper.get() == 'P':
            height, width = A4
        else:
            width, height = A4

        if self.password_for_pdf and not self.mode_print:
            c = canvas.Canvas(name, pagesize = (width, height), encrypt = enc)
        else:
            c = canvas.Canvas(name, pagesize = (width, height))
    
        police = get_font()
        size = int(get_font_size())
        size_w = int(get_font_size()) - 3
        wrap = 'char'
        interligne = self.inter_ligne

        entete = self.text_entete.get()
        pieds = self.text_pieds.get()
        pospage = self.nb_pages.get()
    
        fc = 'black'
        bc = 'white'
    
        c.translate(0, 0)
        c.setFont(police, size)
        chars = []

        maxi_larg = (width - self.margin_right - self.margin_left) / size_w
        maxi_high = (height - self.margin_top - self.margin_bottom) / size

        line = 0
        column = 0
        text = self.get_text()
        len_line = [len(ln) for ln in text.split('\n')]
        list_styles = self.lst_tags.copy()
        list_styles.insert(0, ('normal', bc, fc, '0.0', '0.0'))
        line_text = 0
        column_text = 0
        for char in text:
            if column > maxi_larg:
                line += 1
                column = 0
                len_line.insert(line, 999)

            if line > maxi_high:
                if self.pieds.get():
                    n = 0
                    for i in pieds:
                        chars.append((self.margin_left + (n * size_w),
                                      height - ((size + interligne) * line) - self.margin_top,
                                      i,
                                      'white',
                                      'back'))
                        n += 1
                chars.append('show')
                line = 0
                if self.entetes.get():
                    n = 0
                    for i in entete:
                        chars.append((self.margin_left + (n * size_w),
                                      height - ((size + interligne) * line) - self.margin_top,
                                      i,
                                      'white',
                                      'black'))
                        n += 1

            if char == '\n':
                line += 1
                line_text += 1
                column = 0
                column_text = 0
                continue

            elif char in ('\t', '\r'):
                continue

            for tag in list_styles:
                if tag != ['']:
                    _, bg, fg, begin, end = tag
                    begin_y, begin_x = begin.split('.')
                    end_y, end_x = end.split('.')
                    begin_x, begin_y, end_x, end_y = int(begin_x), int(begin_y) - 1, int(end_x), int(end_y) - 1
                    if begin_y < line_text < end_y:
                        fc = fg
                        bc = bg
                        break

                    elif begin_y == end_y and begin_y <= line_text <= end_y and begin_x <= column_text < end_x:
                        fc = fg
                        bc = bg
                        break

                    elif begin_y <= line_text < end_y and begin_x <= column_text:
                        fc = fg
                        bc = bg
                        break

                    elif begin_y <= line_text <= end_y and begin_x <= column_text < end_x:
                        fc = fg
                        bc = bg
                        break

                    else:
                        bc = list_styles[0][1]
                        fc = list_styles[0][2]

            chars.append((self.margin_left + (column * size_w),
                          height - ((size + interligne) * line) - self.margin_top,
                          char,
                          fc,
                          bc))

            column += 1
            column_text += 1

        for x, y, char, f, b in chars:
            if char == 'show':
                c.showPage()
                continue

            if self.keep_styles.get():
                c.setFillColor(b)
                c.rect(x, y - (size / 4), size_w, size, fill = 1, stroke = 0)
                c.setFillColor(f)

            c.drawString(x, y, char)
    
        c.showPage()
        c.setAuthor(self.title + ' ' + str(self.version))
        c.setTitle(self.title_pdf)
        c.setSubject(self.subject_pdf)
        c.save()

        if self.mode_print:
            self.cmd_print()

        self.dialoging = False

if __name__ == '__main__':
    from __init__ import *
