num = 0
from wordhoard import Synonyms

f2 = open('no synonyms.txt')
f2_list = f2.read().splitlines()
f2.close()

def find_word(word):
    try:
        if Synonyms(search_string=word).find_synonyms() == None:
            return True
        else:
            return False
    except:
        pass

with open('words_alpha_modified.txt') as f:
    words = f.read().splitlines()
    for word in words:
        if word in f2_list:
            continue
        elif find_word(word):
            with open('no synonyms.txt','a') as fi:
                fi.write(word + "\n")
                fi.close()
        else:
            print(word, "has synonyms")

