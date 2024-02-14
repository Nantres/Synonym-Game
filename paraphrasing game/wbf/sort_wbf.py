import nltk
from nltk.corpus import wordnet, words
num = 0
f1 = open('wbf/wbf (common).txt','w')
f2 = open('wbf/wbf (rare).txt','w')
f1.close()
f2.close()

with open('wbf/wbf.txt') as f:
    with open('words_alpha (og).txt') as ff:
        words = f.read().splitlines()
        words2 = ff.read().splitlines()
        for word in words:
            if word in words2:
                with open('wbf/wbf (common).txt','a') as f3:
                    f3.write(word+'\n')
                    num += 1
                    print(num)
                    f3.close()
            else:
                with open('wbf/wbf (rare).txt','a') as f4:
                    f4.write(word+'\n')
                    f4.close()

    f.close()
    ff.close()
    
