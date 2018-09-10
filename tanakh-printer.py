from fpdf import FPDF
from DbActions import DbActions


pdf = FPDF()
pdf.add_page()
font = 'SBL_Hbrw'
# pdf.add_font(font, '', 'C:\Windows\Fonts\{}.ttf'.format(font), uni=True)
pdf.add_font(font, '', '{}.ttf'.format(font), uni=True)
pdf.set_font(font, '', 20)

db_actions = DbActions()
words = db_actions.get_words_by_book('genesis')

cell_w = 40
cell_h = 10
for word in words:
    if word[1] == 1:
        chapter = word[1]
        verse = word[2]
        hebrew_text = word[4][::-1] # Reverse so that word does not print backwards on pdf.
        romanized_text = word[5]
        english_translation = word[6]
        strongs_ref = word[7]

        # Check that there is enough room to print another cell horizontally (x-axis)
        if pdf.w < (pdf.get_x() + cell_w):
            pdf.set_y(pdf.get_y() + cell_h)
            pdf.set_x(10)

        pdf.cell(cell_w, cell_h, txt=hebrew_text, align='r')
    else:
        break

pdf.output('tanakh.pdf', 'F')
# text = 'בְּרֵאשִׁ֖ית'[::-1]
# pdf.cell(40, 10, hebrew_text)
# pdf.output('tanakh.pdf', 'F')