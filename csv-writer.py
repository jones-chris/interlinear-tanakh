from DbActions import DbActions

db_actions = DbActions()
#words = db_actions.get_words_by_book('genesis')
strong_refs = db_actions.get_strongs_ref_by_book('genesis')
heb_words = db_actions.get_heb_word_by_book('genesis')
eng_trans = db_actions.get_eng_tran_by_book('genesis')

with open('tanakh.csv', 'w+', encoding='utf-8') as csvfile:
    #writer = csv.writer(csvfile, dialect='excel', delimiter=' ', quotechar='|', encoding='utf-8')
    #for word in words:
        #writer.writerow(word[4].encode('utf-8'))
        #csvfile.write(word[4] + '|' + word[6])
    for i in range(0, len(heb_words), 5):
        if len(heb_words) - i >= 5:
            csvfile.write('{}|{}|{}|{}|{}'.format(strong_refs[i], strong_refs[i+1], strong_refs[i+2], strong_refs[i+3], strong_refs[i+4]))
            csvfile.write('{}|{}|{}|{}|{}'.format(heb_words[i], heb_words[i + 1], heb_words[i + 2], heb_words[i + 3], heb_words[i + 4]))
            csvfile.write('{}|{}|{}|{}|{}'.format(eng_trans[i], eng_trans[i + 1], eng_trans[i + 2], eng_trans[i + 3], eng_trans[i + 4]))
        else:
            for j in range(i, len(heb_words), 1):
                csvfile.write(strong_refs[j] + '|')
            for j in range(i, len(heb_words), 1):
                csvfile.write(heb_words[j] + '|')
            for j in range(i, len(heb_words), 1):
                csvfile.write(eng_trans[j] + '|')

