from random import randint as ri
from random import choice as rc
import random

binary = ["A", "T", "C", "G"]
mutationRate     =  []
population = int(input("Population >>>= ")) - 1
dnaLen = 32
probability = []
dna = []
SR = []
RR1 = []
RF = []
RR = []
bindRF = []
preRF = []
liveCount = []
genration = []

def runMutation():
    z = liveCount[0]
    for x in range(0, z):
        mutationRate = int(ri(0,100)) / 50
        probability = mutationRate * dnaLen
        print("Mutation Rate % :: ", probability, "%")

        memQue = [rc(binary) for _ in range(dnaLen)]
        print(''.join(memQue))

        if (random.uniform(0.0, 1.0) < probability):
            enumerate(memQue)
            item = rc(binary)
            idx = ri(0, 9)
            memQue[idx] = item
        else:
            pass;
        dna.append(''.join(memQue))
        print(''.join(memQue))
        print("\n")

def genOne():
    for indexCount in range(0, population) :
        bindRR = (ri(0, 8))
        bindSR = (ri(0, 100) / 100)
        RR1.append(bindRR)
        SR.append(bindSR)
        bindRF.append(round(bindSR * bindRR, 2))
    survived = 0
    for indexCounter in range(0, population) :
        x = round(bindRF[indexCounter]/max(bindRF), 2)
        if x <= 0.3 :
            RF.append(x)
            RR.append(RR1[indexCounter])
            survived = survived + 1
        else :
            pass
    liveCount.append(survived)

genOne()
x = 0
while x < len(RF):
    if x < 10:
        print("ID    ", x, RR[x], "  ", RF[x])
    else :
        print("ID   ", x, RR[x], "  ", RF[x])
    x += 1
print(liveCount[0], "/", population + 1, "survived")
runMutation()
