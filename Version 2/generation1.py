from random import randint as ri
from statsgen import statsControl
class firstGen:
    def pt1(f, rr, mr, pop):
        global rr_sum
        x = 0
        while x < pop:
            statsControl.gen()
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
