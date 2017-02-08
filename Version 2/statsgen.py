from random import randint as ri
class statsControl:
    f = []
    rr = []
    mr = []
    def gen():
        f.append(ri(0, 100))
        mr.append(ri(0, 5))
        rr.append(ri(0, 8))
    def generationCounter(generation):
        generation =  generation + 1
        print("Generation:", generation)
        print("=====================================================================")
    def resetList():
        fn = []
        rrn = []
        mrn = []
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
