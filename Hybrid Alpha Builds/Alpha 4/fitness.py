"""
Calculate Relative fitness
https://www.radford.edu/~rsheehy/GraphingDemo/fitness1.html
"""
from random import randint as ri
reproductiveRate = []
survivalRate = []
#SR: survivalRate * reproductiveRate; find max value for differential fitness
SR = []
rf = []
counter = 0
tempCount = 1

def genData(population):
    for i in range(population):
        reproductiveRate.append(ri(0,2))
        survivalRate.append(ri(1,100))

def equivRR():
    for n in reproductiveRate:
        relativeFitness = n/survivalRate
        rf.append(relativeFitness)

def equivSR():
    for n in survivalRate:
        relativeFitness = n/reproductiveRate
        rf.append(relativeFitness)

def notEquiv(population):
    for n in range(population):
        #SR: survivalRate * reproductiveRate; temporary holder/process
        SR.append(survivalRate[n] * reproductiveRate[n])
        relativeFitness = SR[n]/max(SR)
        rf.append(relativeFitness)

def showData():
    for n in range(population):
        print("Cell", n)
        print("Reproductive Rate :", reproductiveRate[n])
        print("Survival Rate :", survivalRate[n])
        print("Relative Fitness :", rf[n])
population = int(input("Population >>> "))
genData(population)
notEquiv(population)
showData()
