from random import randint as ri
from random import choice as rc
import random

"""Assign Vars"""
binary = ["A", "T", "C", "G"]
memQue           =  []
mutationRate     =  []
population = 2
dnaLen = 8
probability = []
dna = []

for x in range(0, population):

    #Determine Mutation probability

    mutationRate = int(ri(0,10)) / 100
    probability = mutationRate * dnaLen
    print("Mutation Rate % :: ", probability, "%")

    #Generate DNA seggment
    memQue = [rc(binary) for _ in range(dnaLen)]
    print(memQue)

    """Start to Mutate"""
    if (random.uniform(0.0, 1.0) < probability):
        enumerate(memQue)
        item = rc(binary)
        idx = ri(1,dnaLen)
        memQue[idx] = item
    else:
        pass;
    dna.append(''.join(memQue))

print(memQue)
print("\n")
print(dna)
