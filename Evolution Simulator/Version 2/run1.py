from random import randint as ri
import math

fData = []
realData = []

def genDat(fData=None):
    """
    Generate 3 value: survivalRate, survivalPercent, reproductiveRate
    """

    survivalRate = int(ri(0,50))
    survivalPercent = survivalRate / 100
    reproductiveRate = int(ri(0,4))

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

def genDataSet(numberOfSets=500):

    for _ in range(numberOfSets):
        genDat(fData)

    divMax(fData, realData)

    return

def printDataSet():

    for rollingstone in range(0,len(realData),4):

        damn = realData[rollingstone]
        motherfucker = round(damn, 2)
        print("DD", motherfucker)

        rollingstone = rollingstone + 1
        damn = realData[rollingstone]
        motherfucker = realData[rollingstone]
        motherfucker = round(damn, 2)
        print("Dd", motherfucker)

        rollingstone = rollingstone + 1
        damn = realData[rollingstone]
        motherfucker = realData[rollingstone]
        motherfucker = round(damn, 2)
        print("dd", motherfucker)

        rollingstone = rollingstone + 1
        damn = realData[rollingstone]
        motherfucker = realData[rollingstone]
        motherfucker = round(damn, 2)
        print("dD", motherfucker)

        print("--- End ---")

        #with open("relative fitness.txt", "a") as f:

if __name__ == "__main__":
    genDataSet()
    printDataSet()

    print(len(fData))
    print("run the script as the following to be interactive")
    print("python -i run.py")
