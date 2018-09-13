from fpdf import FPDF
from DbActions import DbActions


pdf = FPDF()
pdf.add_page()
font = 'SBL_Hbrw'
pdf.add_font(font, '', '{}.ttf'.format(font), uni=True)
pdf.set_font(font, '', 20)

db_actions = DbActions()
words = db_actions.get_words_by_book('genesis')

# TODO:  Y is row number
# TODO:  X is column number
cell_h = 10
x_original = pdf.w - pdf.r_margin
x_current = x_original
y_current = pdf.get_y() #pdf.h - pdf.t_margin
for word in words:
    if word[1] == 1:
        chapter = word[1]
        verse = word[2]
        hebrew_text = word[4][::-1] # Reverse so that word does not print backwards on pdf.
        romanized_text = word[5]
        english_translation = word[6]
        strongs_ref = word[7]

        x_hebrew_word = x_current - (len(hebrew_text) * 2) # Words always print to the right - even when we're starting on the right side.
        y_hebrew_word = y_current
        # Check that there is enough room to print another cell horizontally (x-axis)
        if pdf.l_margin > x_hebrew_word:
            y_current -= cell_h
            x_current = x_original

        pdf.text(x_hebrew_word, y_hebrew_word, hebrew_text)
        x_hebrew_word -= 2
        pdf.text(x_hebrew_word, y_hebrew_word, ' ')
        x_current = x_hebrew_word
    else:
        break

pdf.output('tanakh.pdf', 'F')
