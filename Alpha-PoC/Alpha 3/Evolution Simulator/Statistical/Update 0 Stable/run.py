from random import randint as ri
import math

fData = []
realData = []

def genDat(fData=None):
    """
    Generate 3 value: survivalRate, survivalPercent, reproductiveRate
    """

    survivalRate = int(ri(0,100))
    survivalPercent = survivalRate / 100
    reproductiveRate = int(ri(0,2))

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

def genDataSet(population=28):

    for _ in range(population):
        genDat(fData)

    divMax(fData, realData)

    return

def printDataSet():

    for indexCounter in range(0,len(realData),4):

        rdPrint = realData[indexCounter]
        setIndex = round(rdPrint, 2)
        print("Child 1", setIndex)

        indexCounter = indexCounter + 1
        rdPrint = realData[indexCounter]
        setIndex = realData[indexCounter]
        setIndex = round(rdPrint, 2)
        print("Child 2", setIndex)

        indexCounter = indexCounter + 1
        rdPrint = realData[indexCounter]
        setIndex = realData[indexCounter]
        setIndex = round(rdPrint, 2)
        print("Child 3", setIndex)

        indexCounter = indexCounter + 1
        rdPrint = realData[indexCounter]
        setIndex = realData[indexCounter]
        setIndex = round(rdPrint, 2)
        print("Child 4", setIndex)

        print("--- End ---")

        #with open("relative fitness.txt", "a") as f:

if __name__ == "__main__":
    genDataSet()
    printDataSet()

    print(len(fData))
    print("run the script as the following to be interactive")
    print("python -i run.py")
