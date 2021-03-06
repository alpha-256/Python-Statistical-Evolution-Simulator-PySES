import numpy as np
import matplotlib.pyplot as plt
from random import randint as ri
from random import choice as rc
import random

SR = []
RR = []
MR = []
RF = []
pRF = []
population = []
parentDNA = []
dnaLength = 100
aminoAcids = ["A","U","C","G"]
survived = []
dna = []

def genRawData(SR, RR):

    population.append(int(input("population = ")))
    x = int(population[0])

    for counter in range(0, x):

        #Generate individual survival rate, reproduction rate
        #And mutation rate
        SR.append(ri(0, 100))
        RR.append(ri(0, 8))
        MR.append(int(ri(0,10)) / 2)

        #Generate DNA Sequence
        memQue = [rc(aminoAcids) for _ in range(dnaLength)]
        parentDNA.append(''.join(memQue))

def calculateRawData():

    #Calculate relative fitness
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

def evolve(parentDNA):
    for x in range(len(population)):

        #Calculate probability
        mutationRate = int(ri(0,10))
        probability1 = mutationRate * dnaLength
        probability = probability1 / 100
        print("Mutation Rate % :: ", probability, "%")
        MR.append(probability)

        #Blind picking system
        if (random.uniform(0.0, 1.0) < probability) :
            enumerate(parentDNA)
            item = rc(aminoAcids)
            idx = ri(0, 9)
            parentDNA[idx] = item
        else :
            pass ;

        #Append Data
        for index in parentDNA:
            dna.append(index)
        counter = 0
        for item in dna:
            print(counter)
            print(item)
            counter += 1

genRawData(SR, RR)
calculateRawData()
showData()
evolve(parentDNA)
