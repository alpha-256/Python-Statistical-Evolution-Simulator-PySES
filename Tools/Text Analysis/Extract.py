import itertools
import random
from random import choices as rcs

decide = []
answer = []

with open("notes.txt", "r") as data:
    dataHolder = "The Prologue My teenage life revolves around a mental illness which I dont know what it is called. The voices in my head one says to kill everyone who calls me a liar or a madman. The other one was my ex Angelina. Several more joined the party when I fell to depression after Angelina died. She bled to death. I live in a space station in the year 2048 after a worldwide nuclear war broke out between North Korea China and Iraq against the rest of the world. During the war a secret society of scientists and their families moved underground by 16 kilometers below the surface and developed nuclear fusion and a way to travel to space without the use of rockets."
    dataHolder = dataHolder.lower()

wordlist = dataHolder.split()
wordfreq = []

for w in wordlist:
    wordfreq.append(wordlist.count(w))

#print("String\n" + wordstring +"\n")
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
