from __future__ import print_function

import pycorpora
import random

VERSION = "1/170128"

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
    import argparse
    parser = argparse.ArgumentParser(description="Generate a random strange"
                                                 "sentence.")
    parser.add_argument("--version", help="display this program's version",
                        action="store_true")
    parser.add_argument("--seed", help="seed the random number generator")
    args = parser.parse_args()
    if args.version:
        print("Generate a random strange sentence.")
        print("version " + VERSION)
        exit(0)
    if args.seed:
        random.seed(args.seed)
    print(sentence())
