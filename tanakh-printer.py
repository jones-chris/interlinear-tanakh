from fpdf import FPDF
from DbActions import DbActions
from constants import Constants


def print_line_of_words_right_to_left(pdf, font, font_size, cell_w, cell_h, words, reverse_word=False):
    while pdf.get_x() > pdf.l_margin:
        pdf.set_font(font, '', font_size)

        try:
            for j in range(0, 5, 1):
                word = words[j][0][::-1] if reverse_word else words[j][0]
                pdf.cell(cell_w, cell_h, txt=word)
                pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            # Get remainder and write cell with word
            last_cell_w = pdf.get_x() - pdf.l_margin
            word = words[5][0][::-1] if reverse_word else words[5][0]
            pdf.cell(last_cell_w, cell_h, txt=word)
            pdf.set_x(pdf.get_x() - last_cell_w - last_cell_w)
        # If we reach the end of the list before finishing the loop, then just break the loop.
        except (AttributeError, IndexError):
            break


def move_down_one_line(cell_h, x_origin):
    pdf.set_y(pdf.get_y() + cell_h)
    pdf.set_x(x_origin)


pdf = FPDF()
pdf.add_page()

#font = 'SBL_Hbrw'
font = 'times'
pdf.add_font(font, '', '{}.ttf'.format(font), uni=True)

cell_w = 30
cell_h = 10
x_origin = pdf.w - pdf.r_margin - cell_w
pdf.set_x(x_origin)

db_actions = DbActions()


for book in Constants().torah:
    eng_tran_words = db_actions.get_eng_tran_by_book(book)
    heb_text_words = db_actions.get_heb_word_by_book(book)
    strongs_ref_words = db_actions.get_strongs_ref_by_book(book)
    heb_meaning_words = db_actions.get_heb_meaning_by_book(book)

    for i in range(0, len(heb_text_words), 6):
        print_line_of_words_right_to_left(pdf, font, 10, cell_w, cell_h, strongs_ref_words[i:i+6])
        move_down_one_line(cell_h, x_origin)

        print_line_of_words_right_to_left(pdf, font, 20, cell_w, cell_h, heb_text_words[i:i+6], True)
        move_down_one_line(cell_h, x_origin)

        print_line_of_words_right_to_left(pdf, font, 10, cell_w, cell_h, eng_tran_words[i:i+6])
        move_down_one_line(cell_h, x_origin)

pdf.output('./pdfs/tanakh.pdf', 'F')


