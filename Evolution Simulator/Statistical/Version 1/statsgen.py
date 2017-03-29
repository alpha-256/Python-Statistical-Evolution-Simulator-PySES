import sys
import simpleai
import math
from random import randint as ri

#var Declare
global population
population = int(input("Population? >>> "))

#All Data
genLife = []
genStrength = []
genMutation = []
survivability = []

def genData(genLife, genStrength, genMutation):
    #Generate random popuulation data
    x = 0
    while x < population:
        genLife.append(ri(1, 100))
        genStrength.append(ri(1, 20))
        genMutation.append(ri(1, 5))
        x = x + 1

def printData(genLife, genStrength, genMutation, survivability):
    counter = 0
    while counter < population:
        print(genLife[counter], "  ||  ", genStrength[counter], "    ||  ", genMutation[counter])
        survivability.append( genLife[counter] + genStrength[counter])
        print(survivability[counter])
        counter = counter + 1


def saveData(genLife, genStrength, genMutation):

    #Translate to str format
    genLife = str(genLife)
    genStrength = str(genStrength)
    genMutation = str(genMutation)

    #open data.txt for input
    with open("lifeData.txt", "w+") as lifeData :
        lifeData.write(genLife)
        lifeData.close()
    with open("strengthData.txt", "w+") as strengthData :
        strengthData.write(genStrength)
        strengthData.close()
    with open("mutationData.txt", "w+") as mutationData :
        mutationData.write(genMutation)
        mutationData.close()

genData(genLife, genStrength, genMutation)
printData(genLife, genStrength, genMutation, survivability)