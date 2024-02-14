import nltk
from nltk.corpus import wordnet, words
import random

nltk.download('words')

def generate_random_word():
    word_list = words.words()
    return random.choice(word_list)

if __name__ == "__main__":
    def random_word():
        return generate_random_word()
    
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
          for l in syn.lemmas():
               synonyms.append(l.name())
    return(set(synonyms))

total_correct = 0
total_wrong = 0

def find_word(not_found,total_correct,total_wrong):
    while not_found:
        word = random_word()
        #results = Synonyms(search_string=word, output_format='json').find_synonyms()
        #list = json.loads(results)[word]["synonyms"]
        list = get_synonyms(word)
        not_found = False
        if len(list) <= 5:
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
        elif answer in list:
            print('correct')
            wrong_answer = False
            total_correct += 1
        else:                
            print('wrong')
            total_wrong += 1
        
        print("\033[92mcorrect:", total_correct)
        print("\033[91mwrong:", total_wrong, "\033[0m")

        print(f'synonyms of {word}: {list}')
        find_word(True,total_correct,total_wrong)


find_word(True,total_correct,total_wrong)
