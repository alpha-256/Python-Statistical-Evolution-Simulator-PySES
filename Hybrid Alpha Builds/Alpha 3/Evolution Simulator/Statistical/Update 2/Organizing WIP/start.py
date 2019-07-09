from random import randint as ri
import math

fData = []
realData = []
childData = []
rrData = []
childRR = []

global survivors
survivors = 0

def genDat(fData=None):


    survivalRate = int(ri(0,50))
    survivalPercent = survivalRate / 100
    reproductiveRate = int(ri(0,4))

    rrData.append(reproductiveRate)
    if not isinstance(fData, type(None)):
        fData.append(survivalPercent * reproductiveRate)

    return survivalRate, survivalPercent, reproductiveRate

def divMax(fData, realData):
    """
    Calculate in relative, to the max data
    """

    maxData = max(fData)

    for data in fData:
        cuck = data / maxData
        realData.append(cuck)

    pass

def genDataSet(population=51):

    for _ in range(population):
        genDat(fData)

    divMax(fData, realData)

    return
"""
rrData is bound to genDat
survivors
"""
def printDataSet(childData, rrData, survivors):
    for indexCounter in range(0,len(realData),1):
        rdPrint = realData[indexCounter]
        reproData = rrData[indexCounter]
        setIndex = round(rdPrint, 2)
        rrIndex = round(reproData, 2)
        if setIndex >= 0.3:
            print("Parent", "#", indexCounter, setIndex)
            #survivor counter
            survivors = survivors + 1
            childData.append(setIndex)
            childRR.append(rrIndex)
        else :
            pass
    print(survivors, "Parents Survived")


def writeData():
    with open("relative fitness.txt", "a") as f:
        """
        Save reproduction rate for later generations of entity
        """
        f.write(childRR)

    #Survivor Counter

if __name__ == "__main__":
    genDataSet()
    print("\n")
    printDataSet(childData, rrData, survivors)
    print("\n")
    print(childRR)
    print("\n")
    print(childData)
    print("\n")
    print("run the script as the following to be interactive")
    print("python -i run.py")
