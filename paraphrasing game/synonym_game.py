import nltk
from nltk.corpus import wordnet, words
import random
from wordhoard import Synonyms, Definitions
from PyDictionary import PyDictionary
import os

#nltk.download('words')

def generate_random_word():
    #with open('wws.txt') as f:
    with open('wbf/wbf_wws.txt') as f:
        words = f.read().splitlines()
        word = random.choice(words)
    return word

if __name__ == "__main__":
    def random_word():
        return generate_random_word()
    
def get_synonyms(word):
    #synonyms = []

    #for syn in wordnet.synsets(word):
    #      for l in syn.lemmas():
    #           synonyms.append(l.name())
    #return(set(synonyms))

    synonyms = Synonyms(search_string=word)
    synonym_results = synonyms.find_synonyms()
    return synonym_results

#def get_synonyms2(word):
#    synonyms = []
#    for syn in wordnet.synsets(word):
#          for l in syn.lemmas():
#               synonyms.append(l.name())
#    return(set(synonyms))

total_correct = 0
total_wrong = 0

def find_word(not_found,total_correct,total_wrong):
    while not_found:
        word = random_word()
        #results = Synonyms(search_string=word, output_format='json').find_synonyms()
        #list = json.loads(results)[word]["synonyms"]
        try:
            syn_list = get_synonyms(word)
            #list2 = get_synonyms2(word)
            not_found = False
            if len(syn_list) <= 5:
                not_found = True
        except:
            not_found = True
    print("\033[93m===========================")
    print(word)
    print("\033[93m===========================\033[0m")

    wrong_answer = True

    while wrong_answer:
        answer = input("synonym: ")

        print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

        if answer == word:
            print('wrong')
            total_wrong += 1
        elif answer in syn_list:
            print('correct')
            wrong_answer = False
            total_correct += 1
        else:                
            print('wrong')
            total_wrong += 1

        print("\033[92mcorrect:", total_correct)
        print("\033[91mwrong:", total_wrong, "\033[0m")
        try:
            print("\33[34mratio:", round(total_correct/total_wrong,2), "\033[0m")
        except ZeroDivisionError:
            print("\33[34mratio:", round(total_correct/1,2), "\033[0m")

        dic = PyDictionary()
        definition = list(dic.meaning(word).values())[0]

        print("\033[4m" + word + "\033[0m")
        print('• definition:')
        for i in range(len(definition)):
            print(f'    - {definition[i]};')
        print('• synonyms:')

        output = '    - '
        terminal_size = os.get_terminal_size()[0]
        for i in range(len(syn_list)):
            if (((len(output) // terminal_size) + 1) * terminal_size) - len(output) <= 15:
                output += ' ' * ((((len(output) // terminal_size) + 1) * terminal_size) - len(output)) + '      '
            output += f'| {syn_list[i]} '
        print(output)
        
        #print(f'synonyms of {word}: {list2}')

        find_word(True,total_correct,total_wrong)

find_word(True,total_correct,total_wrong)

#shorten word list: use more common words, or find another word list
#finish analyser with synoynm saving feature
#feature to adjust
#if have synonym keep the word

#one is actually used words with synonyms by frequency
# - how it's derived: wbf list > proper words from dictionary 
#one is all words with synonyms
