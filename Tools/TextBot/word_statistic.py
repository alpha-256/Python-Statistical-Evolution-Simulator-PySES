import itertools
import re
import random as m_random

def weighted_choice(choices):
    # code from
    # https://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    total = sum(w for c, w in choices.items())
    r = m_random.uniform(0, total)
    upto = 0
    for c, w in choices.items():
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

def pop_weight_choice(choices):
    # choose
    option = weighted_choice(choices)
    # remove
    choices.pop(option)

    return option

filename = input("Drag and drop file here: ")
filename = re.sub("['\"]", "", filename)

dataHolder = None # Simply a place holder
with open(filename, "r") as tmpf:
    dataHolder = tmpf.read()
dataHolder = dataHolder.lower()

wordlist = dataHolder.split()

# count words frequency
wordFreqDict = dict()
for w in wordlist:
    wordFreqDict[w] = wordFreqDict.get(w, 0) + 1

# Relative appearance
wordFreqDict_relativeAppearance = dict()
maxFreq = max(wordFreqDict.values())
for k, v in wordFreqDict.items():
    wordFreqDict_relativeAppearance[k] = v / maxFreq

# Over all appearance
wordFreqDict_overallApperance = dict()
overallFreq = len(wordFreqDict)
for k, v in wordFreqDict.items():
    wordFreqDict_overallApperance[k] = v / overallFreq

print("- Raw String (Lowered) -")
print(dataHolder)
print("-- statistic --")
print("> Word count:", len(wordFreqDict))
print("> Word frequency:")
for k, v in wordFreqDict.items():
    print(k, ":", v)
print("> Relative appearance:")
for k, v in wordFreqDict_relativeAppearance.items():
    print(k, ":", v)
print("> Overall appearance:")
for k, v in wordFreqDict_overallApperance.items():
    print(k, ":", v)

answer = []
while len(wordFreqDict) > 0:
    answer.append(pop_weight_choice(wordFreqDict))

print(" ".join(answer))

if __name__ == '__main__':
    pass
