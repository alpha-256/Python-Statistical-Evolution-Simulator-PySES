from random import randint as ri

pop = int(input("Population? "))
print("\n")
print("Generation 1")
print("\n")
print("\n")
f = []
rr = []
mr = []
survived = []
def gen():
    f.append(ri(0, 100))
    mr.append(ri(0, 5))
def offspringGen():
    rr.append(ri(0, 8))
def pt1(f, rr, mr):
    x = 0
    while x < pop:
        gen()
        x = x + 1
    z = 0
    while z < pop:
        if f[z] > 75:
            offspringGen()
            print("Cell", z, "Survived")
            if rr[z] == 0:
                print("And has no offsprings")
            elif rr[z] > 0:
                print("And has", rr[z], "Offsprings")
                print("\n")
        elif f[z] < 75:
            print("Cell", z, "Died")
            print("\n")
        z = z + 1
pt1(f, rr, mr)
