import itertools
import random
from random import choices as rcs

decide = []
answer = []

with open("notes.txt", "r") as data:
    dataHolder = data.read()
    dataHolder = dataHolder.lower()

wordlist = dataHolder.split()
wordfreq = []

for w in wordlist:
    wordfreq.append(wordlist.count(w))

print("String\n" + wordstring +"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Total words\n" + str(len(wordfreq)) + "\n")

def percentCal():
    for index in wordfreq:
        percentDiv = index / len(wordfreq)
        percent = percentDiv * 100
        decide.append(round(percent, 2))
    print(decide)

def probabilityDist():
    for index in range(500):
        answer.append(str(rcs(wordlist, decide)))
percentCal()
probabilityDist()
print(decide)
for index in range(0,len(answer)):
    print(index)
    x0 = str(answer[index])
    x1 = str(answer[index + 1])
    if x0 == x1:
        del answer
