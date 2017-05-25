from random import randint as ri
from random import choice as rc

SR = []
RR = []
MR = []
RF = []
pRF = []
population = []
parentDNA = []
dnaLength = 100
aminoAcids = ["A","T","C","G"]
survived = []

def genRawData(SR, RR):

    population.append(int(input("population = ")))
    x = int(population[0])

    for counter in range(0, x):

        #Generate base state data
        SR.append(ri(0, 100))
        RR.append(ri(0, 8))
        MR.append(int(ri(0,10)) / 2)

        #Generate DNA Sequence
        memQue = [rc(aminoAcids) for _ in range(dnaLength)]
        parentDNA.append(''.join(memQue))

def calculateRawData():

    x = int(population[0])

    for counter in range(0, x):
        pRF.append(SR[counter] * RR[counter])

    for counter in range(0, x):
        y = round(pRF[counter] / max(pRF), 1)

        if y >= 0.3 :
            RF.append(round(y,1))
            survived.append("1")

        else :
            #do nothing
            pass

def showData():

    for counter in range(0, len(RF)):

        print("RF:  ", RF[counter])
        print("DNA :", parentDNA[counter])
        print("")

    liveCount = len(survived)
    print(liveCount, "out of", population, "suvived")

def procceed():

    q1 = input("Evolve: yes/no?")
    if q1 == "yes":
        #procceed
        pass

    elif q1 == "yes":
        #procceed
        pass

    else :
        print("Unknown option: assuming 'no'")
        q2 = input("Write data?")

        if q2 == "yes":
            #write data
            pass

        else :
            exit()

def evolve():
    for x in range(0, population):
        mutationRate = int(ri(0,10)) / 2
        probability = mutationRate * dnaLen
        print("Mutation Rate % :: ", probability, "%")
        MR.append(probability)
        memQue = [rc(binary) for _ in range(dnaLen)]
        print(memQue)

        if (random.uniform(0.0, 1.0) < probability) :
            enumerate(memQue)
            item = rc(binary)
            idx = ri(0, 9)
            memQue[idx] = item
        else :
            pass ;
        dna.append(''.join(memQue))
        print(memQue)

def writeData():
    with open("data.txt", a) as f:
        f.write()
genRawData(SR, RR)
calculateRawData()
showData()
