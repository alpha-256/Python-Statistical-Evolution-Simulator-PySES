from random import randint as ri
generation = 0
pop = int(input("Population? "))
"""
anyAlive()
reset array list
anyAlive()
"""
print("\n")
print("\n")
print("\n")
f = []
rr = []
mr = []
rr_sum = 0
survived = []
#===============================================================================
def gen():
    f.append(ri(0, 100))
    mr.append(ri(0, 5))
    rr.append(ri(0, 8))
#===============================================================================
#First generation
def pt1(f, rr, mr):
    global rr_sum
    x = 0
    while x < pop:
        gen()
        x = x + 1
    z = 0
    while z < pop:
        if f[z] > 75:
            print("Cell", z, "Survived")
            if rr[z] == 0:
                print("And has no offsprings")
            elif rr[z] > 0:
                print("And has", rr[z], "Offsprings")
                print("\n")
                rr_sum += rr[z]
        elif f[z] < 75:
            print("Cell", z, "Died")
            print("\n")
        z = z + 1
#===============================================================================
def countOffspring():
    print("Total offsprings:")
    print(rr_sum)
    print("\n")
    print("=====================================================================")
#===============================================================================
def genOffspring(fn, rrn, mrn, rr_sum):
    fn = []
    rrn = []
    mrn = []
    fn.append(ri(0, 100))
    mrn.append(ri(0, 5))
    rrn.append(ri(0, 8))
    x = 0
    while x < rr_sum:
        gen()
        x = x + 1
    z = 0
    while z < rr_sum:
        if fn[z] > 75:
            print("Cell", z, "Survived")
            if rrn[z] == 0:
                print("And has no offsprings")
            elif rrn[z] > 0:
                print("And has", rrn[z], "Offsprings")
                print("\n")
                rr_sum += rrn[z]
        elif fn[z] < 75:
            print("Cell", z, "Died")
            print("\n")
        z = z + 1
#===============================================================================
def generationCounter(generation):
    generation =  generation + 1
    print("Generation:", generation)
#===============================================================================
def anyAlive(f, rr, mr, fn, rrn, mrn, rr_sum):
    if rr_sum == 0:
        print("Species died")
        pass
        exit()
    elif rr_sum > 0:
        resetList(rr_sum, rrn, mrn, fn)
        genOffspring(f, rr, mr, rr_sum)
        generationCounter(generation)
        countOffspring()
    else:
        pass
#===============================================================================
def resetList(rr_sum, rrn, mrn, fn):
    fn = []
    rrn = []
    mrn = []

generationCounter(generation)
pt1(f, rr, mr)
anyAlive(f, rr, mr, fn, rrn, mrn, rr_sum)
