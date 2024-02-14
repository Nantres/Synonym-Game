import nltk
from nltk.corpus import wordnet, words
num = 0
f1 = open('wbf/wbf_wws.txt','w')
f1.close()

nltk.download('words')
    
def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
          for l in syn.lemmas():
               synonyms.append(l.name())
    return(set(synonyms))

with open('wbf/wbf.txt') as f:
    words = f.read().splitlines()
    for word in words:
        if len(get_synonyms(word)) > 1:
            with open('wbf/wbf_wws.txt','a') as f2:
                f2.write(word+'\n')
                num += 1
                print(num)
                f2.close()
    f.close()
    
