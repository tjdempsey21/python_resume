from fpdf import FPDF
import os
from datetime import datetime

today = datetime.today()
day = today.strftime('%A')
month = today.strftime('%B')
Date = (day + month + str(today.day)) 

title = 'XXX' 
address = 'XXX'
phone = 'XXX'
email = 'XXX'

class PDF(FPDF):
    def header(self):
        # font
        self.set_font('helvetica', 'B', 11)
        # Calculate width of title and position
        title_w = self.get_string_width(title) + 6
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        # Title
        self.cell(title_w, 10, title, border=0, ln=1, align='C')
        self.cell(0, 10, f'{email}, {phone}, {Date}', align='C')
        # Line break
        self.ln(10)

    # Page footer
    def footer(self):
        # Set position of the footer
        self.set_y(-15)
        # set font
        self.set_font('helvetica', 'I', 8)
        # Set font color grey
        self.set_text_color(169,169,169)
        # Page number
        self.cell(0, 10, f'{address} | Page {self.page_no()}', align='C')

    # Read txt file
    def read_txt_file(self, txt_file_path):
        with open(txt_file_path, 'rb') as fh:
            return fh.read().decode('latin-1')

    # Print content from multiple files on a single page
    def print_resume(self, files):
        path = r"XXX"
        # set font
        self.set_font('times', '', 10)
        
        for idx, file in enumerate(files):
            txt_file_path = os.path.join(path, file)
            txt = self.read_txt_file(txt_file_path)

            # insert text
            self.multi_cell(0, 5, txt)

            # draw a line after each file entry except for the last one
            if idx < len(files) - 1:
                self.ln()
                self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
                self.ln()

# Create a PDF object
pdf = PDF('P', 'mm', 'Letter')

# get total page numbers
pdf.alias_nb_pages()

# Set auto page break
pdf.set_auto_page_break(auto=True, margin=15)

# Add Page
pdf.add_page()

# Specify the files you want to include in the resume
files_to_print = ['education.txt', 'work.txt', 'research.txt', 'skills.txt']

# Print content from all files on a single page with lines in between
pdf.print_resume(files_to_print)

# Add links 
pdf.cell( 0, 5, txt='- Linkedin Profile:https://www.linkedin.com/in/XXX', 
         link="XXX",
         ln=True)
pdf.cell(0, 5, txt = '- github profile: https://github.com/XXX (click here if you want to see how this resume was made with python)',
         link='https://github.com/XXX')

# Add image
pdf.image('resume_photo.png', x=180, y=3, w=25, h=25)

# Add title line
pdf.line(10, 30, 205, 30)

pdf.output('XXX')