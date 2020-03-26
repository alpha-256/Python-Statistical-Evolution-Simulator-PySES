"""
Punnett Square = 25%
Each population is sorted into 1/4th
DNA is required.
"""

#randomInteger is for mutation stuff DO NOT TOUCH!
from random import randint as randomInteger
from random import choice as randomChoice
import os


def yield_free_specimen_file_name():
    counter = 0
    while True:
        ffmt = "specimen{number}.txt".format(number=counter)
        if os.path.exists(ffmt):
            counter += 1
            continue
        yield ffmt

class dnastuff:

    @staticmethod
    def generate():
        dnaAssembler = []
        finalDNA = []
        dnaLength = 1354
        aminoAcids = ["A","T","C","G"]
        for i in range(dnaLength):
            dnaAssembler.append(randomChoice(aminoAcids))

        print(dnaAssembler)
        finalDNA.append(''.join(dnaAssembler))
        print(finalDNA)

        gen = yield_free_specimen_file_name()
        a = next(gen)
        with open(a, "w") as f:
            f.write(finalDNA[0])
            
if __name__ == "__main__":
    dnastuff().generate()
