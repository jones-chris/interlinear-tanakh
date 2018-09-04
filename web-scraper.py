import requests
from bs4 import BeautifulSoup
from DbActions import DbActions


# Start of script
# Constants
BIBLE_HUB_BASE_URL = 'https://biblehub.com/interlinear/study/{}/{}.htm'
TORAH = {
    'genesis' : 2
    # 'exodus' : 40,
    # 'leviticus' : 27,
    # 'numbers' : 21,
    # 'deuteronomy' : 34,
    # 'joshua' : 24,
    # 'judges' : 21
}
TITLE_PROPS_ROMANIZED_WORD = 0
TITLE_PROPS_ENGLISH_TRANSLATION_WITH_STRONGS = 1
TITLE_PROPS_MEANING = 2
db_actions = DbActions()


db_actions.delete_all_records()
for book in TORAH.keys():
    chapter_number = 1
    while chapter_number <= TORAH.get(book):
        url = BIBLE_HUB_BASE_URL.format(book, chapter_number)
        response = requests.get(url)
        response.encoding = 'utf-8'

        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='utf-8')
        spans = soup.find_all('span', {'class': ['hebrew', 'refmain']})

        verse_number = 1
        word_ordinal = 0
        for span in spans:
            # if is refmain class, then update verse number
            if span.attrs['class'][0] == 'refmain':
                verse_number = span.text
            # else get attributes to write to database
            else:
                aEl = span.find('a')

                hebrew_word = span.text
                title_props = None
                romanized_hebrew_word = None
                english_translation = None
                strongs_reference = None
                hebrew_meaning = None
                grammar = None

                # Title attribute has all translation and meaning data
                title_props = aEl.attrs['title'].split(':')

                # Unfortunately, the title attribute is not in a standardized format.  Sometime the second list element
                # (after calling the split method) can be the TITLE_PROPS_ENGLISH_TRANSLATION_WITH_STRONGS and other
                # times it can be TITLE_PROPS_MEANING.  The words that have this incomplete data are usually minor
                # conjunctions, so the script just tries to get the data it can and if an IndexError is thrown, it stops
                # and inserts a record based on the data it has already parsed.
                try:
                    romanized_hebrew_word = title_props[TITLE_PROPS_ROMANIZED_WORD]
                    english_translation = title_props[TITLE_PROPS_ENGLISH_TRANSLATION_WITH_STRONGS].split(' -- ')[0]
                    strongs_reference = title_props[TITLE_PROPS_ENGLISH_TRANSLATION_WITH_STRONGS].split(' -- ')[1]
                    hebrew_meaning = title_props[TITLE_PROPS_MEANING].split(' -- ')[0]
                    grammar = title_props[TITLE_PROPS_MEANING].split(' -- ')[1]
                except IndexError:
                    pass
                finally:
                    db_actions.insert_record(book, chapter_number, verse_number, word_ordinal, hebrew_word, romanized_hebrew_word,
                                  english_translation, strongs_reference, hebrew_meaning, grammar)

                word_ordinal += 1

        chapter_number += 1