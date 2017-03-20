from random import randint as ri
import math

fData = []
realData = []
def genDat(fData):
    survivalRate = int(ri(0,50))
    survivalPercent = survivalRate / 10
    reproductiveRate = int(ri(0,4))
    fData.append(survivalPercent * reproductiveRate)
    pass

def divMax(fData, realData):
    dataRoller = 0
    maxData = max(fData)
    int(maxData)
    for data in fData:
        rolledData = fData[dataRoller]
        int(rolledData)
        cuck = rolledData / maxData
        realData.append(cuck)
        dataRoller = dataRoller + 1
    pass

looper = 0
while looper < 4 :
    genDat(fData)
    looper = looper + 1
divMax(fData, realData)
print(realData)

rollingstone = 0

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

#with open("relative fitness.txt", "a") as f:
