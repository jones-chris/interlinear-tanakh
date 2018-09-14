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

    def get_words_by_book(self, book):
        conn = None
        try:
            sql = 'select * from tanakh where book = ?;'
            conn = sqlite3.connect('./data/tanakh.db')
            cur = conn.cursor()
            cur.execute(sql, (book,))
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            exit(1)
        finally:
            if conn is not None:
                conn.close()

    def get_strongs_ref_by_book(self, book):
        conn = None
        try:
            sql = 'select strongs_ref from tanakh where book = ?;'
            conn = sqlite3.connect('./data/tanakh.db')
            cur = conn.cursor()
            cur.execute(sql, (book,))
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            exit(1)
        finally:
            if conn is not None:
                conn.close()

    def get_heb_word_by_book(self, book):
        conn = None
        try:
            sql = 'select heb_word from tanakh where book = ?;'
            conn = sqlite3.connect('./data/tanakh.db')
            cur = conn.cursor()
            cur.execute(sql, (book,))
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            exit(1)
        finally:
            if conn is not None:
                conn.close()

    def get_eng_tran_by_book(self, book):
        conn = None
        try:
            sql = 'select eng_tran from tanakh where book = ?;'
            conn = sqlite3.connect('./data/tanakh.db')
            cur = conn.cursor()
            cur.execute(sql, (book,))
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            exit(1)
        finally:
            if conn is not None:
                conn.close()

    def get_heb_meaning_by_book(self, book):
        conn = None
        try:
            sql = 'select heb_meaning from tanakh where book = ?;'
            conn = sqlite3.connect('./data/tanakh.db')
            cur = conn.cursor()
            cur.execute(sql, (book,))
            return cur.fetchall()
        except Exception as ex:
            print(ex)
            exit(1)
        finally:
            if conn is not None:
                conn.close()