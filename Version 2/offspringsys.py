from random import randint as ri
class offspringSys:
    def countOffspring():
        print("Total offsprings:")
        print(rr_sum)
        print("\n")
    def genOffspring(fn, rrn, mrn, rr_sum):
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
