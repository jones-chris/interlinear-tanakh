from fpdf import FPDF
from DbActions import DbActions


pdf = FPDF()
pdf.add_page()
font = 'SBL_Hbrw'
# pdf.add_font(font, '', 'C:\Windows\Fonts\{}.ttf'.format(font), uni=True)
pdf.add_font(font, '', '{}.ttf'.format(font), uni=True)
pdf.set_font(font, '', 20)

cell_w = 30
cell_h = 10
x_origin = pdf.w - pdf.r_margin - cell_w
pdf.set_x(x_origin)

db_actions = DbActions()
words = db_actions.get_words_by_book('genesis')

for word in words:
    #chapter = word[1]
    #verse = word[2]
    hebrew_text = word[4][::-1] # Reverse so that word does not print backwards on pdf.
    #romanized_text = word[5]
    #english_translation = word[6]
    #strongs_ref = word[7]

    # Check that there is enough room to print another cell horizontally (x-axis)
    if pdf.l_margin > (pdf.get_x() - cell_w):
        # get remainder and write cell with word
        last_cell_w = pdf.get_x() - pdf.l_margin
        pdf.cell(last_cell_w, cell_h, txt=hebrew_text, border=0)

        # move cursor to next line (y) and back to right side of document (x)
        pdf.set_y(pdf.get_y() + cell_h)
        pdf.set_x(x_origin)
    else:
        pdf.cell(cell_w, cell_h, txt=hebrew_text, border=0)
        pdf.set_x(pdf.get_x() - cell_w - cell_w) # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

pdf.output('tanakh.pdf', 'F')


