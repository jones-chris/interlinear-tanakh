from fpdf import FPDF
from DbActions import DbActions
from constants import Constants


def print_line_of_words_right_to_left(pdf, font, font_size, cell_w, cell_h, words, reverse_word=False):
    while pdf.get_x() > pdf.l_margin:
        # Uncomment these lines to set a breakpoint when words collection's length is less than the usual 6 items.
        # if len(words) < 6:
        #     print(words)
        pdf.set_font(font, '', font_size)

        #TODO test if we get an attribute error when printing a Pei.  All the strongs_refs and eng_tran are blank for a line after a Pei.
        try:
            # Loop through all words in words collection except for last word.
            for j in range(0, len(words)-1, 1):
                # If the word is None, then print empty text and continue.  This is mostly to catch the Pei of Sameck.
                if words[j] is None:
                    pdf.cell(cell_w, cell_h, txt='')
                    pdf.set_x(pdf.get_x() - cell_w - cell_w)
                    continue

                word = words[j][::-1] if reverse_word else words[j]
                pdf.cell(cell_w, cell_h, txt=word)
                pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            # For last word in words, get remainder and write cell with word
            last_cell_w = pdf.get_x() - pdf.l_margin
            last_index = len(words)-1
            word = words[last_index][::-1] if reverse_word else words[last_index]
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

font = 'times'
pdf.add_font(font, '', './{}.ttf'.format(font), uni=True)

cell_w = 30
cell_h = 10
x_origin = pdf.w - pdf.r_margin - cell_w
pdf.set_x(x_origin)

db_actions = DbActions()


for book in Constants().torah:
    words = db_actions.get_words_by_book(book)

    #TODO:  add page with book title here.

    #TODO:  chapter, and verse printing logic.
    for i in range(0, len(words), 6):
        words_list = words[i:i + 6]
        strongs_ref_words = []
        for j in range(0, len(words_list)):
            strongs_ref_words.append(words_list[j][4])
        print_line_of_words_right_to_left(pdf, font, 10, cell_w, 12, strongs_ref_words)
        move_down_one_line(cell_h, x_origin)

        heb_text_words = []
        for j in range(0, len(words_list)):
            heb_text_words.append(words_list[j][3])
        print_line_of_words_right_to_left(pdf, font, 20, cell_w, 6, heb_text_words, True)
        move_down_one_line(cell_h, x_origin)

        #print_line_of_words_right_to_left(pdf, font, 10, cell_w, 1, eng_tran_words[i:i+6])
        print_line_of_words_right_to_left(pdf, font, 10, cell_w, 1, ['', '', '', '', '', ''])
        move_down_one_line(cell_h, x_origin)

pdf.output('./pdfs/tanakh.pdf', 'F')


