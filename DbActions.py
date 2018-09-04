import sqlite3

class DbActions:

    def insert_record(self, book, chapter_number, verse_number, word_ordinal, hebrew_word, romanized_hebrew_word,
                      english_translation=None, strongs_reference=None, hebrew_meaning=None, grammar=None):
        conn = None
        try:
            conn = sqlite3.connect('tanakh.db')
            COMPLEX_SQL_INSERT_TEMPLATE = "INSERT INTO tanakh values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            conn.execute(COMPLEX_SQL_INSERT_TEMPLATE, (book, chapter_number, verse_number, word_ordinal,
                                                       hebrew_word, romanized_hebrew_word,
                                                       english_translation, strongs_reference, hebrew_meaning, grammar))
            conn.commit()
        except Exception as ex:
            if conn is not None:
                conn.rollback()
            print(repr(ex))
            exit(1)
        finally:
            conn.close()

    def delete_all_records(self):
        conn = None
        try:
            conn = sqlite3.connect('tanakh.db')
            conn.execute('delete from tanakh;')
            conn.commit()
        except Exception as ex:
            if conn is not None:
                conn.rollback()
            print(ex)
            exit(1)
        finally:
            if conn is not None:
                conn.close()