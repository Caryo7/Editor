#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from confr import *
from progress import *

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


## Rajouter dimensions personnalisées de page PDF (griser donc les radio buttons orientation)


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
        self.pt = Toplevel(self.am)
        self.pt.transient(self.am)
        self.pt.iconbitmap(self.ico['config'])
        self.pt.title(lg('piedtete'))
        self.pt.resizable(False, False)

        def style_piedtete(type_, self):
            assert type_ in ('pieds', 'tete')
            z = Toplevel(self.pt)
            z.transient()
            z.title(lg('style'))
            z.iconbitmap(self.ico['config'])
            Label(z, text = lg('background')).place(x = 10, y = 10)
            Label(z, text = lg('foreground')).place(x = 10, y = 70)

            c1 = ttk.Combobox(z, value = self.colors_name)
            c1.place(x = 10, y = 40)
            c2 = ttk.Combobox(z, value = self.colors_name)
            c2.place(x = 10, y = 100)

            c1.current(1)
            c2.current(0)

            ch = IntVar()
            Checkbutton(z, text = lg('nb_tt_pages'), onvalue = 1, offvalue = 0, variable = ch, stat = 'disabled').place(x = 10, y = 130)
            def valide(self):
                if type_ == 'tete':
                    self.bg_tete.set(self.colors[c1.get()])
                    self.fg_tete.set(self.colors[c2.get()])
                else:
                    self.bg_pieds.set(self.colors[c1.get()])
                    self.fg_pieds.set(self.colors[c2.get()])
                self.show_tt_pages.set(ch.get())
                z.destroy()

            Button(z, text = lg('ok'), command = lambda : valide(self)).place(x = 10, y = 160)
            z.geometry('200x200')

        r1 = ttk.Radiobutton(self.pt, text = lg('nb_page_haut'), value = 'h', variable = self.nb_pages)
        r1.place(x = 200, y = 10)
        txt_ent = ttk.Entry(self.pt, textvariable = self.text_entete, font = ('courier', 10, 'italic'), width = 41)
        txt_ent.place(x = 20, y = 40)
        b1 = Button(self.pt, text = lg('...'), command = lambda : style_piedtete('tete', self), width = 3)
        b1.place(x = 360, y = 40)
        def active1(self):
            txt_ent.config(stat = 'disabled' if self.entetes.get() == 0 else 'normal')
            b1.config(stat = 'disabled' if self.entetes.get() == 0 else 'normal')

        active1(self)
        c1 = ttk.Checkbutton(self.pt, text = lg('Entete')     , onvalue = 1, offvalue = 0, variable = self.entetes, command = lambda : active1(self))
        c1.place(x = 10, y = 10)

        r1 = ttk.Radiobutton(self.pt, text = lg('no_nb_page'), value = 'a', variable = self.nb_pages).place(x = 200, y = 70)

        r2 = ttk.Radiobutton(self.pt, text = lg('nb_page_bas')  , value = 'b', variable = self.nb_pages)
        r2.place(x = 200, y = 100)
        txt_pied = ttk.Entry(self.pt, textvariable = self.text_pieds, font = ('courier', 10, 'italic'), width = 41)
        txt_pied.place(x = 20, y = 130)
        b2 = Button(self.pt, text = lg('...'), command = lambda : style_piedtete('pieds', self), width = 3)
        b2.place(x = 360, y = 130)
        def active2(self):
            txt_pied.config(stat = 'disabled' if self.pieds.get() == 0 else 'normal')
            b2.config(stat = 'disabled' if self.pieds.get() == 0 else 'normal')

        active2(self)
        c2 = ttk.Checkbutton(self.pt, text = lg('Pieds_de_page'), onvalue = 1, offvalue = 0, variable = self.pieds, command = lambda : active2(self))
        c2.place(x = 10, y = 100)

        def validate(self):
            self.pt.destroy()

        def cancel(self):
            self.entetes.set(0)
            self.text_entete.set('')
            self.pieds.set(1)
            self.text_pieds.set('')
            self.nb_pages.set('b')
            validate(self)

        Button(self.pt, text = lg('OK'), command = lambda : validate(self)).place(x = 50, y = 170)
        Button(self.pt, text = lg('cancel'), command = lambda : cancel(self)).place(x = 200, y = 170)
        self.pt.geometry('400x220')

    def protect_pdf(self):
        self.pp = Toplevel(self.am)
        self.pp.iconbitmap(self.ico['security'])
        self.pp.transient(self.am)
        self.pp.title(lg('security'))
        self.pp.resizable(False, False)
        Label(self.pp, text = lg('password')).place(x = 15, y = 15)
        Label(self.pp, text = lg('confirmation')).place(x = 15, y = 45)
        self.password_pdf = StringVar(master = self.am)
        pwd = ttk.Entry(self.pp, textvariable = self.password_pdf, show = '*')
        pwd.place(x = 150, y = 15)
        self.password_pdf_conf = StringVar(master = self.am)
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
        self.am = Toplevel(self.master)
        # Variables
        self.open_finish = IntVar(master = self.master)
        self.pdf_can_print = IntVar(master = self.master)
        self.pdf_can_modify = IntVar(master = self.master)
        self.pdf_can_copy = IntVar(master = self.master)
        self.pdf_can_annotate = IntVar(master = self.master)
        self.keep_styles = IntVar(master = self.master)
        self.orient_paper = StringVar(master = self.master)
        self.text_entete = StringVar(master = self.master)
        self.text_pieds = StringVar(master = self.master)
        self.nb_pages = StringVar(master = self.master)
        self.entetes = IntVar(master = self.master)
        self.pieds = IntVar(master = self.master)
        self.fg_pieds = StringVar(master = self.master)
        self.bg_pieds = StringVar(master = self.master)
        self.fg_tete = StringVar(master = self.master)
        self.bg_tete = StringVar(master = self.master)
        self.show_tt_pages = IntVar(master = self.master)
        #Valeurs
        self.open_finish.set(1)
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
        self.fg_pieds.set('black')
        self.bg_pieds.set('white')
        self.fg_tete.set('black')
        self.bg_tete.set('white')
        self.show_tt_pages.set(0)
        #Fenêtre
        self.am.iconbitmap(self.ico['config'])
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
        self._title_pdf_s = StringVar(master = self.master)
        self._title_pdf = ttk.Entry(self.am, width = 20, textvariable = self._title_pdf_s, stat = 'normal' if not self.mode_print else 'disabled')
        self._title_pdf.place(x = 100, y = 120)
        Label(self.am, text = lg('subject')).place(x = 100, y = 150)
        self._subject_pdf_s = StringVar(master = self.master)
        self._subject_pdf = ttk.Entry(self.am, width = 20, textvariable = self._subject_pdf_s, stat = 'normal' if not self.mode_print else 'disabled')
        self._subject_pdf.place(x = 100, y = 180)

        kps = ttk.Checkbutton(self.am, text = lg('kpstyles'), variable = self.keep_styles).place(x = 100, y = 280)
        ope = ttk.Checkbutton(self.am, text = lg('open_finish'), variable = self.open_finish).place(x = 200, y = 250)

        r1 = ttk.Radiobutton(self.am, text = lg('paysage'), value = 'P', variable = self.orient_paper).place(x = 150, y = 310)
        r2 = ttk.Radiobutton(self.am, text = lg('portrait'), value = 'p', variable = self.orient_paper).place(x = 15, y = 310)

        Label(self.am, text = lg('int_line')).place(x = 75, y = 340)
        self.inter_lines = ttk.Spinbox(self.am, from_ = 0, to = 50, width = 7 + self.decimals, increment = 10 ** (0 - self.decimals))
        self.inter_lines.place(x = 175, y = 340)
        self.inter_lines.set(int((self.inter_ligne / cm) * (10**self.decimals)) / (10**self.decimals))

        Button(self.am, text = lg('security'), command = self.protect_pdf, stat = 'normal' if not self.mode_print else 'disabled').place(x = 100, y = 370)
        Button(self.am, text = lg('piedtete'), command = self.askpiedtete).place(x = 190, y = 370)
        
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
            else:
                name = self.path_prog + '/temp/temp_pdf.pdf'

            self.mode_print = mode_print
            self.cmd_print = cmd_print
            if name and export_pdf:
                if name[-4:] != '.pdf' and name[-5:] != '.pdff':name += '.pdf'
                self.ask_margins(name)
                self.dialoging = False
            else:
                self.dialoging = False

    def begin_export_pdf(self, name):
        zak = Toplevel(self.master)
        zak.iconbitmap(self.ico['pdf'])
        zak.transient(self.master)
        zak.resizable(False, False)
        zak.title(lg('export_pdf'))
        pb = Progressbar(zak, orient='horizontal', mode='determinate', length = 300)
        pb.place(x = 10, y = 50)
        zak.geometry("320x130")
        zak.update()

        nmax = len(self.get_text())
        def step():
            pb['value'] += (1 / nmax) * 100
            zak.update()

        def reset(maxi):
            global nmax
            nmax = maxi
            pb['value'] = 0
            zak.update()

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
        self.page = 0

        def new_page(self):
            self.page += 1
            if self.entetes.get():
                n = 0
                for i in entete:
                    chars.append((self.margin_left + (n * size_w),
                                  int(height - (self.margin_top / 2)),
                                  i,
                                  self.fg_tete.get(),
                                  self.bg_tete.get()))
                    n += 1

            if self.pieds.get():
                n = 0
                for i in pieds:
                    chars.append((self.margin_left + (n * size_w),
                                  int(self.margin_bottom / 2),
                                  i,
                                  self.fg_pieds.get(),
                                  self.bg_pieds.get()))
                    n += 1

            if self.nb_pages.get() != 'a':
                page_ = str(self.page)
                for n in range(len(page_)):
                    chars.append((width - self.margin_right - (n * size_w),
                                  int(self.margin_bottom / 2) if self.nb_pages.get() == 'b' else int(height - (self.margin_top / 2)),
                                  page_[len(page_) - 1 - n],
                                  'black',
                                  'white'))

        for char in text:
            step()
            if column > maxi_larg:
                line += 1
                column = 0
                len_line.insert(line, 999)

            if line > maxi_high:
                new_page(self)
                chars.append((None, None, 'show', None, None))
                line = 0

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

        new_page(self)
        reset(len(chars))
        for x, y, char, f, b in chars:
            step()
            if char == 'show':
                c.showPage()
                continue
    
            if self.keep_styles.get():
                c.setFillColor(b)
                c.rect(x, y - (size / 4), size_w, size, fill = 1, stroke = 0)
                c.setFillColor(f)

            c.setFont(police, size)
            c.drawString(x, y, char)
    
        c.showPage()
        c.setAuthor(self.title + ' ' + str(self.version))
        c.setTitle(self.title_pdf)
        c.setSubject(self.subject_pdf)
        c.save()

        if self.mode_print:
            self.cmd_print()

        zak.destroy()
        os.popen(name)
        self.dialoging = False

if __name__ == '__main__':
    from __init__ import *
