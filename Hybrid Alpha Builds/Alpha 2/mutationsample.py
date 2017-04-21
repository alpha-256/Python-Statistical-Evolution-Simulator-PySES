from random import randint as ri
from random import choice as rc
import random

"""Assign Vars"""
binary = ["A", "T", "C", "G"]
memQue           =  []
mutationRate     =  []
population = 5
dnaLen = 8
probability = []
dna = []

"""Artihmetic Vars"""
#Determine Mutation probability
mutationRate = int(ri(0,100)) / 2
probability = mutationRate * dnaLen

#Determine Survival probability
survivalPercent = int(ri(0,50))
reproductiveRate = int(ri(0,4))

for entity in range(population):
    dna.append()
    print("Mutation Rate % :: ", probability, "%")

    """Mutate"""
    memQue = [rc(binary) for _ in range(dnaLen)]
    print(memQue)

    for x in range(0, 9):
        if (random.uniform(0.0, 1.0) < probability):
            enumerate(memQue)
            item = rc(binary)
            idx = ri(0,7)
            memQue[idx] = item
        else:
            print("No mutation")
    print(memQue)
