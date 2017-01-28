from __future__ import print_function

try:
    import pycorpora
except:
    print("Install pycorpora")
    exit(1)

import random

def sentence():
    verblist = pycorpora.words.verbs["verbs"]
    verbs = []
    for i in verblist:
        verbs.append(i["present"])
    adjs = pycorpora.words.adjs["adjs"]
    nouns = pycorpora.words.nouns["nouns"]
    sentence_parts = [random.choice(verbs).title(), random.choice(adjs), random.
                      choice(nouns)]
    sentence = " ".join(sentence_parts)
    return sentence + "."

if __name__ == "__main__":
    random.seed(input("Seed? "))
    print(sentence())
