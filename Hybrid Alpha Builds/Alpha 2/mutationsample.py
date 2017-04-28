import math

from random import randint as ri
from random import choice as rc
import random

binary = ["A", "T", "C", "G"]
memQue           =  []
mutationRate     =  []
population = 50
dnaLen = 10
probability = []
dna = []
SR = []
RR = []
RF = []
preRF = []
surviived = []
global survived

def defStats():
    SR.append(ri(0, 100) / 100)
    RR.append(ri(0, 8))
    srSet = float(SR[indexCount])
    rrSet = float(RR[indexCount])
    rfRound = srSet * rrSet
    preRF.append(round(rfRound, 2))

def genOne():
    maxData = max(preRF)
    for indexCounter in preRF:
        x = preRF[indexCounter] / maxData
        if x >= 3.0 :
            RF.append(y)
        else:
            pass;

def showData():
    print(RR)
    print(SR)
    print(preRF)

def runMutation():
    for x in range(0, population):
        mutationRate = int(ri(0,10)) / 2
        probability = mutationRate * dnaLen
        print("Mutation Rate % :: ", probability, "%")

        memQue = [rc(binary) for _ in range(dnaLen)]
        print(memQue)

        if (random.uniform(0.0, 1.0) < probability):
            enumerate(memQue)
            item = rc(binary)
            idx = ri(0, 9)
            memQue[idx] = item
        else:
            pass;
        dna.append(''.join(memQue))
        print(memQue)
        print("\n")


runMutation()
print("\n")
print(dna)
for indexCount in range(0, population):
    defStats()
showData()
