from fpdf import FPDF
from DbActions import DbActions


pdf = FPDF()
pdf.add_page()
font = 'SBL_Hbrw'
pdf.add_font(font, '', '{}.ttf'.format(font), uni=True)
pdf.set_font(font, '', 20)

cell_w = 30
cell_h = 10
x_origin = pdf.w - pdf.r_margin - cell_w
pdf.set_x(x_origin)

db_actions = DbActions()
eng_tran_words = db_actions.get_eng_tran_by_book('genesis')
heb_text_words = db_actions.get_heb_word_by_book('genesis')
strongs_ref_words = db_actions.get_strongs_ref_by_book('genesis')
heb_meaning_words = db_actions.get_heb_meaning_by_book('genesis')

for i in range(0, len(heb_text_words), 6):

    while pdf.get_x() > pdf.l_margin:
        # Decrease font
        pdf.set_font(font, '', 10)

        try:

            # Write one line of english translation words
            pdf.cell(cell_w, cell_h, txt=strongs_ref_words[i][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=strongs_ref_words[i+1][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=strongs_ref_words[i+2][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=strongs_ref_words[i+3][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=strongs_ref_words[i+4][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            # Get remainder and write cell with word
            last_cell_w = pdf.get_x() - pdf.l_margin
            pdf.cell(last_cell_w, cell_h, txt=strongs_ref_words[i+5][0], border=0)
            pdf.set_x(pdf.get_x() - last_cell_w - last_cell_w) # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

        except (AttributeError, IndexError):
            break

    # Go to down one line and set cursor at right side of page.
    pdf.set_y(pdf.get_y() + cell_h)
    pdf.set_x(x_origin)


    while pdf.get_x() > pdf.l_margin:
        # Increase font
        pdf.set_font(font, '', 20)

        try:

            # Write one line of english translation words
            pdf.cell(cell_w, cell_h, txt=heb_text_words[i][0][::-1])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=heb_text_words[i+1][0][::-1])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=heb_text_words[i+2][0][::-1])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=heb_text_words[i+3][0][::-1])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=heb_text_words[i+4][0][::-1])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            # Get remainder and write cell with word
            last_cell_w = pdf.get_x() - pdf.l_margin
            pdf.cell(last_cell_w, cell_h, txt=heb_text_words[i+5][0][::-1], border=0)
            pdf.set_x(pdf.get_x() - last_cell_w - last_cell_w) # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

        except (AttributeError, IndexError):
            break

    # Go to down one line and set cursor at right side of page.
    pdf.set_y(pdf.get_y() + cell_h)
    pdf.set_x(x_origin)

    while pdf.get_x() > pdf.l_margin:
        # Decrease font
        pdf.set_font(font, '', 10)

        try:

            # Write one line of english translation words
            pdf.cell(cell_w, cell_h, txt=eng_tran_words[i][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=eng_tran_words[i+1][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=eng_tran_words[i+2][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=eng_tran_words[i+3][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            pdf.cell(cell_w, cell_h, txt=eng_tran_words[i+4][0])
            pdf.set_x(pdf.get_x() - cell_w - cell_w)  # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

            # Get remainder and write cell with word
            last_cell_w = pdf.get_x() - pdf.l_margin
            pdf.cell(last_cell_w, cell_h, txt=eng_tran_words[i+5][0], border=0)
            pdf.set_x(pdf.get_x() - last_cell_w - last_cell_w) # Subtract cell_w twice because cell() increases pdf object's x property by w parameter automatically.

        except (AttributeError, IndexError):
            break

    # Go to down one line and set cursor at right side of page.
    pdf.set_y(pdf.get_y() + cell_h)
    pdf.set_x(x_origin)

pdf.output('tanakh.pdf', 'F')


