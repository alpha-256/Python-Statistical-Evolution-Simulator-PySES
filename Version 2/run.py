import time
import sys
import simpleai
import math
from random import randint as ri
from statsgen import genStats

genStats.genAll()

def closeData():
    strengthData.close()
    mutationData.close()
    lifeData.close()

with open("lifeData.txt", "w+") as lifeData :
    lifeData = str(lifeData)
with open("strengthData.txt", "w+") as strengthData :
    strengthData = str(strengthData)
with open("mutationData.txt", "w+") as mutationData :
    mutationData = str(mutationData)
