from random import randint
import random

for item in range(4):
    tempChromosome = []
    chromosome = []
    gene = ["A","T","C","G"]
    for i in range(20):
        tempChromosome.append(random.choice(gene))

    chromosome.append("".join(tempChromosome))
    print(chromosome)


    file = open("gene.csv", "a")
    for i in chromosome:
        file.write(i)
    file.write(",")
    file.write("\n")
