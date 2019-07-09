"""
Calculate Relative fitness
https://www.radford.edu/~rsheehy/GraphingDemo/fitness1.html
"""
from random import randint as ri
RR = []
SR = []
#SR: survivalRate * reproductiveRate; find max value for differential fitness
SxR = []
RF = []
counter = 0
tempCount = 1

def genData(population):
    for i in range(population):
        RR.append(ri(0,2))
        SR.append(ri(1,100))
"""
REDUNDANT FOR NOW!

def equivRR():
    for n in reproductiveRate:
        relativeFitness = n/survivalRate
        RF.append(relativeFitness)

def equivSR():
    for n in survivalRate:
        relativeFitness = n/reproductiveRate
        RF.append(relativeFitness)
"""

def notEquiv(population):
    for n in range(population):
        #SR: survivalRate * reproductiveRate; temporary holder/process
        SxR.append(SR[n] * RR[n])
        if SxR[n] == 0:
            relativeFitness = 0
        else:
            relativeFitness = SxR[n]/max(SR)
        RF.append(relativeFitness)

def showData():
    for n in range(population):
        print("Cell", n)
        print("Reproductive Rate :", RR[n])
        print("Survival Rate :", SR[n])
        print("Relative Fitness Decmial :", RF[n])
        print("Relative Fitness Percent :", round(RF[n] * 100, 5))
        print("################################################")

def showDebug():
    print("DEBUG")
    print(RR)
    print(SR)
    print(RF)
    print("################################################")

population = int(input("Population >>> "))
genData(population)
notEquiv(population)
showData()
showDebug()
