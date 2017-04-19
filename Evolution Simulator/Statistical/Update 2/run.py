from start import base
from child import childGeneratiions
fData = []
realData = []
childData = []
rrData = []
childRR = []

if __name__ == "__main__":
    start.genDataSet()
    start.printDataSet(childData, rrData)

    print(childData)
    print("run the script as the following to be interactive")
    print("python -i run.py")
