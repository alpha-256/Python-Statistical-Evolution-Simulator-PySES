from random import randint as ri
from random import choice as rc
import math

#Memory Que step 1
memQue           =  []
allEntities      =  []
entityFitness    =  []
mutationRate     =  []
reproductiveRate =  []
survivalPercent  =  []

#population
population = 5

#binary DNA select
binary = ["O", "I"]

indexCounter = 0

"""
Check list

*Reproduction Rate
*Mutation Rate
*Survival Rate
*Chance of winning against everything
"""

#Entity Data Generation
def createEntity(memQue, indexCounter, mutationRate, entityFitness, reproductiveRate, survivalPercent):
    memQue.append([rc(binary) for _ in range(8)])
    survivalPercent = int(ri(0,50))
    mutationRate = int(ri(0,100)) / 2
    reproductiveRate = int(ri(0,4))
    if not isinstance(entityFitness, type(None)):
        entityFitness.append(survivalPercent * reproductiveRate)
    print("\n")
    print("Mutation Rate                :: ", mutationRate)
    print("Binary DNA Sequence          :: ", "".join(memQue[-1]))
    print("Fitness                      :: ", entityFitness[indexCounter])
    print("Chances of Mitosis           :: ", reproductiveRate)
    print("Percent of survivalbility    :: ", survivalPercent)
    print("\n")
    indexCounter = indexCounter + 1

for population in range(10) :
    createEntity(memQue, indexCounter, mutationRate, entityFitness, reproductiveRate, survivalPercent)
