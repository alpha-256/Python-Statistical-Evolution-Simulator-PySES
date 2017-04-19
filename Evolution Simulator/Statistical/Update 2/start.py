from random import randint as ri
import math
class base:
    def genDat(fData=None):
        """
        Generate 3 value: survivalRate, survivalPercent, reproductiveRate
        """

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

    def genDataSet(population=101):

        for _ in range(population):
            genDat(fData)

        divMax(fData, realData)

        return

    def printDataSet(childData, rrData):

        survivors = 0

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

            #with open("relative fitness.txt", "a") as f:

        #Survivor Counter
        print(survivors, "Parents Survived")
